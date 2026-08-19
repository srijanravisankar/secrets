import uuid

from models.secrets import Secret
from schemas.secrets import SecretContent, SecretCreateRequest
from security.encryption import encrypt
from security.passwords import hash_password
from sqlalchemy.orm import Session


def create_secret(db: Session, secret: SecretCreateRequest) -> Secret:
    secret_content = SecretContent.model_validate(secret).model_dump_json()

    new_secret = Secret(
        secret_prompt=secret.secret_prompt,
        secret_password_hash=hash_password(secret.secret_password),
        secret_encrypted=encrypt(secret_content),
    )

    db.add(new_secret)
    db.commit()
    db.refresh(new_secret)

    return new_secret


def get_secret(db: Session, id: uuid.UUID):
    pass
