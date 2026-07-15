from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from omnixys_commons.dtos.phone_number import PhoneNumberDTO


class CreateGuestDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    user_id: str = Field(alias="userId")
    token: str
    username: str
    email: str
    invitation_id: str = Field(alias="invitationId")


class PublicPlusOneDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    email: str | None = None
    plus_one_age_category: str | None = Field(default=None, alias="plusOneAgeCategory")


class PublicPlusOneWithIdDTO(PublicPlusOneDTO):
    model_config = ConfigDict(extra="allow")
    invitation_id: str = Field(alias="invitationId")
    phone_numbers: list[PhoneNumberDTO] | None = Field(default=None, alias="phoneNumbers")


class CreatePendingUserDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    actor_id: str = Field(alias="actorId")
    email: str | None = None
    event_id: str = Field(alias="eventId")
    invitation_id: str = Field(alias="invitationId")
    seat_id: str | None = Field(default=None, alias="seatId")
    note: str | None = None
    tenant_id: str | None = Field(default=None, alias="tenantId")
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    phone_numbers: list[PhoneNumberDTO] | None = Field(default=None, alias="phoneNumbers")
    plus_one_age_category: str | None = Field(default=None, alias="plusOneAgeCategory")
    locale: str
    plus_ones: list[PublicPlusOneWithIdDTO] | None = None
    selected_invited_by: list[str] | None = Field(default=None, alias="selectedInvitedBy")
    guest_note: str | None = Field(default=None, alias="guestNote")
    event_ends_at: str = Field(alias="eventEndsAt")


class GuestInvitee(BaseModel):
    model_config = ConfigDict(extra="allow")
    invitation_id: str = Field(alias="invitationId")
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    email: str | None = None
    phone_numbers: list[PhoneNumberDTO] | None = Field(default=None, alias="phoneNumbers")
    is_primary: bool = Field(alias="isPrimary")
    plus_one_age_category: str | None = Field(default=None, alias="plusOneAgeCategory")


class GuestUserKey(BaseModel):
    model_config = ConfigDict(extra="allow")
    actor_id: str = Field(alias="actorId")
    users: list[GuestInvitee]
