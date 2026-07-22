from __future__ import annotations

from typing import ClassVar

from pydantic import BaseModel, ConfigDict


class OmnixysLocale(BaseModel):
    model_config = ConfigDict(extra="allow")

    language: str
    country: str | None = None

    GERMANY: ClassVar[OmnixysLocale]
    US: ClassVar[OmnixysLocale]

    @staticmethod
    def from_string(value: str) -> OmnixysLocale:
        parts = value.split("-", 1)
        return OmnixysLocale(language=parts[0], country=parts[1] if len(parts) > 1 else None)

    def __str__(self) -> str:
        if self.country:
            return f"{self.language}-{self.country}"
        return self.language


OmnixysLocale.GERMANY = OmnixysLocale(language="de", country="DE")
OmnixysLocale.US = OmnixysLocale(language="en", country="US")
