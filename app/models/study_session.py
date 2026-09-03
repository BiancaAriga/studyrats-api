from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel


class StudySession(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    subject: str
    duration: int
    created_at: datetime = Field(default_factory=datetime.utcnow)

    user: "User" = Relationship(
        back_populates="study_sessions"
    )