from __future__ import annotations

from commons.errors.error_code import ErrorCode
from commons.errors.framework_exception import OmnixysException


class UserNotFoundException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.USER_NOT_FOUND, "User was not found", **kwargs)  # type: ignore[arg-type]


class UserAlreadyExistsException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.USER_ALREADY_EXISTS, "User already exists", **kwargs)  # type: ignore[arg-type]


class UserEmailAlreadyExistsException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.USER_EMAIL_ALREADY_EXISTS, "A user with this email already exists", **kwargs)  # type: ignore[arg-type]
