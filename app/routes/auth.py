from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.database import get_session
from app.models.user import User
from app.schemas.user import UserLogin
from app.security import verify_password

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)

@router.post("/login")
def login(
    user_data: UserLogin,
    session: Session = Depends(get_session),
):
    user = session.exec(
        select(User).where(User.email == user_data.email)
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha inválidos.",
        )

    if not verify_password(
        user_data.password,
        user.password_hash,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha inválidos.",
        )

    return {"message": "Login realizado com sucesso."}