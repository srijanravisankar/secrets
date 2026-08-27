from typing import Annotated

from database import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.users import TokenResponse, UserCreateRequest
from security.tokens import create_access_token
from services.exceptions import UsernameTakenError
from services.users import authenticate_user, create_user
from sqlalchemy.orm import Session

router = APIRouter(prefix="/auth")

DbSession = Annotated[Session, Depends(get_db)]


@router.post(
    "/signup", status_code=status.HTTP_201_CREATED, response_model=TokenResponse
)
def signup(db: DbSession, user: UserCreateRequest) -> TokenResponse:
    try:
        new_user = create_user(db, user)
    except UsernameTakenError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already taken",
        )

    access_token = create_access_token(new_user.username)

    return TokenResponse(access_token=access_token)


@router.post("/login", response_model=TokenResponse)
def login(db: DbSession, user: UserCreateRequest) -> TokenResponse:
    user_result = authenticate_user(db, user)

    if user_result is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    access_token = create_access_token(user_result.username)

    return TokenResponse(access_token=access_token)
