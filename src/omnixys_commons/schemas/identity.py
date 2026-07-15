from __future__ import annotations

import uuid

from pydantic import BaseModel, ConfigDict, Field, field_validator

from omnixys_commons.enums.phone_number_type import PhoneNumberType


def validate_uuid4(value: str) -> str:
    parsed = uuid.UUID(value, version=4)
    return str(parsed)


class IdentitySchema:
    request_id: str = Field(min_length=1, max_length=128)
    correlation_id: str = Field(min_length=1, max_length=128)
    actor_id: str
    tenant_id: str = Field(min_length=1, max_length=128)
    user_id: str
    event_id: str


class PhoneNumberSchema(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: PhoneNumberType
    country_code: str = Field(alias="countryCode", min_length=1, max_length=8)
    number: str = Field(min_length=6, max_length=32)
    label: str | None = Field(default=None, min_length=1, max_length=64)
    is_primary: bool | None = Field(default=None, alias="isPrimary")


class ActorIdModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    actor_id: str = Field(alias="actorId")

    @field_validator("actor_id")
    @classmethod
    def must_be_valid_uuid(cls, v: str) -> str:
        return validate_uuid4(v)


class TenantIdModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    tenant_id: str = Field(alias="tenantId")

    @field_validator("tenant_id")
    @classmethod
    def must_be_valid_tenant_id(cls, v: str) -> str:
        v = v.strip()
        if not v or len(v) > 128:
            raise ValueError("tenantId must be 1-128 characters")
        return v


class UserIdModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    user_id: str = Field(alias="userId")

    @field_validator("user_id")
    @classmethod
    def must_be_valid_uuid(cls, v: str) -> str:
        return validate_uuid4(v)


class EventIdModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    event_id: str = Field(alias="eventId")

    @field_validator("event_id")
    @classmethod
    def must_be_valid_uuid(cls, v: str) -> str:
        return validate_uuid4(v)


class InvitationIdModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    invitation_id: str = Field(alias="invitationId")

    @field_validator("invitation_id")
    @classmethod
    def must_be_valid_uuid(cls, v: str) -> str:
        return validate_uuid4(v)
