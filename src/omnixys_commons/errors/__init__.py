from omnixys_commons.errors.conversation import (
    ConversationAccessDeniedException,
    ConversationAssignmentConflictException,
    ConversationChannelUnavailableException,
    ConversationClosedException,
    ConversationDuplicateException,
    ConversationNotFoundException,
    ConversationStateInvalidException,
    QuickReplyDuplicateException,
    QuickReplyNotFoundException,
)
from omnixys_commons.errors.error_code import ERROR_CODES, ErrorCode, is_error_code
from omnixys_commons.errors.event import (
    EventAlreadyExistsException,
    EventClosedException,
    EventNotFoundException,
)
from omnixys_commons.errors.framework_exception import ExceptionContext, OmnixysException, with_metadata
from omnixys_commons.errors.invitation import (
    InvitationAlreadyApprovedException,
    InvitationAlreadyExistsException,
    InvitationNotFoundException,
)
from omnixys_commons.errors.notification import (
    NotificationChannelUnavailableException,
    NotificationNotFoundException,
)
from omnixys_commons.errors.seat import (
    SeatAlreadyReservedException,
    SeatCapacityExceededException,
    SeatNotFoundException,
)
from omnixys_commons.errors.ticket import (
    TicketAlreadyScannedException,
    TicketNotFoundException,
    TicketRevokedException,
)
from omnixys_commons.errors.user import (
    UserAlreadyExistsException,
    UserEmailAlreadyExistsException,
    UserNotFoundException,
)

__all__ = [
    "ErrorCode",
    "ERROR_CODES",
    "is_error_code",
    "OmnixysException",
    "ExceptionContext",
    "with_metadata",
    "ConversationNotFoundException",
    "ConversationAccessDeniedException",
    "ConversationStateInvalidException",
    "ConversationAssignmentConflictException",
    "ConversationClosedException",
    "ConversationChannelUnavailableException",
    "ConversationDuplicateException",
    "QuickReplyNotFoundException",
    "QuickReplyDuplicateException",
    "EventNotFoundException",
    "EventAlreadyExistsException",
    "EventClosedException",
    "InvitationNotFoundException",
    "InvitationAlreadyExistsException",
    "InvitationAlreadyApprovedException",
    "NotificationNotFoundException",
    "NotificationChannelUnavailableException",
    "SeatNotFoundException",
    "SeatAlreadyReservedException",
    "SeatCapacityExceededException",
    "TicketNotFoundException",
    "TicketRevokedException",
    "TicketAlreadyScannedException",
    "UserNotFoundException",
    "UserAlreadyExistsException",
    "UserEmailAlreadyExistsException",
]
