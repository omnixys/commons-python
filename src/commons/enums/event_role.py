from enum import StrEnum


class EventRoleType(StrEnum):
    ADMIN = "ADMIN"
    SECURITY = "SECURITY"
    GUEST = "GUEST"
    SUPPORT = "SUPPORT"
