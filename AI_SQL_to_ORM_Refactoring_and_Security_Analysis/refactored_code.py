import os

from sqlalchemy import String, create_engine, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column


# MySQL URL: mysql+mysqlconnector://user:password@localhost/example_db
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///:memory:")

engine = create_engine(DATABASE_URL)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(120), nullable=False
    )


def create_user(session: Session, username: str, email: str) -> None:
    if not username or not email:
        print("Username and email are required.")
        return

    try:
        session.add(User(username=username, email=email))
        session.commit()
        print(f"User '{username}' created successfully.")
    except SQLAlchemyError:
        session.rollback()
        print("Error creating user.")


def get_user_by_username(session: Session, username: str):
    if not username:
        print("Username is required.")
        return None

    try:
        return session.scalars(
            select(User).where(User.username == username)
        ).first()
    except SQLAlchemyError:
        session.rollback()
        print("Error fetching user.")
        return None


def update_user_email(
    session: Session, username: str, new_email: str
) -> None:
    if not username or not new_email:
        print("Username and email are required.")
        return

    try:
        user = session.scalars(
            select(User).where(User.username == username)
        ).first()

        if user is None:
            print(f"User '{username}' not found.")
            return

        user.email = new_email
        session.commit()
        print(f"Email updated for '{username}'.")
    except SQLAlchemyError:
        session.rollback()
        print("Error updating user.")


def delete_user(session: Session, username: str) -> None:
    if not username:
        print("Username is required.")
        return

    try:
        user = session.scalars(
            select(User).where(User.username == username)
        ).first()

        if user is None:
            print(f"User '{username}' not found.")
            return

        session.delete(user)
        session.commit()
        print(f"User '{username}' deleted.")
    except SQLAlchemyError:
        session.rollback()
        print("Error deleting user.")


def list_users(session: Session) -> list[User]:
    try:
        return list(
            session.scalars(select(User).order_by(User.id)).all()
        )
    except SQLAlchemyError:
        session.rollback()
        print("Error listing users.")
        return []


if __name__ == "__main__":
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        create_user(session, "kai_example", "kai@example.com")

        user = get_user_by_username(session, "kai_example")
        if user is not None:
            print(f"Found: {user.id}, {user.username}, {user.email}")

        update_user_email(
            session, "kai_example", "kai.updated@example.com"
        )

        for user in list_users(session):
            print(f"{user.id}: {user.username} — {user.email}")

        delete_user(session, "kai_example")

    engine.dispose()
