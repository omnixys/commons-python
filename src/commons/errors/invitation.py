from __future__ import annotations

from commons.errors.error_code import ErrorCode
from commons.errors.framework_exception import OmnixysException


class InvitationNotFoundException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.INVITATION_NOT_FOUND, "Invitation was not found", **kwargs)  # type: ignore[arg-type]


class InvitationAlreadyExistsException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.INVITATION_ALREADY_EXISTS, "Invitation already exists", **kwargs)  # type: ignore[arg-type]


class InvitationAlreadyApprovedException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.INVITATION_ALREADY_APPROVED, "Invitation has already been approved", **kwargs)  # type: ignore[arg-type]
