from __future__ import annotations

from omnixys_commons.errors.error_code import ErrorCode
from omnixys_commons.errors.framework_exception import OmnixysException


class TicketNotFoundException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.TICKET_NOT_FOUND, "Ticket was not found", **kwargs)  # type: ignore[arg-type]


class TicketRevokedException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.TICKET_REVOKED, "Ticket has been revoked", **kwargs)  # type: ignore[arg-type]


class TicketAlreadyScannedException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.TICKET_ALREADY_SCANNED, "Ticket has already been scanned", **kwargs)  # type: ignore[arg-type]
