from __future__ import annotations

from omnixys_commons.errors.error_code import ErrorCode
from omnixys_commons.errors.framework_exception import OmnixysException


class SeatNotFoundException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.SEAT_NOT_FOUND, "Seat was not found", **kwargs)  # type: ignore[arg-type]


class SeatAlreadyReservedException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.SEAT_ALREADY_RESERVED, "Seat is already reserved", **kwargs)  # type: ignore[arg-type]


class SeatCapacityExceededException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.SEAT_CAPACITY_EXCEEDED, "Seat capacity has been exceeded", **kwargs)  # type: ignore[arg-type]
