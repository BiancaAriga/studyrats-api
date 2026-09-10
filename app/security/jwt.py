import jwt

from app.config.settings import settings

def create_access_token(data: dict) -> str:
    return jwt.encode(
        data,
        settings.secret_key,
        algorithm=settings.algorithm,
    )

def decode_access_token(token: str) -> dict:
    return jwt.decode(
        token,
        settings.secret_key,
        algorithms=[settings.algorithm],
    )