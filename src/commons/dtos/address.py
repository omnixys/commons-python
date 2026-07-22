from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class CreateUserAddressDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    user_id: str = Field(alias="userId")
    token: str


class CreateEventAddressDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    event_id: str = Field(alias="eventId")
    street: str | None = None
    house_number: str | None = None
    postal_code: str | None = None
    city: str
    state: str | None = None
    country: str
    additional_info: str | None = None
