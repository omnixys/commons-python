from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class CreateSeatDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    actor_id: str = Field(alias="actorId")
    event_id: str = Field(alias="eventId")
    max_seats: int = Field(alias="maxSeats")


class SeatAssignment(BaseModel):
    model_config = ConfigDict(extra="allow")
    invitation_id: str = Field(alias="invitationId")
    seat_id: str | None = Field(default=None, alias="seatId")
    note: str | None = None


class AddGuestToSeatDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    actor_id: str = Field(alias="actorId")
    event_id: str = Field(alias="eventId")
    user_id: str = Field(alias="userId")
    seat_id: str = Field(alias="seatId")
    note: str | None = None


class GuestSeatKey(BaseModel):
    model_config = ConfigDict(extra="allow")
    actor_id: str = Field(alias="actorId")
    event_id: str = Field(alias="eventId")
    assignments: list[SeatAssignment]
