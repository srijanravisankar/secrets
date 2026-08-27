from models.users import User
from schemas.users import UserCreateRequest
from security.passwords import hash_password, verify_password
from services.exceptions import UsernameTakenError
from sqlalchemy import select
from sqlalchemy.orm import Session


def create_user(db: Session, user: UserCreateRequest) -> User:
    statement = select(User).where(User.username == user.username).exists()
    username_exists = db.scalar(select(statement))

    if username_exists:
        raise UsernameTakenError

    new_user = User(username=user.username, password_hash=hash_password(user.password))

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def authenticate_user(db: Session, user: UserCreateRequest) -> User | None:
    statement = select(User).where(User.username == user.username)
    user_in_db = db.scalar(statement)

    if user_in_db is None:
        return None

    verification = verify_password(user.password, user_in_db.password_hash)
    if not verification:
        return None

    return user_in_db
