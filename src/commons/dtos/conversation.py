from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from commons.enums.conversation_channel import ConversationChannel
from commons.enums.conversation_priority import ConversationPriority


class ConversationCreatedDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    conversation_id: str = Field(alias="conversationId")
    event_id: str = Field(alias="eventId")
    invitation_id: str | None = Field(default=None, alias="invitationId")
    guest_user_id: str | None = Field(default=None, alias="guestUserId")
    guest_name: str = Field(alias="guestName")
    channel: ConversationChannel
    first_message: str = Field(alias="firstMessage")


class AgentRepliedDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    conversation_id: str = Field(alias="conversationId")
    message_id: str = Field(alias="messageId")
    channel: ConversationChannel
    body: str
    assigned_to: str = Field(alias="assignedTo")


class GuestRepliedDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    conversation_id: str = Field(alias="conversationId")
    message_id: str = Field(alias="messageId")
    channel: ConversationChannel
    body: str


class ConversationChatAssignedDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    conversation_id: str = Field(alias="conversationId")
    assigned_to: str = Field(alias="assignedTo")
    assigned_by: str = Field(alias="assignedBy")


class ConversationChatClosedDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    conversation_id: str = Field(alias="conversationId")
    closed_by: str = Field(alias="closedBy")


class ConversationChannelMessageDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    conversation_id: str = Field(alias="conversationId")
    channel: ConversationChannel
    to: str
    body: str
    external_id: str | None = Field(default=None, alias="externalId")


class SupportMessageReceivedDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    id: str
    conversation_id: str = Field(alias="conversationId")
    direction: str
    channel: str
    from_user_id: str | None = Field(default=None, alias="fromUserId")
    from_guest: bool = Field(alias="fromGuest")
    body: str | None = None
    media_url: str | None = Field(default=None, alias="mediaUrl")
    mime_type: str | None = Field(default=None, alias="mimeType")
    status: str
    created_at: str = Field(alias="createdAt")


class ConversationMappingDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    id: str
    channel: ConversationChannel
    external_id: str = Field(alias="externalId")
    event_id: str | None = Field(default=None, alias="eventId")
    conversation_id: str | None = Field(default=None, alias="conversationId")
    mapping_type: str = Field(alias="mappingType")
    metadata: dict[str, object] | None = None


class CreateConversationMappingDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    channel: ConversationChannel
    external_id: str = Field(alias="externalId")
    event_id: str = Field(alias="eventId")
    conversation_id: str = Field(alias="conversationId")
    mapping_type: str | None = Field(default=None, alias="mappingType")


class InternalConversationCreatedDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    conversation_id: str = Field(alias="conversationId")
    event_id: str = Field(alias="eventId")
    title: str
    type: str
    role_id: str | None = Field(default=None, alias="roleId")
    created_by: str = Field(alias="createdBy")


class InternalMessageSentDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    id: str
    conversation_id: str = Field(alias="conversationId")
    sender_id: str = Field(alias="senderId")
    body: str
    priority: ConversationPriority
    created_at: str = Field(alias="createdAt")
    participant_ids: list[str] | None = Field(default=None, alias="participantIds")


class InternalReadReceiptDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    conversation_id: str = Field(alias="conversationId")
    user_id: str = Field(alias="userId")
    last_read_at: str = Field(alias="lastReadAt")


class EmailAttachment(BaseModel):
    model_config = ConfigDict(extra="allow")
    filename: str
    content_type: str = Field(alias="contentType")
    size: int
    content: str


class EmailReceivedDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    message_id: str = Field(alias="messageId")
    from_address: str = Field(alias="from")
    to: list[str]
    cc: list[str] | None = None
    subject: str
    body: str
    html_body: str | None = Field(default=None, alias="htmlBody")
    in_reply_to: str | None = Field(default=None, alias="inReplyTo")
    references: str | None = None
    attachments: list[EmailAttachment] | None = None
    received_at: str = Field(alias="receivedAt")


class EmailOutboundDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    to: str
    subject: str
    body: str
    html_body: str | None = Field(default=None, alias="htmlBody")
    in_reply_to: str | None = Field(default=None, alias="inReplyTo")
    references: str | None = None
    message_id: str | None = Field(default=None, alias="messageId")
    conversation_id: str | None = Field(default=None, alias="conversationId")


class DeliveryStatusDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    message_id: str = Field(alias="messageId")
    provider_message_id: str | None = Field(default=None, alias="providerMessageId")
    conversation_id: str = Field(alias="conversationId")
    channel: str
    status: str
    error: str | None = None
    timestamp: str


class EscalationDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    conversation_id: str = Field(alias="conversationId")
    escalated_to: str = Field(alias="escalatedTo")
    escalated_by: str = Field(alias="escalatedBy")
    reason: str | None = None
    escalated_at: str = Field(alias="escalatedAt")
