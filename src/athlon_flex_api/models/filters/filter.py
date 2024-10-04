from __future__ import annotations

from pydantic import BaseModel


class Filter(BaseModel):
    """Base class for filters."""

    def to_request_params(self) -> dict:
        """Return the filter as request parameters, to be provied to api request"""
        return {
            f"Filters.{key}": value
            for key, value in self.model_dump(exclude_none=True).items()
        }


class EmptyFilter(Filter):
    """Empty filter for loading all items."""

    pass
