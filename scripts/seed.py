from sqlmodel import Session, select

from app.database import engine
from app.models.study_session import StudySession
from app.models.user import User
from app.security.password import hash_password


def seed_database():
    with Session(engine) as session:
        # Não popula novamente um banco que já possui usuários.
        existing_user = session.exec(select(User)).first()

        if existing_user:
            print("Banco já possui dados. Seed não executado.")
            return

        users_data = [
            {
                "name": "Bianca",
                "email": "bianca@studyrats.com",
                "password": "12345678",
            },
            {
                "name": "Ana",
                "email": "ana@studyrats.com",
                "password": "12345678",
            },
            {
                "name": "Carlos",
                "email": "carlos@studyrats.com",
                "password": "12345678",
            },
            {
                "name": "Marina",
                "email": "marina@studyrats.com",
                "password": "12345678",
            },
            {
                "name": "Lucas",
                "email": "lucas@studyrats.com",
                "password": "12345678",
            },
        ]

        users = []

        for user_data in users_data:
            user = User(
                name=user_data["name"],
                email=user_data["email"],
                password_hash=hash_password(user_data["password"]),
            )

            session.add(user)
            users.append(user)

        session.commit()

        for user in users:
            session.refresh(user)

        sessions_data = [
            # Bianca — 270 minutos
            (users[0], "Python", 120),
            (users[0], "Angular", 90),
            (users[0], "Banco de Dados", 60),

            # Ana — 390 minutos
            (users[1], "Java", 180),
            (users[1], "Angular", 120),
            (users[1], "Docker", 90),

            # Carlos — 210 minutos
            (users[2], "Python", 150),
            (users[2], "FastAPI", 60),

            # Marina — 165 minutos
            (users[3], "TypeScript", 120),
            (users[3], "Git", 45),

            # Lucas — 150 minutos
            (users[4], "Docker", 90),
            (users[4], "SQL", 60),
        ]

        for user, subject, duration in sessions_data:
            study_session = StudySession(
                user_id=user.id,
                subject=subject,
                duration=duration,
            )

            session.add(study_session)

        session.commit()

        print("Banco populado com sucesso!")


if __name__ == "__main__":
    seed_database()