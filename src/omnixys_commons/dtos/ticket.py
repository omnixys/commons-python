from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class TicketAssignment(BaseModel):
    model_config = ConfigDict(extra="allow")
    invitation_id: str = Field(alias="invitationId")
    seat_id: str = Field(alias="seatId")


class GuestTicketKey(BaseModel):
    model_config = ConfigDict(extra="allow")
    actor_id: str = Field(alias="actorId")
    event_id: str = Field(alias="eventId")
    tickets: list[TicketAssignment]
