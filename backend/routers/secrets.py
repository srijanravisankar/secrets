import uuid
from typing import Annotated

from database import get_db
from fastapi import APIRouter, Depends, status
from models import Secret
from schemas.secrets import SecretCreateRequest, SecretCreateResponse
from security.passwords import hash_password
from sqlalchemy.orm import Session

router = APIRouter(prefix="/secrets")

DbSession = Annotated[Session, Depends(get_db)]


@router.post(
    "", status_code=status.HTTP_201_CREATED, response_model=SecretCreateResponse
)
def create_secret_page(secret: SecretCreateRequest, db: DbSession):
    new_secret = Secret(
        secret_prompt=secret.secret_prompt,
        secret_password_hash=hash_password(secret.secret_password),
        # secret_encrypted=encrypt_secret(
        #     secret.secret_message,
        #     secret.font_style,
        #     secret.gif_url,
        #     secret.background_colour,
        # ),
    )

    db.add(new_secret)
    db.commit()
    db.refresh(new_secret)

    return new_secret


@router.get("/{id}")
def get_secret_page_prompt(id: uuid.UUID):
    pass


@router.post("/{id}/unlock")
def unlock_secret_page(id: uuid.UUID):
    pass
