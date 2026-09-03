from datetime import datetime

from pydantic import BaseModel


class StudySessionCreate(BaseModel):
    user_id: int
    subject: str
    duration: int


class StudySessionResponse(BaseModel):
    id: int
    user_id: int
    subject: str
    duration: int
    created_at: datetime