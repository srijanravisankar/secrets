import uuid

from enums.font import FontStyle
from pydantic import BaseModel, Field, HttpUrl
from pydantic_extra_types import Color


class SecretCreateRequest(BaseModel):
    secret_message: str = Field(min_length=1, max_length=1000)
    background_colour: Color
    font_style: FontStyle
    gif_url: HttpUrl

    secret_prompt: str = Field(min_length=1, max_length=100)
    secret_password: str = Field(min_length=8)


class SecretCreateResponse(BaseModel):
    id: uuid.UUID


class SecretPromptResponse(BaseModel):
    secret_prompt: str


class SecretReadRequest(BaseModel):
    secret_password: str


class SecretReadResponse(BaseModel):
    secret_message: str
    background_colour: Color
    font_style: FontStyle
    gif_url: HttpUrl
