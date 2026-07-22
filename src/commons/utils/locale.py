from __future__ import annotations

from typing import Literal

Locale = Literal["de-DE", "en-US"]

LANGUAGE_TO_LOCALE: dict[str, Locale] = {
    "ENGLISH": "en-US",
    "GERMAN": "de-DE",
}


def map_language_to_locale(language: str | None) -> Locale:
    if language is None:
        return "en-US"
    return LANGUAGE_TO_LOCALE.get(language, "en-US")
