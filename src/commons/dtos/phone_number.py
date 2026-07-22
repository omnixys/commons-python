from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from commons.enums.phone_number_type import PhoneNumberType


class PhoneNumberDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    type: PhoneNumberType
    country_code: str = Field(alias="countryCode")
    number: str
    label: str | None = None
    is_primary: bool | None = Field(default=None, alias="isPrimary")


class AddPhoneNumberDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    user_id: str = Field(alias="userId")
    number: str
    type: PhoneNumberType


class RemovePhoneNumberDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    user_id: str = Field(alias="userId")
    phone_number_id: str = Field(alias="phoneNumberId")
