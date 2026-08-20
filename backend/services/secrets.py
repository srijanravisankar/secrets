import uuid

from models.secrets import Secret
from schemas.secrets import SecretContent, SecretCreateRequest
from security.encryption import decrypt, encrypt
from security.passwords import hash_password, verify_password
from services.exceptions import InvalidSecretPasswordError
from sqlalchemy.orm import Session


def create_secret(db: Session, secret: SecretCreateRequest) -> Secret:
    secret_content = SecretContent.model_validate(secret.model_dump())

    new_secret = Secret(
        secret_prompt=secret.secret_prompt,
        secret_password_hash=hash_password(secret.secret_password),
        secret_encrypted=encrypt(secret_content.model_dump_json()),
    )

    db.add(new_secret)
    db.commit()
    db.refresh(new_secret)

    return new_secret


def get_secret(db: Session, id: uuid.UUID) -> Secret | None:
    secret = db.get(Secret, id)
    return secret


def unlock_secret(
    db: Session, id: uuid.UUID, secret_password: str
) -> SecretContent | None:
    secret = db.get(Secret, id)

    if secret is None:
        return None

    verification = verify_password(secret_password, secret.secret_password_hash)

    if not verification:
        raise InvalidSecretPasswordError

    secret_content_str = decrypt(secret.secret_encrypted)
    secret_content = SecretContent.model_validate_json(secret_content_str)

    return secret_content
