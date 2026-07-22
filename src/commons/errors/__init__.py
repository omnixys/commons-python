from commons.errors.conversation import (
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
from commons.errors.error_code import ERROR_CODES, ErrorCode, is_error_code
from commons.errors.event import (
    EventAlreadyExistsException,
    EventClosedException,
    EventNotFoundException,
)
from commons.errors.framework_exception import ExceptionContext, OmnixysException, with_metadata
from commons.errors.invitation import (
    InvitationAlreadyApprovedException,
    InvitationAlreadyExistsException,
    InvitationNotFoundException,
)
from commons.errors.notification import (
    NotificationChannelUnavailableException,
    NotificationNotFoundException,
)
from commons.errors.seat import (
    SeatAlreadyReservedException,
    SeatCapacityExceededException,
    SeatNotFoundException,
)
from commons.errors.ticket import (
    TicketAlreadyScannedException,
    TicketNotFoundException,
    TicketRevokedException,
)
from commons.errors.user import (
    UserAlreadyExistsException,
    UserEmailAlreadyExistsException,
    UserNotFoundException,
)

__all__ = [
    "ERROR_CODES",
    "ConversationAccessDeniedException",
    "ConversationAssignmentConflictException",
    "ConversationChannelUnavailableException",
    "ConversationClosedException",
    "ConversationDuplicateException",
    "ConversationNotFoundException",
    "ConversationStateInvalidException",
    "ErrorCode",
    "EventAlreadyExistsException",
    "EventClosedException",
    "EventNotFoundException",
    "ExceptionContext",
    "InvitationAlreadyApprovedException",
    "InvitationAlreadyExistsException",
    "InvitationNotFoundException",
    "NotificationChannelUnavailableException",
    "NotificationNotFoundException",
    "OmnixysException",
    "QuickReplyDuplicateException",
    "QuickReplyNotFoundException",
    "SeatAlreadyReservedException",
    "SeatCapacityExceededException",
    "SeatNotFoundException",
    "TicketAlreadyScannedException",
    "TicketNotFoundException",
    "TicketRevokedException",
    "UserAlreadyExistsException",
    "UserEmailAlreadyExistsException",
    "UserNotFoundException",
    "is_error_code",
    "with_metadata",
]
