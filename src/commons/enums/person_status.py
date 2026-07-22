from enum import StrEnum


class PersonStatusType(StrEnum):
    ACTIVE = "ACTIVE"
    DISABLED = "DISABLED"
    DELETED = "DELETED"
    INACTIVE = "INACTIVE"
    BLOCKED = "BLOCKED"
    CLOSED = "CLOSED"
