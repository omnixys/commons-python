from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class TemporalRange:
    start: str
    end: str | None = None

    def contains(self, timestamp: str) -> bool:
        if self.end is None:
            return timestamp >= self.start
        return self.start <= timestamp <= self.end
