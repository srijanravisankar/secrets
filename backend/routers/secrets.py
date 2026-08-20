import uuid
from typing import Annotated

from database import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from models import Secret
from schemas.secrets import (
    SecretContent,
    SecretCreateRequest,
    SecretCreateResponse,
    SecretPromptResponse,
    SecretReadRequest,
    SecretReadResponse,
)
from services import secrets
from services.exceptions import InvalidSecretPasswordError
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


@router.post("/{id}/unlock", response_model=SecretReadResponse)
def unlock_secret(
    db: DbSession, id: uuid.UUID, request: SecretReadRequest
) -> SecretContent:
    try:
        secret_unlocked = secrets.unlock_secret(db, id, request.secret_password)
    except InvalidSecretPasswordError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
        )

    if secret_unlocked is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Secret not found",
        )

    return secret_unlocked
