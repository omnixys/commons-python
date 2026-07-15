from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class AddGuestIdToInvitationDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    user_id: str = Field(alias="userId")
    actor_id: str = Field(alias="actorId")
    invitation_id: str = Field(alias="invitationId")


class CreateUserWithInvitationIdDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    user_id: str = Field(alias="userId")
    token: str
    invitation_id: str = Field(alias="invitationId")


class InvitationSeatingInfoUpdatedDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    event_id: str = Field(alias="eventId")
    invitation_id: str = Field(alias="invitationId")
    guest_id: str = Field(alias="guestId")
    selected_invited_by: list[str] = Field(alias="selectedInvitedBy")
