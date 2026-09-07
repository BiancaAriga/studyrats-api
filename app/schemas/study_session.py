from datetime import datetime

from pydantic import BaseModel, Field


class StudySessionCreate(BaseModel):
    user_id: int
    subject: str = Field(min_length=1, max_length=100)
    duration: int = Field(gt=0, le=1440)

class StudySessionUpdate(BaseModel):
    subject: str | None = Field(default=None, min_length=1, max_length=100)
    duration: int | None = Field(default=None, gt=0, le=1440)

class StudySessionResponse(BaseModel):
    id: int
    user_id: int
    subject: str
    duration: int
    created_at: datetime