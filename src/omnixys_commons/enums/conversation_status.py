from enum import StrEnum


class ConversationStatus(StrEnum):
    OPEN = "OPEN"
    ASSIGNED = "ASSIGNED"
    PENDING = "PENDING"
    RESOLVED = "RESOLVED"
    CLOSED = "CLOSED"
