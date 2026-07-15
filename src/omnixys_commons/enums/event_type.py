from enum import StrEnum


class EventType(StrEnum):
    LOG = "LOG"
    EVENT = "EVENT"
    METRIC = "METRIC"
    ALERT = "ALERT"
    COMMAND = "COMMAND"
