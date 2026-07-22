from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class Address(BaseModel):
    model_config = ConfigDict(extra="allow")

    street: str | None = None
    house_number: str | None = None
    postal_code: str | None = None
    city: str
    state: str | None = None
    country: str
    additional_info: str | None = None


class EventAddress(BaseModel):
    model_config = ConfigDict(extra="allow")

    street: str | None = None
    house_number: str | None = None
    postal_code: str | None = None
    city: str
    state: str | None = None
    country: str
    additional_info: str | None = None
