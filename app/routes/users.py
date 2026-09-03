from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.database import get_session
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.security import hash_password
from sqlmodel import select
from fastapi import Depends, HTTPException, status

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "/", 
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Criar usuário",
    description="Cria um novo usuário no StudyRats."
)
def create_user(
    user_data: UserCreate,
    session: Session = Depends(get_session),
):

    existing_user = session.exec(
        select(User).where(User.email == user_data.email)
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email já cadastrado.",
        )

    user = User(
        name=user_data.name,
        email=user_data.email,
        password_hash=hash_password(user_data.password),
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    return user