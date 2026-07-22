from enum import StrEnum


class StatusType(StrEnum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    BLOCKED = "BLOCKED"
    PENDING = "PENDING"
    SUSPENDED = "SUSPENDED"
    CLOSED = "CLOSED"
