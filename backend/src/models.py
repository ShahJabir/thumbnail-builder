"""Pydantic and SQL model for the application"""

from datetime import datetime, timezone
from typing import Optional, List
from uuid import uuid4
from sqlmodel import Field, SQLModel, Relationship


def _uuid() -> str:
    """Generate a UUIDv4 in string format"""
    return str(uuid4())


def _now() -> datetime:
    """Generate the current UTC timestamp"""
    return datetime.now(timezone.utc)


class Thumbnail(SQLModel, table=True):
    """Model for representing a thumbnail in the database"""

    id: Optional[str] = Field(default_factory=_uuid, primary_key=True)
    job_id: str = Field(default_factory="job.id")
    style_name: str = Field(default="")
    status: str = Field(default="pending")
    error_message: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=_now)

    job: Optional["Job"] = Relationship(back_populates="thumbnails")


class Job(SQLModel, table=True):
    """Model for representing a job in the database"""

    id: str = Field(default_factory=_uuid, primary_key=True)
    prompt: str = Field(default="")
    num_thumbnails: int = Field(default=1, ge=1, le=3)
    headshot_url: str = Field(default="")
    status: str = Field(default="pending")
    created_at: datetime = Field(default_factory=_now)

    thumbnails: List["Thumbnail"] = Relationship(back_populates="job")
