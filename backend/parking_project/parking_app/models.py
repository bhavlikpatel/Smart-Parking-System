from django.db import models
from django.contrib.auth.models import User
from . import constants, choices
from core import models as core_model
from admin_management import models as admin_models


class FixedSlot(core_model.BaseModel):
    plot = models.ForeignKey(admin_models.Plot, related_name="plot_slots", on_delete=models.CASCADE, null=True, blank=True)
    slot_id = models.CharField(verbose_name="Slot ID", max_length=200, unique=True)

    def __str__(self):
        return f"{self.id}"


class Slot(core_model.BaseModel):
    slot_date = models.DateField(verbose_name="Slot Date")
    reference_number = models.CharField(max_length=25, verbose_name="Reference Number", null=True, blank=True)
    is_booked = models.BooleanField(default=False)
    plot = models.ForeignKey(admin_models.Plot, related_name="plot_user_slots", on_delete=models.CASCADE, null=True, blank=True)
    fixed_slot = models.ForeignKey(FixedSlot, verbose_name="Fixed Slot", related_name="fixed_user_slots", on_delete=models.CASCADE, null=True, blank=True)
    slot_status = models.CharField(default=constants.SlotStatusConstants.EMPTY_BOOKED_SLOT,
                                   choices=choices.SLOT_STATUS_CHOICES,
                                   verbose_name="Slot Status", max_length=25)
    from_time = models.TimeField(blank=True, null=True, verbose_name="From Time")
    to_time = models.TimeField(blank=True, null=True, verbose_name="To Time")
    # Vehicle Fields
    vehicle_plat_no = models.CharField(max_length=15, verbose_name="Vehicle No", null=True, blank=True)
    vehicle_type = models.CharField(verbose_name="Vehicle Type", default=constants.VehicleTypeConstants.FOUR_WHEELER,
                                    choices=choices.VEHICLE_TYPE_CHOICES, max_length=30)
    # Payment Fields
    payment_method = models.CharField(default=constants.PaymentMethod.CASH, choices=choices.PAYMENT_TYPE_CHOICES,
                                      verbose_name="Payment Method", max_length=25)
    amount = models.PositiveIntegerField(default=0)
    # User Fields
    contact_number = models.CharField(max_length=10, verbose_name="Contact Number", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.id}"
