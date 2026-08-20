import uuid
from typing import Annotated

from database import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from models import Secret
from schemas.secrets import (
    SecretCreateRequest,
    SecretCreateResponse,
    SecretPromptResponse,
)
from services import secrets
from sqlalchemy.orm import Session

router = APIRouter(prefix="/secrets")

DbSession = Annotated[Session, Depends(get_db)]


@router.post(
    "", status_code=status.HTTP_201_CREATED, response_model=SecretCreateResponse
)
def create_secret(db: DbSession, secret: SecretCreateRequest) -> Secret:
    return secrets.create_secret(db, secret)


@router.get("/{id}", response_model=SecretPromptResponse)
def get_secret_prompt(db: DbSession, id: uuid.UUID) -> Secret:
    secret = secrets.get_secret(db, id)

    if secret is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Secret not found",
        )

    return secret


@router.post("/{id}/unlock")
def unlock_secret_page(id: uuid.UUID):
    pass
