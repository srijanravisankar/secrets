import uuid

from pydantic import BaseModel, ConfigDict, Field, HttpUrl
from pydantic_extra_types.color import Color
from schemas.font import FontStyle


class SecretContent(BaseModel):
    secret_message: str = Field(min_length=1, max_length=1000)
    font_style: FontStyle
    gif_url: HttpUrl
    background_colour: Color


class SecretCreateRequest(SecretContent):
    secret_prompt: str = Field(min_length=1, max_length=100)
    secret_password: str = Field(min_length=8)


class SecretCreateResponse(BaseModel):
    id: uuid.UUID

    model_config = ConfigDict(from_attributes=True)


class SecretPromptResponse(BaseModel):
    secret_prompt: str


class SecretReadRequest(BaseModel):
    secret_password: str


class SecretReadResponse(SecretContent):
    pass
