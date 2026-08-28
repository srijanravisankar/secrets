from dependencies import CurrentUser
from fastapi import APIRouter
from models.users import User
from schemas.users import UserResponse

router = APIRouter(prefix="/users")


@router.get("/me", response_model=UserResponse)
def get_me(user: CurrentUser) -> User:
    return user
