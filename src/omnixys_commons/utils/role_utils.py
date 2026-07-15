from __future__ import annotations

from collections.abc import Iterable

from omnixys_commons.enums.event_permission_key import EVENT_PERMISSION_KEYS, EventPermissionKey
from omnixys_commons.enums.event_role_type import EventRoleType


class EventSystemRoleKey:
    ADMIN = "ADMIN"
    SECURITY = "SECURITY"
    GUEST = "GUEST"


STAFF_VIEW_PERMISSIONS: list[EventPermissionKey] = [
    EventPermissionKey.VIEW_EVENT,
    EventPermissionKey.VIEW_GUESTS,
    EventPermissionKey.VIEW_TICKETS,
    EventPermissionKey.VIEW_SEATS,
    EventPermissionKey.VIEW_TIMELINE,
]

SECURITY_PERMISSIONS: list[EventPermissionKey] = [
    *STAFF_VIEW_PERMISSIONS,
    EventPermissionKey.SCAN_TICKETS,
]

GUEST_PERMISSIONS: list[EventPermissionKey] = [
    EventPermissionKey.VIEW_EVENT,
    EventPermissionKey.VIEW_SELF_TICKET,
    EventPermissionKey.VIEW_SELF_SEAT,
    EventPermissionKey.MANAGE_SELF_PLUS_ONES,
    EventPermissionKey.VIEW_TIMELINE,
]

SUPPORT_PERMISSIONS: list[EventPermissionKey] = [
    EventPermissionKey.VIEW_EVENT,
    EventPermissionKey.VIEW_SUPPORT,
    EventPermissionKey.RESPOND_SUPPORT,
    EventPermissionKey.VIEW_NOTIFICATIONS,
]


def get_default_permissions_for_event_role(role: EventRoleType | str | None) -> list[EventPermissionKey]:
    if role == EventRoleType.ADMIN:
        return list(EVENT_PERMISSION_KEYS)
    if role == EventRoleType.SECURITY:
        return list(SECURITY_PERMISSIONS)
    if role == EventRoleType.GUEST:
        return list(GUEST_PERMISSIONS)
    if role == EventRoleType.SUPPORT:
        return list(SUPPORT_PERMISSIONS)
    return []


def get_default_permissions_for_system_role(role: str) -> list[EventPermissionKey]:
    return get_default_permissions_for_event_role(role)


def unique_event_permissions(permissions: Iterable[str]) -> list[EventPermissionKey]:
    valid = set(EVENT_PERMISSION_KEYS)
    seen: set[str] = set()
    result: list[EventPermissionKey] = []
    for p in permissions:
        if p not in seen and p in valid:
            result.append(EventPermissionKey(p))
            seen.add(p)
    return result


def has_every_event_permission(actual: Iterable[str], required: list[str]) -> bool:
    actual_set = set(actual)
    return all(p in actual_set for p in required)
