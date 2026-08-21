import uuid

from pydantic import BaseModel, ConfigDict, Field, HttpUrl
from pydantic.alias_generators import to_camel
from schemas.font import FontStyle


class SecretBaseModel(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        alias_generator=to_camel,
        validate_by_name=True,
        serialize_by_alias=True,
        populate_by_name=True,
    )


class SecretContent(SecretBaseModel):
    secret_message: str = Field(min_length=1, max_length=1000)
    font_style: FontStyle
    gif_url: HttpUrl
    background_colour: str = Field(pattern=r"^#[0-9a-fA-F]{6}$")


class SecretCreateRequest(SecretContent):
    secret_prompt: str = Field(min_length=1, max_length=100)
    secret_password: str = Field(min_length=3, max_length=72)


class SecretCreateResponse(SecretBaseModel):
    id: uuid.UUID


class SecretPromptResponse(SecretBaseModel):
    secret_prompt: str


class SecretReadRequest(SecretBaseModel):
    secret_password: str


class SecretReadResponse(SecretContent):
    pass
