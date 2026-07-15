from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class EventPermissionKey(StrEnum):
    VIEW_EVENT = "event.view"
    EDIT_EVENT = "event.edit"
    DELETE_EVENT = "event.delete"
    VIEW_GUESTS = "guests.view"
    MANAGE_GUESTS = "guests.manage"
    APPROVE_GUESTS = "guests.approve"
    EXPORT_GUESTS = "guests.export"
    VIEW_INVITATIONS = "invitations.view"
    MANAGE_INVITATIONS = "invitations.manage"
    VIEW_SEATS = "seats.view"
    VIEW_SELF_SEAT = "seats.self.view"
    MANAGE_SEATS = "seats.manage"
    VIEW_TICKETS = "tickets.view"
    VIEW_SELF_TICKET = "tickets.self.view"
    MANAGE_TICKETS = "tickets.manage"
    SCAN_TICKETS = "tickets.scan"
    MANAGE_PLUS_ONES = "plus_ones.manage"
    MANAGE_SELF_PLUS_ONES = "plus_ones.self.manage"
    VIEW_ANALYTICS = "analytics.view"
    VIEW_SUPPORT = "support.view"
    MANAGE_SUPPORT = "support.manage"
    RESPOND_SUPPORT = "support.respond"
    VIEW_NOTIFICATIONS = "notifications.view"
    SEND_NOTIFICATIONS = "notifications.send"
    VIEW_TIMELINE = "timeline.view"
    MANAGE_TIMELINE = "timeline.manage"
    VIEW_EVENT_SETTINGS = "settings.view"
    MANAGE_EVENT_SETTINGS = "settings.manage"
    VIEW_ROLES = "roles.view"
    MANAGE_ROLES = "roles.manage"
    VIEW_STAFF = "staff.view"
    MANAGE_STAFF = "staff.manage"
    VIEW_MEDIA = "media.view"
    MANAGE_MEDIA = "media.manage"
    EXPORT_DATA = "data.export"
    VIEW_AUDIT_LOG = "audit.view"


class EventPermissionCategory(StrEnum):
    EVENT = "event"
    GUESTS = "guests"
    INVITATIONS = "invitations"
    SEATS = "seats"
    TICKETS = "tickets"
    PLUS_ONES = "plus_ones"
    ANALYTICS = "analytics"
    SUPPORT = "support"
    NOTIFICATIONS = "notifications"
    TIMELINE = "timeline"
    SETTINGS = "settings"
    ROLES = "roles"
    STAFF = "staff"
    MEDIA = "media"
    DATA = "data"
    AUDIT = "audit"


@dataclass(frozen=True, slots=True)
class EventPermissionDefinition:
    key: EventPermissionKey
    category: EventPermissionCategory
    label: str
    description: str
    premium_feature_key: str | None = None


def _d(
    key: EventPermissionKey,
    cat: EventPermissionCategory,
    label: str,
    desc: str,
) -> EventPermissionDefinition:
    return EventPermissionDefinition(key, cat, label, desc)


EC = EventPermissionCategory

EVENT_PERMISSION_KEYS: tuple[EventPermissionKey, ...] = tuple(EventPermissionKey)

EPK = EventPermissionKey

EVENT_PERMISSION_DEFINITIONS: tuple[EventPermissionDefinition, ...] = (
    _d(EPK.VIEW_EVENT, EC.EVENT, "View Event", "Can view event details"),
    _d(EPK.EDIT_EVENT, EC.EVENT, "Edit Event", "Can edit event settings"),
    _d(EPK.DELETE_EVENT, EC.EVENT, "Delete Event", "Can delete the event"),
    _d(EPK.VIEW_GUESTS, EC.GUESTS, "View Guests", "Can view guest list"),
    _d(EPK.MANAGE_GUESTS, EC.GUESTS, "Manage Guests", "Can manage guests"),
    _d(EPK.APPROVE_GUESTS, EC.GUESTS, "Approve Guests", "Can approve guest invitations"),
    _d(EPK.EXPORT_GUESTS, EC.GUESTS, "Export Guests", "Can export guest data"),
    _d(EPK.VIEW_INVITATIONS, EC.INVITATIONS, "View Invitations", "Can view invitations"),
    _d(EPK.MANAGE_INVITATIONS, EC.INVITATIONS, "Manage Invitations", "Can manage invitations"),
    _d(EPK.VIEW_SEATS, EC.SEATS, "View Seats", "Can view seat assignments"),
    _d(EPK.VIEW_SELF_SEAT, EC.SEATS, "View Self Seat", "Can view own seat"),
    _d(EPK.MANAGE_SEATS, EC.SEATS, "Manage Seats", "Can manage seat assignments"),
    _d(EPK.VIEW_TICKETS, EC.TICKETS, "View Tickets", "Can view tickets"),
    _d(EPK.VIEW_SELF_TICKET, EC.TICKETS, "View Self Ticket", "Can view own ticket"),
    _d(EPK.MANAGE_TICKETS, EC.TICKETS, "Manage Tickets", "Can manage tickets"),
    _d(EPK.SCAN_TICKETS, EC.TICKETS, "Scan Tickets", "Can scan tickets at entry"),
    _d(EPK.MANAGE_PLUS_ONES, EC.PLUS_ONES, "Manage Plus Ones", "Can manage plus ones for guests"),
    _d(EPK.MANAGE_SELF_PLUS_ONES, EC.PLUS_ONES, "Manage Self Plus Ones", "Can manage own plus ones"),
    _d(EPK.VIEW_ANALYTICS, EC.ANALYTICS, "View Analytics", "Can view event analytics"),
    _d(EPK.VIEW_SUPPORT, EC.SUPPORT, "View Support", "Can view support conversations"),
    _d(EPK.MANAGE_SUPPORT, EC.SUPPORT, "Manage Support", "Can manage support assignments"),
    _d(EPK.RESPOND_SUPPORT, EC.SUPPORT, "Respond Support", "Can respond to support messages"),
    _d(EPK.VIEW_NOTIFICATIONS, EC.NOTIFICATIONS, "View Notifications", "Can view notifications"),
    _d(EPK.SEND_NOTIFICATIONS, EC.NOTIFICATIONS, "Send Notifications", "Can send notifications"),
    _d(EPK.VIEW_TIMELINE, EC.TIMELINE, "View Timeline", "Can view event timeline"),
    _d(EPK.MANAGE_TIMELINE, EC.TIMELINE, "Manage Timeline", "Can manage event timeline"),
    _d(EPK.VIEW_EVENT_SETTINGS, EC.SETTINGS, "View Settings", "Can view event settings"),
    _d(EPK.MANAGE_EVENT_SETTINGS, EC.SETTINGS, "Manage Settings", "Can manage event settings"),
    _d(EPK.VIEW_ROLES, EC.ROLES, "View Roles", "Can view role assignments"),
    _d(EPK.MANAGE_ROLES, EC.ROLES, "Manage Roles", "Can manage role assignments"),
    _d(EPK.VIEW_STAFF, EC.STAFF, "View Staff", "Can view staff list"),
    _d(EPK.MANAGE_STAFF, EC.STAFF, "Manage Staff", "Can manage staff assignments"),
    _d(EPK.VIEW_MEDIA, EC.MEDIA, "View Media", "Can view event media"),
    _d(EPK.MANAGE_MEDIA, EC.MEDIA, "Manage Media", "Can manage event media"),
    _d(EPK.EXPORT_DATA, EC.DATA, "Export Data", "Can export event data"),
    _d(EPK.VIEW_AUDIT_LOG, EC.AUDIT, "View Audit Log", "Can view audit log"),
)


def get_default_permissions_for_event_role(role: EventPermissionKey | str | None) -> list[EventPermissionKey]:
    from omnixys_commons.enums.event_role_type import EventRoleType

    if role is None:
        return []
    role_str = str(role) if not isinstance(role, str) else role
    try:
        event_role = EventRoleType(role_str)
    except ValueError:
        return []

    if event_role == EventRoleType.ADMIN:
        return list(EventPermissionKey)
    if event_role == EventRoleType.SECURITY:
        return [EventPermissionKey.VIEW_STAFF, EventPermissionKey.MANAGE_STAFF, EventPermissionKey.SCAN_TICKETS]
    if event_role == EventRoleType.GUEST:
        return [
            EventPermissionKey.VIEW_EVENT,
            EventPermissionKey.VIEW_SELF_TICKET,
            EventPermissionKey.VIEW_SELF_SEAT,
            EventPermissionKey.MANAGE_SELF_PLUS_ONES,
            EventPermissionKey.VIEW_TIMELINE,
        ]
    if event_role == EventRoleType.SUPPORT:
        return [
            EventPermissionKey.VIEW_EVENT,
            EventPermissionKey.VIEW_SUPPORT,
            EventPermissionKey.RESPOND_SUPPORT,
            EventPermissionKey.VIEW_NOTIFICATIONS,
        ]
    return []
