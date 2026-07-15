from __future__ import annotations

from enum import StrEnum


class RealmRoleType(StrEnum):
    ADMIN = "ADMIN"
    SUPREME = "SUPREME"
    ELITE = "ELITE"
    BASIC = "BASIC"
    USER = "USER"
    GUEST = "GUEST"


_PRIORITY: dict[RealmRoleType, int] = {
    RealmRoleType.ADMIN: 1,
    RealmRoleType.SUPREME: 2,
    RealmRoleType.ELITE: 3,
    RealmRoleType.BASIC: 4,
    RealmRoleType.USER: 5,
    RealmRoleType.GUEST: 6,
}


def resolve_effective_role(is_authenticated: bool, raw: list[str | None] | None = None) -> RealmRoleType | None:
    if not is_authenticated:
        return RealmRoleType.GUEST
    roles = to_enum_roles(raw)
    if not roles:
        return None
    return min(roles, key=lambda r: _PRIORITY.get(r, 99))


def to_enum_roles(raw: list[str | None] | None) -> list[RealmRoleType]:
    if raw is None:
        return []
    result: list[RealmRoleType] = []
    seen: set[RealmRoleType] = set()
    for s in raw:
        if s is None:
            continue
        role = role_str_to_enum(s)
        if role is not None and role not in seen:
            seen.add(role)
            result.append(role)
    return result


def role_str_to_enum(s: str | None) -> RealmRoleType | None:
    if s is None:
        return None
    cleaned = s.strip().removeprefix("ROLE_").removeprefix("REALM_").removeprefix("CLIENT_")
    for part in cleaned.split(":"):
        try:
            return RealmRoleType(part.upper())
        except ValueError:
            continue
    return None


def enum_to_kc_name(role: RealmRoleType) -> str:
    return role.value
