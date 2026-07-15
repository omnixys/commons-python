from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class UserIdDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    user_id: str = Field(alias="userId")


class ActorIdDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    actor_id: str = Field(alias="actorId")


class TokenDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    token: str


class EventIdDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    event_id: str = Field(alias="eventId")


class EventIdsDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    event_ids: list[str] = Field(alias="eventIds")


class UserIdListDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    user_ids: list[str] = Field(alias="userIds")


class UserActionDTO(UserIdDTO, ActorIdDTO):
    pass


class UserTokenDTO(UserIdDTO, TokenDTO):
    pass
