from .constants import PaymentMethod, SlotStatusConstants, VehicleTypeConstants

PAYMENT_TYPE_CHOICES = (
    (PaymentMethod.PREPAID, "Prepaid"),
    (PaymentMethod.CASH, "Cash"),
    (PaymentMethod.CHQ, "Cheque"),
    (PaymentMethod.CREDITCARD, "Credit Card")
)

SLOT_STATUS_CHOICES = (
    (SlotStatusConstants.EMPTY_BOOKED_SLOT, "Empty Slot"),
    (SlotStatusConstants.PARTIAL_BOOKED_SLOT, "Partial Slot"),
    (SlotStatusConstants.FULL_BOOKED_SLOT, "Full Slot"),
)

VEHICLE_TYPE_CHOICES = (
    (VehicleTypeConstants.TWO_WHEELER, "2 Wheeler"),
    (VehicleTypeConstants.THREE_WHEELER, "3 Wheeler"),
    (VehicleTypeConstants.FOUR_WHEELER, "4 wheeler"),
    (VehicleTypeConstants.SIX_WHEELER, "6 wheeler"),
    (VehicleTypeConstants.EIGHT_WHEELER, "8 wheeler"),
    (VehicleTypeConstants.OTHER, "Other")
)
