from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class UserCredentialsDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    user_id: str = Field(alias="userId")
    username: str
    email: str
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    invitation_id: str | None = Field(default=None, alias="invitationId")


class GuestNotificationDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    token: str
    event_name: str = Field(alias="eventName")
    seat: str | None = None
    seat_id: str | None = Field(default=None, alias="seatId")
    event_ends_at: str = Field(alias="eventEndsAt")


class WhatsAppMessageValue(BaseModel):
    model_config = ConfigDict(extra="allow")
    id: str
    chat_id: str = Field(alias="chatId")
    direction: str
    from_address: str = Field(alias="from")
    to: str
    body: str | None = None
    created_at: str = Field(alias="createdAt")


class WhatsAppMessageDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    key: str
    value: WhatsAppMessageValue


class WhatsappOutgoingValueDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    message_id: str = Field(alias="messageId")
    to: str
    message: str
    retry_count: int | None = Field(default=None, alias="retryCount")
    created_at: str | None = Field(default=None, alias="createdAt")


class WhatsappOutgoingDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    key: str
    value: WhatsappOutgoingValueDTO


class WhatsAppDLQValueDTO(WhatsappOutgoingValueDTO):
    model_config = ConfigDict(extra="allow")
    error: str
    failed_at: str = Field(alias="failedAt")


class WhatsAppDLQDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    key: str
    value: WhatsAppDLQValueDTO
