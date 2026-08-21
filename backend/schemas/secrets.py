import uuid

from pydantic import Field, HttpUrl
from schemas.base import BaseSchema
from schemas.font import FontStyle


class SecretContent(BaseSchema):
    secret_message: str = Field(min_length=1, max_length=1000)
    font_style: FontStyle
    gif_url: HttpUrl
    background_colour: str = Field(pattern=r"^#[0-9a-fA-F]{6}$")


class SecretCreateRequest(SecretContent):
    secret_prompt: str = Field(min_length=1, max_length=100)
    secret_password: str = Field(min_length=3, max_length=72)


class SecretCreateResponse(BaseSchema):
    id: uuid.UUID


class SecretPromptResponse(BaseSchema):
    secret_prompt: str


class SecretReadRequest(BaseSchema):
    secret_password: str


class SecretReadResponse(SecretContent):
    pass
