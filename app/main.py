from fastapi import FastAPI
from app.database import create_db_and_tables

from app.models import User, StudySession
from app.routes.users import router as users_router
from app.routes.auth import router as auth_router
from app.routes.study_sessions import router as study_sessions_router

app = FastAPI(
    title="StudyRats API",
    description="API para gerenciamento de estudos do StudyRats",
    version="1.0.0",
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(users_router)
app.include_router(auth_router)
app.include_router(study_sessions_router)