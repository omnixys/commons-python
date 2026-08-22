"""Behavioral tests for commons utilities."""

from __future__ import annotations

from commons.dtos.phone_number import PhoneNumberDTO
from commons.enums.event_permission_key import EventPermissionKey
from commons.enums.phone_number_type import PhoneNumberType
from commons.utils import (
    EventSystemRoleKey,
    Locale,
    create_tmp_username,
    get_default_permissions_for_event_role,
    get_primary_phone_number,
    has_every_event_permission,
    map_language_to_locale,
    n2u,
    unique_event_permissions,
)
from commons.utils.null_to_undefined import SENTINEL, null_to_undefined, undefined_to_null


def test_map_language_to_locale() -> None:
    assert map_language_to_locale("GERMAN") == "de-DE"
    assert map_language_to_locale("ENGLISH") == "en-US"
    assert map_language_to_locale(None) == "en-US"
    assert map_language_to_locale("UNKNOWN") == "en-US"
    assert isinstance(map_language_to_locale("GERMAN"), str)


def test_locale_is_literal_of_supported_values() -> None:
    locale: Locale = "de-DE"
    assert locale in ("de-DE", "en-US")


def test_n2u_passthrough() -> None:
    assert n2u(None) is None
    assert n2u("value") == "value"


def test_null_to_undefined_roundtrip() -> None:
    data = {"a": None, "b": 1, "c": None}
    converted = null_to_undefined(data)
    assert converted == {"a": SENTINEL, "b": 1, "c": SENTINEL}
    assert undefined_to_null(converted) == data


def test_null_to_undefined_handles_none() -> None:
    assert null_to_undefined(None) is None


def test_create_tmp_username() -> None:
    assert create_tmp_username("Doe", "John") == "john.doe"
    assert create_tmp_username("", "John") == "john."


def test_get_primary_phone_number() -> None:
    numbers = [
        PhoneNumberDTO(
            type=PhoneNumberType.MOBILE,
            countryCode="+49",
            number="1701234567",
            isPrimary=False,
        ),
        PhoneNumberDTO(
            type=PhoneNumberType.HOME,
            countryCode="+49",
            number="3012345678",
            isPrimary=True,
        ),
    ]
    assert get_primary_phone_number(numbers) == "+493012345678"


def test_get_primary_phone_number_empty() -> None:
    assert get_primary_phone_number(None) is None
    assert get_primary_phone_number([]) is None


def test_get_primary_phone_number_missing_number() -> None:
    numbers = [PhoneNumberDTO(type=PhoneNumberType.MOBILE, countryCode="+49", number="")]
    assert get_primary_phone_number(numbers) is None


def test_default_permissions_for_admin_include_all() -> None:
    perms = get_default_permissions_for_event_role("ADMIN")
    assert len(perms) == len(EventPermissionKey)
    assert EventPermissionKey.VIEW_EVENT in perms


def test_default_permissions_for_guest() -> None:
    perms = get_default_permissions_for_event_role("GUEST")
    assert EventPermissionKey.VIEW_SELF_TICKET in perms
    assert EventPermissionKey.MANAGE_TICKETS not in perms


def test_default_permissions_unknown_role() -> None:
    assert get_default_permissions_for_event_role(None) == []


def test_event_system_role_key() -> None:
    assert EventSystemRoleKey.ADMIN == "ADMIN"
    assert EventSystemRoleKey.GUEST == "GUEST"


def test_unique_event_permissions() -> None:
    result = unique_event_permissions(["event.view", "event.view", "unknown.permission"])
    assert result == [EventPermissionKey.VIEW_EVENT]


def test_has_every_event_permission() -> None:
    actual = ["event.view", "seats.view"]
    assert has_every_event_permission(actual, ["event.view"]) is True
    assert has_every_event_permission(actual, ["event.view", "seats.manage"]) is False
