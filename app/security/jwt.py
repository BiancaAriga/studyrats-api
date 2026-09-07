import jwt

SECRET_KEY = "chave-secreta"
ALGORITHM = "HS256"

def create_access_token(data: dict) -> str:
    return jwt.encode(
        data,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )