from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class GeoLocation(BaseModel):
    model_config = ConfigDict(extra="allow")

    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
