import uuid

import pytest
from schemas.secrets import SecretContent
from services.exceptions import InvalidSecretPasswordError
from services.secrets import create_secret, unlock_secret


def test_create_secret_stores_no_plaintext_content(db, secret_request):
    secret = create_secret(db, secret_request)

    assert secret_request.secret_message not in secret.secret_encrypted
    assert secret_request.font_style not in secret.secret_encrypted
    assert str(secret_request.gif_url) not in secret.secret_encrypted
    assert str(secret_request.background_colour) not in secret.secret_encrypted


def test_create_secret_stores_no_plaintext_password_or_prompt(db, secret_request):
    secret = create_secret(db, secret_request)

    assert secret_request.secret_prompt not in secret.secret_encrypted
    assert secret_request.secret_password not in secret.secret_encrypted


def test_unlock_secret_returns_content_for_correct_password(db, secret_request):
    secret = create_secret(db, secret_request)
    secret_content = unlock_secret(db, secret.id, secret_request.secret_password)

    secret_content_expected = SecretContent.model_validate(
        {
            "secret_message": secret_request.secret_message,
            "font_style": secret_request.font_style,
            "gif_url": secret_request.gif_url,
            "background_colour": secret_request.background_colour,
        }
    )

    assert secret_content == secret_content_expected


def test_unlock_secret_raises_error_for_wrong_password(db, secret_request):
    secret = create_secret(db, secret_request)

    with pytest.raises(InvalidSecretPasswordError):
        unlock_secret(db, secret.id, "wrong password")


def test_unlock_secret_returns_none_for_unknown_id(db):
    random_uuid = uuid.uuid4()
    assert unlock_secret(db, random_uuid, "some password") is None
