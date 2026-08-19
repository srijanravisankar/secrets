from models.secrets import Secret
from schemas.secrets import SecretContent, SecretCreateRequest
from security.encryption import encrypt_secret
from security.passwords import hash_password
from sqlalchemy.orm import Session


def create_secret(db: Session, secret: SecretCreateRequest) -> Secret:
    secret_content = SecretContent.model_validate(secret.model_dump())

    new_secret = Secret(
        secret_prompt=secret.secret_prompt,
        secret_password_hash=hash_password(secret.secret_password),
        secret_encrypted=encrypt_secret(secret_content),
    )

    db.add(new_secret)
    db.commit()
    db.refresh(new_secret)

    return new_secret
