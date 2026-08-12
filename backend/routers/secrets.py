import uuid

from fastapi import APIRouter

router = APIRouter(prefix="/secrets")


@router.post("")
def create_secret_page():
    pass


@router.get("/{id}")
def get_secret_page_prompt(id: uuid.UUID):
    pass


@router.post("/{id}/unlock")
def unlock_secret_page(id: uuid.UUID):
    pass
