from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, field_validator

from omnixys_commons.schemas.identity import ActorIdModel, EventIdModel, InvitationIdModel, PhoneNumberSchema


class CreatePendingUserSchema(ActorIdModel, EventIdModel, InvitationIdModel):
    model_config = ConfigDict(extra="forbid")

    email: str | None = None
    seat_id: str | None = Field(default=None, alias="seatId")
    note: str | None = Field(default=None, max_length=2000)
    tenant_id: str | None = Field(default=None, alias="tenantId")
    first_name: str = Field(alias="firstName", min_length=1, max_length=128)
    last_name: str = Field(alias="lastName", min_length=1, max_length=128)
    phone_numbers: list[PhoneNumberSchema] | None = Field(default=None, alias="phoneNumbers")
    locale: str
    plus_ones: list[PlusOneEntry] | None = Field(default=None, alias="plusOnes")
    event_ends_at: str = Field(alias="eventEndsAt")


class PlusOneEntry(BaseModel):
    model_config = ConfigDict(extra="forbid")

    first_name: str = Field(alias="firstName", min_length=1, max_length=128)
    last_name: str = Field(alias="lastName", min_length=1, max_length=128)
    email: str | None = None
    invitation_id: str = Field(alias="invitationId")
    phone_numbers: list[PhoneNumberSchema] | None = Field(default=None, alias="phoneNumbers")

    @field_validator("invitation_id")
    @classmethod
    def must_be_valid_uuid(cls, v: str) -> str:
        from omnixys_commons.schemas.identity import validate_uuid4

        return validate_uuid4(v)


class GuestNotificationSchema(BaseModel):
    model_config = ConfigDict(extra="forbid")

    token: str = Field(min_length=1)
    event_name: str = Field(alias="eventName", min_length=1)
    seat: str | None = None
    seat_id: str | None = Field(default=None, alias="seatId")
    event_ends_at: str = Field(alias="eventEndsAt")


class GuestInviteeEntry(BaseModel):
    model_config = ConfigDict(extra="forbid")

    invitation_id: str = Field(alias="invitationId")
    email: str | None = None
    first_name: str = Field(alias="firstName", min_length=1, max_length=128)
    last_name: str = Field(alias="lastName", min_length=1, max_length=128)

    @field_validator("invitation_id")
    @classmethod
    def must_be_valid_uuid(cls, v: str) -> str:
        from omnixys_commons.schemas.identity import validate_uuid4

        return validate_uuid4(v)


class GuestAuthKeySchema(ActorIdModel):
    model_config = ConfigDict(extra="forbid")

    invitees: list[GuestInviteeEntry]
    event_ends_at: str = Field(alias="eventEndsAt")


class GuestSignUpTokenPayloadSchema(BaseModel):
    model_config = ConfigDict(extra="forbid")

    auth_key: str = Field(alias="authKey", min_length=1)
    user_key: str = Field(alias="userKey", min_length=1)
    event_key: str = Field(alias="eventKey", min_length=1)
    seat_key: str = Field(alias="seatKey", min_length=1)
    timestamp: int | None = None
    event_end_at: str | None = Field(default=None, alias="eventEndAt")


class SignUpTokenPayloadSchema(BaseModel):
    model_config = ConfigDict(extra="forbid")

    auth_key: str = Field(alias="authKey", min_length=1)
    user_key: str = Field(alias="userKey", min_length=1)
    event_key: str = Field(alias="eventKey", min_length=1)
    seat_key: str = Field(alias="seatKey", min_length=1)
    timestamp: int | None = None
    event_end_at: str | None = Field(default=None, alias="eventEndAt")


CreatePendingUserSchema.model_rebuild()
