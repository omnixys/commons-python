from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from commons.enums.event_media_type import EventMediaType
from commons.enums.event_milestone_type import EventMilestoneType
from commons.enums.event_role_type import EventRoleType
from commons.enums.event_visible_tab import EventVisibleTab
from commons.enums.seat_color_group_match import SeatColorGroupMatchType


class SeatColorGroupStyleDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    background: str
    foreground: str
    border: str
    legend_icon: str = Field(alias="legendIcon")


class SeatColorGroupDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    id: str
    name: str
    style: SeatColorGroupStyleDTO
    match_type: SeatColorGroupMatchType = Field(alias="matchType")
    invited_by_values: list[str] = Field(alias="invitedByValues")
    priority: int
    order: int
    is_orphaned: bool = Field(alias="isOrphaned")


class EventCreatedDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    event_id: str = Field(alias="eventId")
    name: str
    ends_at: str = Field(alias="endsAt")
    approval_mode: str = Field(alias="approvalMode")
    max_seats: int = Field(alias="maxSeats")
    require_approval_for_plus_ones: bool = Field(alias="requireApprovalForPlusOnes")
    starts_at: str = Field(alias="startsAt")
    allow_public_rsvp: bool = Field(alias="allowPublicRsvp")
    allow_public_plus_one: bool = Field(alias="allowPublicPlusOne")
    allow_guest_seat_selection: bool = Field(alias="allowGuestSeatSelection")
    schedule_ticket_release: bool = Field(alias="scheduleTicketRelease")
    ticket_release_at: str | None = Field(default=None, alias="ticketReleaseAt")
    rsvp_deadline: str | None = Field(default=None, alias="rsvpDeadline")
    category: str | None = None
    visible_tabs: list[EventVisibleTab] | None = Field(default=None, alias="visibleTabs")
    seat_color_groups: list[SeatColorGroupDTO] | None = Field(default=None, alias="seatColorGroups")
    occurred_at: str = Field(alias="occurredAt")


class EventUpdatedDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    event_id: str = Field(alias="eventId")
    name: str | None = None
    ends_at: str | None = Field(default=None, alias="endsAt")
    approval_mode: str | None = Field(default=None, alias="approvalMode")
    max_seats: int | None = Field(default=None, alias="maxSeats")
    require_approval_for_plus_ones: bool | None = Field(default=None, alias="requireApprovalForPlusOnes")
    starts_at: str | None = Field(default=None, alias="startsAt")
    allow_public_rsvp: bool | None = Field(default=None, alias="allowPublicRsvp")
    allow_public_plus_one: bool | None = Field(default=None, alias="allowPublicPlusOne")
    allow_guest_seat_selection: bool | None = Field(default=None, alias="allowGuestSeatSelection")
    schedule_ticket_release: bool | None = Field(default=None, alias="scheduleTicketRelease")
    ticket_release_at: str | None = Field(default=None, alias="ticketReleaseAt")
    rsvp_deadline: str | None = Field(default=None, alias="rsvpDeadline")
    category: str | None = None
    visible_tabs: list[EventVisibleTab] | None = Field(default=None, alias="visibleTabs")
    seat_color_groups: list[SeatColorGroupDTO] | None = Field(default=None, alias="seatColorGroups")
    occurred_at: str = Field(alias="occurredAt")


class EventMediaUploadedDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    event_id: str = Field(alias="eventId")
    media_id: str = Field(alias="mediaId")
    key: str
    filename: str
    mimetype: str
    size: int | None = None
    type: EventMediaType


class EventMilestoneRecordedDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    event_id: str = Field(alias="eventId")
    milestone_id: str = Field(alias="milestoneId")
    type: EventMilestoneType
    label: str
    occurred_at: str = Field(alias="occurredAt")
    reference_id: str | None = Field(default=None, alias="referenceId")


class EventRoleAssignedDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    event_id: str = Field(alias="eventId")
    user_id: str = Field(alias="userId")
    role: EventRoleType
    assigned_by: str = Field(alias="assignedBy")
    occurred_at: str = Field(alias="occurredAt")


class EventRoleRemovedDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    event_id: str = Field(alias="eventId")
    user_id: str = Field(alias="userId")
    old_role: EventRoleType = Field(alias="oldRole")
    removed_by: str = Field(alias="removedBy")
    occurred_at: str = Field(alias="occurredAt")


class EventRoleDefinitionChangedDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    event_id: str = Field(alias="eventId")
    occurred_at: str = Field(alias="occurredAt")


class EventAccessDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    event_id: str = Field(alias="eventId")
    user_id: str = Field(alias="userId")
    roles: list[str]
    permissions: list[str]
    occurred_at: str = Field(alias="occurredAt")


class EventOwnerChangedDTO(BaseModel):
    model_config = ConfigDict(extra="allow")
    event_id: str = Field(alias="eventId")
    old_owner_id: str = Field(alias="oldOwnerId")
    new_owner_id: str = Field(alias="newOwnerId")
    changed_by: str = Field(alias="changedBy")
    occurred_at: str = Field(alias="occurredAt")
