class Actions:
    LIST = 'list'
    CREATE = 'create'
    UPDATE = 'update'
    PARTIAL_UPDATE = 'partial_update'
    DESTROY = 'destroy'
    Retrieve = 'retrieve'
    VIEW = 'view'


class Method:
    GET = 'get'
    HEAD = 'head'
    OPTIONS = 'options'
    POST = 'post'
    PUT = 'put'
    PATCH = 'patch'
    DELETE = 'delete'


class UserRole:
    ADMIN = "admin"
    NORMAL_USER = "normal_user"


class PaymentMethod:
    PREPAID = 'PREPAID'
    CHQ = 'CHQ'
    CASH = "CASH"
    CREDITCARD = "CREDITCARD"


class FieldConstants:
    PHONE_NUMBER_LENGTH = 12
    ADDRESS_LENGTH = 200
    NAME_LENGTH = 200
    MAX_LENGTH = 255
    FULL_DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
    DATE_TIME_FORMAT = "%Y-%m-%d %H:%M"
    DATE_FORMAT = "%Y-%m-%d"
    FULL_TIME_FORMAT = "%H:%M:%S"
    TIME_FORMAT = "%H:%M"
    INTEGRATION_DATE_FORMAT = "%m/%d/%Y"
    MULTIPLE_DATE_FORMATS = ("%m/%d/%Y", "%m-%d-%Y",
                             "%d-%m-%Y", "%d/%m/%Y", "%Y-%m-%d")
    START_TIME = "09:00"
    END_TIME = "18:00"
    DEFAULT_PROCESSING_TIME = 0


class DurationConstants:
    TWO_HRS = 120
    SIX_HRS = 360
    TWELVE_HRS = 720
    TWENTY_FORE_HRS = 1440


class PaymentChargeConstants:
    THIRTY_RS = 30
    FIFTY_RS = 50
    HUNDRED_RS = 100
    ONE_FIFTY_RS = 150


class SlotStatusConstants:
    EMPTY_BOOKED_SLOT = "EMPTY_BOOKED_SLOT"
    PARTIAL_BOOKED_SLOT = "PARTIAL_BOOKED_SLOT"
    FULL_BOOKED_SLOT = "FULL_BOOKED_SLOT"


class VehicleTypeConstants:
    TWO_WHEELER = "TWO_WHEELER"
    THREE_WHEELER = "THREE_WHEELER"
    FOUR_WHEELER = "FOUR_WHEELER"
    SIX_WHEELER = "SIX_WHEELER"
    EIGHT_WHEELER = "EIGHT_WHEELER"
    OTHER = "OTHER"
