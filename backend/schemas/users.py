from pydantic import Field
from schemas.base import BaseSchema


class UserCreateRequest(BaseSchema):
    username: str = Field(min_length=3, max_length=20)
    password: str = Field(min_length=3, max_length=72)


class TokenResponse(BaseSchema):
    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseSchema):
    id: int
    username: str
