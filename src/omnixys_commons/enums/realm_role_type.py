from __future__ import annotations

from collections.abc import Sequence
from enum import StrEnum


class RealmRoleType(StrEnum):
    ADMIN = "ADMIN"
    SUPREME = "SUPREME"
    ELITE = "ELITE"
    BASIC = "BASIC"
    USER = "USER"
    GUEST = "GUEST"


ENUM_TO_KC: dict[RealmRoleType, str] = {
    RealmRoleType.ADMIN: "ADMIN",
    RealmRoleType.SUPREME: "SUPREME",
    RealmRoleType.ELITE: "ELITE",
    RealmRoleType.BASIC: "BASIC",
    RealmRoleType.USER: "USER",
    RealmRoleType.GUEST: "GUEST",
}

_KC_TO_ENUM: dict[str, RealmRoleType] = {}
for _role in RealmRoleType:
    _KC_TO_ENUM[_role.value.upper()] = _role
    _KC_TO_ENUM[_role.value.lower()] = _role
    _KC_TO_ENUM[_role.value] = _role

_ROLE_PRIORITY: list[RealmRoleType] = [
    RealmRoleType.ADMIN,
    RealmRoleType.SUPREME,
    RealmRoleType.ELITE,
    RealmRoleType.BASIC,
    RealmRoleType.USER,
    RealmRoleType.GUEST,
]


def role_str_to_enum(role: str | None) -> RealmRoleType | None:
    if not role:
        return None
    cleaned = role
    for prefix in ("ROLE_", "REALM:", "CLIENT:"):
        if cleaned.upper().startswith(prefix):
            cleaned = cleaned[len(prefix) :]
    if ":" in cleaned:
        cleaned = cleaned.split(":")[-1]
    cleaned = cleaned.strip()
    return _KC_TO_ENUM.get(cleaned)


def to_enum_roles(roles: Sequence[str | None]) -> list[RealmRoleType]:
    seen: set[RealmRoleType] = set()
    result: list[RealmRoleType] = []
    for role in roles:
        enum_role = role_str_to_enum(role)
        if enum_role is not None and enum_role not in seen:
            seen.add(enum_role)
            result.append(enum_role)
    return result


def enum_to_kc_name(role: RealmRoleType) -> str:
    return ENUM_TO_KC[role]


def resolve_effective_role(is_authenticated: bool, roles: list[str] | None = None) -> RealmRoleType:
    if not is_authenticated:
        return RealmRoleType.GUEST
    if roles is None:
        return RealmRoleType.GUEST
    enum_roles = to_enum_roles(roles)
    for candidate in _ROLE_PRIORITY:
        if candidate in enum_roles:
            return candidate
    return RealmRoleType.GUEST
