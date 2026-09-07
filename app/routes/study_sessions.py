from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.database import get_session
from app.models.study_session import StudySession
from app.models.user import User
from app.schemas.study_session import (
    StudySessionCreate,
    StudySessionResponse,
    StudySessionUpdate,
)

router = APIRouter(
    prefix="/study-sessions",
    tags=["Study Sessions"],
)


@router.post(
    "/",
    response_model=StudySessionResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Criar sessão de estudo",
    description="Cria uma nova sessão de estudo para um usuário.",
)
def create_study_session(
    session_data: StudySessionCreate,
    session: Session = Depends(get_session),
):
    user = session.get(User, session_data.user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado.",
        )

    study_session = StudySession(
        user_id=session_data.user_id,
        subject=session_data.subject,
        duration=session_data.duration,
    )

    session.add(study_session)
    session.commit()
    session.refresh(study_session)

    return study_session

@router.get(
    "/",
    response_model=list[StudySessionResponse],
    summary="Listar sessões de estudo",
    description="Retorna todas as sessões de estudo.",
)
def get_study_sessions(
    session: Session = Depends(get_session),
):
    study_sessions = session.exec(
        select(StudySession)
    ).all()

    return study_sessions

@router.get(
    "/{session_id}",
    response_model=StudySessionResponse,
    summary="Buscar sessão de estudo",
    description="Retorna uma sessão de estudo pelo ID.",
)
def get_study_session(
    session_id: int,
    session: Session = Depends(get_session),
):
    study_session = session.get(StudySession, session_id)

    if not study_session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sessão de estudo não encontrada.",
        )

    return study_session

@router.patch(
    "/{session_id}",
    response_model=StudySessionResponse,
    summary="Atualizar sessão de estudo",
    description="Atualiza parcialmente uma sessão de estudo.",
)
def update_study_session(
    session_id: int,
    session_data: StudySessionUpdate,
    session: Session = Depends(get_session),
):
    study_session = session.get(StudySession, session_id)

    if not study_session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sessão de estudo não encontrada.",
        )

    if session_data.subject is not None:
        study_session.subject = session_data.subject

    if session_data.duration is not None:
        study_session.duration = session_data.duration

    session.add(study_session)
    session.commit()
    session.refresh(study_session)

    return study_session
    
@router.delete(
    "/{session_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Excluir sessão de estudo",
    description="Exclui uma sessão de estudo pelo ID.",
)
def delete_study_session(
    session_id: int,
    session: Session = Depends(get_session),
):
    study_session = session.get(StudySession, session_id)

    if not study_session:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sessão de estudo não encontrada.",
        )

    session.delete(study_session)
    session.commit()