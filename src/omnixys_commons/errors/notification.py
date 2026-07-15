from __future__ import annotations

from omnixys_commons.errors.error_code import ErrorCode
from omnixys_commons.errors.framework_exception import OmnixysException


class NotificationNotFoundException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.NOTIFICATION_NOT_FOUND, "Notification was not found", **kwargs)  # type: ignore[arg-type]


class NotificationChannelUnavailableException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.NOTIFICATION_CHANNEL_UNAVAILABLE, "Notification channel is unavailable", **kwargs)  # type: ignore[arg-type]
