from __future__ import annotations

from pydantic import BaseModel


class PaginationQuerySchema(BaseModel):
    page: int = 0
    size: int = 20


class PaginationResponseSchema(BaseModel):
    page: int = 0
    size: int = 20
    total: int = 0
    total_pages: int = 0

    @property
    def has_next(self) -> bool:
        return self.page + 1 < self.total_pages

    @property
    def has_previous(self) -> bool:
        return self.page > 0
