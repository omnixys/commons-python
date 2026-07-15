from __future__ import annotations

from omnixys_commons.errors.error_code import ErrorCode
from omnixys_commons.errors.framework_exception import OmnixysException


class EventNotFoundException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.EVENT_NOT_FOUND, "Event was not found", **kwargs)  # type: ignore[arg-type]


class EventAlreadyExistsException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.EVENT_ALREADY_EXISTS, "Event already exists", **kwargs)  # type: ignore[arg-type]


class EventClosedException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.EVENT_CLOSED, "Event is closed", **kwargs)  # type: ignore[arg-type]
