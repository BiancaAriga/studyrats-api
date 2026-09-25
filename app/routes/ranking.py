from fastapi import APIRouter, Depends
from sqlmodel import Session, func, select

from app.database import get_session
from app.models.study_session import StudySession
from app.models.user import User
from app.schemas.ranking import RankingResponse

router = APIRouter(
    prefix="/ranking",
    tags=["Ranking"],
)


@router.get("/", response_model=list[RankingResponse])
def get_ranking(
    session: Session = Depends(get_session),
):
    statement = (
        select(
            User.id,
            User.name,
            func.sum(StudySession.duration),
        )
        .join(
            StudySession,
            StudySession.user_id == User.id,
        )
        .group_by(User.id, User.name)
        .order_by(
            func.sum(StudySession.duration).desc()
        )
    )

    results = session.exec(statement).all()

    return [
        RankingResponse(
            user_id=user_id,
            user_name=user_name,
            total_duration=total_duration,
        )
        for user_id, user_name, total_duration in results
    ]