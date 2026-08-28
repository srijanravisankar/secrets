from typing import Annotated

from database import get_db
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import InvalidTokenError
from models import User
from security.tokens import decode_access_token
from services.users import get_user_by_username
from sqlalchemy.orm import Session

bearer_scheme = HTTPBearer()

DbSession = Annotated[Session, Depends(get_db)]
AuthCredentials = Annotated[HTTPAuthorizationCredentials, Depends(bearer_scheme)]


def get_current_user(db: DbSession, credentials: AuthCredentials) -> User:
    try:
        decoded_token = decode_access_token(credentials.credentials)
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    user = get_user_by_username(db, decoded_token)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    return user


CurrentUser = Annotated[User, Depends(get_current_user)]
