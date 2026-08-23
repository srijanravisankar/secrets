import pytest
from jwt import ExpiredSignatureError, InvalidSignatureError
from security import tokens


def test_decode_access_token_returns_correct_username():
    username = "Srijan"
    encoded_jwt = tokens.create_access_token(username)
    decoded_username = tokens.decode_access_token(encoded_jwt)
    assert decoded_username == username


def test_decode_access_token_rejects_token_with_different_secret(monkeypatch):
    encoded_jwt = tokens.create_access_token("Srijan")
    monkeypatch.setattr(tokens, "JWT_SECRET", "differet-jwt-secret")
    with pytest.raises(InvalidSignatureError):
        tokens.decode_access_token(encoded_jwt)


def test_decode_access_token_rejects_expired_token(monkeypatch):
    monkeypatch.setattr(tokens, "JWT_EXPIRE_MINUTES", -1)
    encoded_jwt = tokens.create_access_token("Srijan")
    with pytest.raises(ExpiredSignatureError):
        tokens.decode_access_token(encoded_jwt)
