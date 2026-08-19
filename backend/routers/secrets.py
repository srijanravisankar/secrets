import uuid
from typing import Annotated

from database import get_db
from fastapi import APIRouter, Depends, status
from models import Secret
from schemas.secrets import SecretCreateRequest, SecretCreateResponse
from services.secrets import create_secret
from sqlalchemy.orm import Session

router = APIRouter(prefix="/secrets")

DbSession = Annotated[Session, Depends(get_db)]


@router.post(
    "", status_code=status.HTTP_201_CREATED, response_model=SecretCreateResponse
)
def create_secret_page(db: DbSession, secret: SecretCreateRequest) -> Secret:
    return create_secret(db, secret)


@router.get("/{id}")
def get_secret_page_prompt(id: uuid.UUID):
    pass


@router.post("/{id}/unlock")
def unlock_secret_page(id: uuid.UUID):
    pass
