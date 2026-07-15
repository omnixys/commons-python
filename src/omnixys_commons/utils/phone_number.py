from __future__ import annotations

from omnixys_commons.dtos.phone_number import PhoneNumberDTO


def get_primary_phone_number(phone_numbers: list[PhoneNumberDTO] | None) -> str | None:
    if not phone_numbers:
        return None
    primary = next((p for p in phone_numbers if p.is_primary is True), None)
    selected = primary or phone_numbers[0]
    if not selected.country_code or not selected.number:
        return None
    return f"{selected.country_code}{selected.number}"
