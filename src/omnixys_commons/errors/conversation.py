from __future__ import annotations

from omnixys_commons.errors.error_code import ErrorCode
from omnixys_commons.errors.framework_exception import OmnixysException


class ConversationNotFoundException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.CONVERSATION_NOT_FOUND, "Conversation was not found", **kwargs)  # type: ignore[arg-type]


class ConversationAccessDeniedException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.CONVERSATION_ACCESS_DENIED, "Access denied to conversation", **kwargs)  # type: ignore[arg-type]


class ConversationStateInvalidException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(
            ErrorCode.CONVERSATION_STATE_INVALID,
            "Conversation is in an invalid state for this operation",
            **kwargs,  # type: ignore[arg-type]
        )


class ConversationAssignmentConflictException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.CONVERSATION_ASSIGNMENT_CONFLICT, "Assignment conflict on conversation", **kwargs)  # type: ignore[arg-type]


class ConversationClosedException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.CONVERSATION_CLOSED, "Conversation is closed", **kwargs)  # type: ignore[arg-type]


class ConversationChannelUnavailableException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.CONVERSATION_CHANNEL_UNAVAILABLE, "Conversation channel is unavailable", **kwargs)  # type: ignore[arg-type]


class ConversationDuplicateException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(
            ErrorCode.CONVERSATION_DUPLICATE,
            "A conversation with these parameters already exists",
            **kwargs,  # type: ignore[arg-type]
        )


class QuickReplyNotFoundException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.QUICK_REPLY_NOT_FOUND, "Quick reply was not found", **kwargs)  # type: ignore[arg-type]


class QuickReplyDuplicateException(OmnixysException):
    def __init__(self, **kwargs: object) -> None:
        super().__init__(ErrorCode.QUICK_REPLY_DUPLICATE, "Quick reply with this key already exists", **kwargs)  # type: ignore[arg-type]
