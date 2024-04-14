from rest_framework import viewsets, mixins
from django.utils import timezone
from lib.paginators import CustomPagination
from . import models
from . import serializers
from core.views import BaseViewSet, BaseGenericViewSet
from lib.constants import Actions, Method
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from . import helpers
from . import constants
from admin_management import models as admin_models
from . import filters

class SlotViewSet(BaseViewSet):
    pagination_class = CustomPagination
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    search_fields = ('reference_number', 'vehicle_plat_no', 'contact_number', 'vehicle_type', 'slot_id', 'slot_date')

    dynamic_serializers = {
        Actions.LIST: serializers.SlotListSerializer,
        Actions.Retrieve: serializers.SlotSerializer,
        Actions.VIEW: serializers.SlotDetailSerializer
    }

    def get_queryset(self):
        user = self.request.user
        queryset = models.Slot.objects.filter(user=user, is_booked=True)
        return queryset

    @action(methods=[Method.GET], detail=True)
    def get_booked_slot_detail(self, request, pk, *args, **kwargs):
        slot_date = self.request.query_params.get('slot_date')
        if not slot_date:
            slot_date = timezone.now().date()
        user_slots = models.Slot.objects.filter(fixed_slot=pk, slot_date=slot_date)
        serializer = serializers.SlotSerializer(user_slots, many=True)
        if serializer:
            return Response(data={"data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"errors": "Data Does Not exist"}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=[Method.GET], detail=False)
    def get_payment_from_time_windows(self, request, *args, **kwargs):
        from_time = self.request.query_params.get('from_time')
        to_time = self.request.query_params.get('to_time')
        if from_time and to_time:
            date = timezone.now().date()
            start_time = helpers.convert_date_and_time_into_datetime(date=date, time=from_time)
            end_time = helpers.convert_date_and_time_into_datetime(date=date, time=to_time)
            duration = end_time - start_time if start_time and end_time else 0
            amount = 0
            if duration:
                duration = duration.seconds // 60  # convert into Minutes
                if int(duration) <= constants.DurationConstants.TWO_HRS:
                    amount = 30
                elif constants.DurationConstants.TWO_HRS < int(duration) <= constants.DurationConstants.SIX_HRS:
                    amount = 50
                elif constants.DurationConstants.SIX_HRS < int(duration) <= constants.DurationConstants.TWELVE_HRS:
                    amount = 100
                elif constants.DurationConstants.TWELVE_HRS < int(
                        duration) <= constants.DurationConstants.TWENTY_FORE_HRS:
                    amount = 150

            return Response(data={"amount": amount}, status=status.HTTP_200_OK)
        return Response({"errors": "Data Does Not exist"}, status=status.HTTP_400_BAD_REQUEST)


class FixedSlotListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, BaseGenericViewSet):
    serializer_class = serializers.FixedSlotSerializer
    queryset = models.FixedSlot.objects.all()
    search_fields = ('plot__id', 'plot__plot_name', 'plot__plot_id')
    filterset_class = filters.FixedSlotFilter


class PlotSlotListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, BaseGenericViewSet):
    serializer_class = serializers.PlotSlotsSerializer
    queryset = admin_models.Plot.objects.all()
    search_fields = ('plot_name', 'city', 'plot_id')
