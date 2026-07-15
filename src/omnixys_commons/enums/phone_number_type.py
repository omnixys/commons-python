from enum import StrEnum


class PhoneNumberType(StrEnum):
    WHATSAPP = "WHATSAPP"
    MOBILE = "MOBILE"
    PRIVATE = "PRIVATE"
    WORK = "WORK"
    HOME = "HOME"
    OTHER = "OTHER"
