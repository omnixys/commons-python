from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class SendAuthLinkDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    username: str
    token: str
    email: str
    locale: str
    device: str
    ip: str
    location: str


class SecurityQuestionAnswer(BaseModel):
    model_config = ConfigDict(extra="allow")
    question_id: str = Field(alias="questionId")
    answer: str


class CredentialsDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    user_id: str = Field(alias="userId")
    username: str
    password: str
    invitation_id: str = Field(alias="invitationId")
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")


class KCSignUpDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    id: str
    username: str
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    email: str
    password: str
    security_questions: list[SecurityQuestionAnswer] | None = Field(default=None, alias="securityQuestions")


class InviteeInfo(BaseModel):
    model_config = ConfigDict(extra="allow")
    invitation_id: str = Field(alias="invitationId")
    email: str | None = None
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")


class GuestAuthKey(BaseModel):
    model_config = ConfigDict(extra="allow")
    actor_id: str = Field(alias="actorId")
    invitees: list[InviteeInfo]
    event_ends_at: str = Field(alias="eventEndsAt")
