from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, field_validator


class TaskStatus(str, Enum):
    PENDING = "Pending"
    COMPLETED = "Completed"


class Task(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str = Field(..., min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)
    status: TaskStatus = Field(default=TaskStatus.PENDING)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator("title")
    @classmethod
    def title_must_not_be_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Title cannot be empty or whitespace only")
        return v
