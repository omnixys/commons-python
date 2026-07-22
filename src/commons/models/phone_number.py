from __future__ import annotations

from pydantic import BaseModel, ConfigDict

from commons.enums.phone_number_type import PhoneNumberType


class PhoneNumber(BaseModel):
    model_config = ConfigDict(extra="allow")

    type: PhoneNumberType
    country_code: str
    number: str
    label: str | None = None
    is_primary: bool = False
