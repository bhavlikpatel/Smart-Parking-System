import random
from . import models
from .lib import common_serializers
from rest_framework import serializers
from . import constants
from djoser.conf import settings
from django.utils import timezone
from lib.constants import UserRole
from admin_management import models as admin_models


class TokenSerializer(serializers.ModelSerializer):
    token = serializers.CharField(source="key")
    user_type = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()

    def get_user_id(self, instance):
        return instance.user.id

    def get_user_type(self, instance):
        return UserRole.ADMIN if instance.user.is_superuser else UserRole.NORMAL_USER

    def get_username(self, instance):
        return instance.user.username

    class Meta:
        model = settings.TOKEN_MODEL
        fields = ("token", "user_type", "username", "user_id")


class SlotListSerializer(common_serializers.DynamicFieldsModelSerializer):
    class Meta:
        model = models.Slot
        fields = (
            "id", "slot_date", "reference_number", "slot_status", "from_time", "to_time",
            "is_booked", "vehicle_plat_no", "vehicle_type", "payment_method", "amount", "contact_number", "plot", "fixed_slot"
        )

    def validate(self, attrs):
        return attrs


class SlotDetailSerializer(common_serializers.DynamicFieldsModelSerializer):
    class Meta:
        model = models.Slot
        fields = (
            "id", "slot_date", "reference_number", "slot_status", "from_time", "to_time",
            "is_booked", "vehicle_plat_no", "vehicle_type", "payment_method", "amount", "contact_number", "plot", "fixed_slot"
        )


class SlotSerializer(common_serializers.DynamicFieldsModelSerializer):
    from_time = serializers.CharField(required=True)
    to_time = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)
    slot_date = serializers.DateField(required=True)
    contact_number = serializers.CharField(required=True)
    slot_status = serializers.SerializerMethodField()
    plot = serializers.CharField(required=True)
    fixed_slot = serializers.CharField(required=True)

    def get_slot_status(self, instance: models.Slot):
        date = timezone.now().date()
        if instance.id:
            user_slots = models.Slot.objects.filter(slot_date=date, id=instance.id)
            total_hours = 0
            for user_slot in user_slots:
                total_hours += int(user_slot.to_time.strftime("%H")) - int(user_slot.from_time.strftime("%H"))
            if 0 < total_hours < 23:
                return constants.SlotStatusConstants.PARTIAL_BOOKED_SLOT
            elif total_hours in [23, 24]:
                return constants.SlotStatusConstants.FULL_BOOKED_SLOT
            else:
                return constants.SlotStatusConstants.EMPTY_BOOKED_SLOT
        return constants.SlotStatusConstants.EMPTY_BOOKED_SLOT

    class Meta:
        model = models.Slot
        fields = (
            "id", "slot_date", "reference_number", "slot_status", "from_time", "to_time",
            "is_booked", "vehicle_plat_no", "vehicle_type", "payment_method", "amount", "contact_number", "plot", "fixed_slot"
        )

    def validate_contact_number(self, contact_number):
        if not len(contact_number) == 10:
            raise serializers.ValidationError(f"contact number should be 12 digit")
        return contact_number

    def validate_fixed_slot(self, fixed_slot):
        slot_obj = models.FixedSlot.objects.filter(id=fixed_slot).last()
        if not slot_obj:
            raise serializers.ValidationError(f"{fixed_slot} slot Does not exist")
        return slot_obj

    def validate_plot(self, plot):
        plot_obj = admin_models.Plot.objects.filter(id=plot).last()
        if not plot_obj:
            raise serializers.ValidationError(f"{plot} Plot Does not exist")
        return plot_obj

    def validate(self, attrs):
        from . import helpers
        from_time = attrs.get('from_time')
        to_time = attrs.get('to_time')
        slot_date = attrs.get('slot_date')
        fixed_slot = attrs.get('fixed_slot')
        fixed_slot = models.FixedSlot.objects.filter(id=fixed_slot.id).last()
        if not fixed_slot:
            raise serializers.ValidationError(f"There is Some issue with Slot ID {fixed_slot.id}")

        if not from_time:
            raise serializers.ValidationError(f"From time required")
        if not to_time:
            raise serializers.ValidationError(f"To time required")
        # Time Validation
        start_time = helpers.convert_date_and_time_into_datetime(date=slot_date, time=from_time)
        end_time = helpers.convert_date_and_time_into_datetime(date=slot_date, time=to_time)
        user_slots = models.Slot.objects.filter(slot_date=slot_date, fixed_slot=fixed_slot)
        from datetimerange import DateTimeRange
        time_windows_list = []
        for user_slot in user_slots:
            user_start_time = helpers.convert_date_and_time_into_datetime(date=slot_date,
                                                                          time=user_slot.from_time.strftime("%H:%M"))
            user_end_time = helpers.convert_date_and_time_into_datetime(date=slot_date,
                                                                        time=user_slot.to_time.strftime("%H:%M"))
            time_range1 = DateTimeRange(start_time, end_time)
            time_range2 = DateTimeRange(user_start_time, user_end_time)
            tem3 = time_range1.intersection(time_range2)
            if tem3.start_datetime and tem3.end_datetime:  # If overlap
                time_windows_list.append(f"{user_slot.from_time} to {user_slot.to_time}")
        if time_windows_list:
            time_intervals = ",".join(time_windows_list)
            raise serializers.ValidationError(f"Slot already booked for following time windows: {time_intervals}")

        # Payment Validation
        duration = end_time - start_time if start_time and end_time else 0
        if duration:
            duration = duration.seconds // 60  # convert into Minutes
            amount = attrs.get('amount')
            if not amount:
                raise serializers.ValidationError("Amount is required")
            if int(duration) <= constants.DurationConstants.TWO_HRS:
                if amount < constants.PaymentChargeConstants.THIRTY_RS:
                    raise serializers.ValidationError("Minimum 30 rs amount required for up to 2 hours parking")
            elif constants.DurationConstants.TWO_HRS < int(duration) <= constants.DurationConstants.SIX_HRS:
                if amount < constants.PaymentChargeConstants.FIFTY_RS:
                    raise serializers.ValidationError("Minimum 50 rs amount required for up to 6 hours parking")
            elif constants.DurationConstants.SIX_HRS < int(duration) <= constants.DurationConstants.TWELVE_HRS:
                if amount < constants.PaymentChargeConstants.HUNDRED_RS:
                    raise serializers.ValidationError("Minimum 100 rs amount required for up to 12 hours parking")
            elif constants.DurationConstants.TWELVE_HRS < int(duration) <= constants.DurationConstants.TWENTY_FORE_HRS:
                if amount < constants.PaymentChargeConstants.ONE_FIFTY_RS:
                    raise serializers.ValidationError("Minimum 150 rs amount required for up to 24 hours parking")

        return attrs

    def create(self, validated_data):
        slot_date = validated_data['slot_date']
        user = self.context['request'].user
        if user:
            validated_data['user'] = user
        else:
            raise serializers.ValidationError("user does not have slot create permission")
        last_slot = models.Slot.objects.last()
        if last_slot:
            last_slot_id = last_slot.id
        else:
            last_slot_id = random.randint(111, 999999)
        validated_data['reference_number'] = f"STKT000{last_slot_id}"
        slot = super(SlotSerializer, self).create(validated_data=validated_data)
        return slot


class FixedSlotSerializer(common_serializers.DynamicFieldsModelSerializer):
    is_booked = serializers.SerializerMethodField()
    slot_status = serializers.SerializerMethodField()
    plot_name = serializers.SerializerMethodField()
    plot_id = serializers.SerializerMethodField()

    def get_plot_name(self, instance: models.FixedSlot):
        if instance.plot:
            return instance.plot.plot_name
        return None

    def get_plot_id(self, instance: models.FixedSlot):
        if instance.plot:
            return instance.plot.plot_id
        return None

    def get_is_booked(self, instance: models.FixedSlot):
        date = timezone.now().date()
        if instance.id:
            user_slot = models.Slot.objects.filter(slot_date=date, fixed_slot=instance.id)
            if user_slot:
                return True
        return False

    def get_slot_status(self, instance: models.FixedSlot):
        date = timezone.now().date()
        if instance.id:
            user_slots = models.Slot.objects.filter(slot_date=date, fixed_slot=instance.id)
            total_hours = 0
            for user_slot in user_slots:
                total_hours += int(user_slot.to_time.strftime("%H")) - int(user_slot.from_time.strftime("%H"))
            if 0 < total_hours < 23:
                return constants.SlotStatusConstants.PARTIAL_BOOKED_SLOT
            elif total_hours in [23, 24]:
                return constants.SlotStatusConstants.FULL_BOOKED_SLOT
            else:
                return constants.SlotStatusConstants.EMPTY_BOOKED_SLOT
        return constants.SlotStatusConstants.EMPTY_BOOKED_SLOT

    class Meta:
        model = models.FixedSlot
        fields = ("id", "slot_id", "is_booked", "slot_status", "plot", "plot_name", "plot_id")


class PlotSlotsSerializer(common_serializers.DynamicFieldsModelSerializer):
    plot_slots = serializers.SerializerMethodField()

    def get_plot_slots(self, instance: admin_models.Plot):
        plot_fixed_slots = models.FixedSlot.objects.filter(plot=instance)
        date = timezone.now().date()
        plot_data = []
        for fixed_slot in plot_fixed_slots:
            is_booked = False
            total_hours = 0
            fixed_slot_data = {}
            slot_status = constants.SlotStatusConstants.EMPTY_BOOKED_SLOT
            if fixed_slot.id:
                user_slots = models.Slot.objects.filter(slot_date=date, fixed_slot=fixed_slot.id).order_by('fixed_slot')
                if user_slots:
                    for user_slot in user_slots:
                        if user_slots:
                            is_booked = True
                        total_hours += int(user_slot.to_time.strftime("%H")) - int(user_slot.from_time.strftime("%H"))
                        if 0 < total_hours < 23:
                            slot_status = constants.SlotStatusConstants.PARTIAL_BOOKED_SLOT
                        elif total_hours in [23, 24]:
                            slot_status = constants.SlotStatusConstants.FULL_BOOKED_SLOT

                        fixed_slot_data = {
                            "id": fixed_slot.id,
                            "slot_id": fixed_slot.id,
                            "is_booked": is_booked,
                            "slot_status": slot_status,
                        }
                    plot_data.append(fixed_slot_data)
                else:
                    fixed_slot_data = {
                        "id": fixed_slot.id,
                        "slot_id": fixed_slot.slot_id,
                        "is_booked": is_booked,
                        "slot_status": slot_status,
                    }
                    plot_data.append(fixed_slot_data)
        return plot_data

    class Meta:
        model = admin_models.Plot
        fields = ("id", "plot_id", "plot_name", "city", "plot_slots", "plot_address")
