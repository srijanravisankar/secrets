import pytest
from cryptography.fernet import InvalidToken
from security.encryption import decrypt, encrypt


def test_decrypt_returns_original_content():
    test_str = "meet me at noon"
    encrypted = encrypt(test_str)
    assert decrypt(encrypted) == test_str


def test_encrypt_does_not_leak_plaintext():
    test_str = "meet me at noon"
    encrypted = encrypt(test_str)
    assert test_str not in encrypted


def test_decrypt_returns_original_content_for_emoji():
    test_str = "😊"
    encrypted = encrypt(test_str)
    assert decrypt(encrypted) == test_str


def test_decrypt_rejects_tampered_token():
    test_str = "meet me at noon"
    encrypted = encrypt(test_str)
    tampered_str = encrypted[:-5] + "ABCDEFG"
    assert tampered_str != encrypted
    with pytest.raises(InvalidToken):
        decrypt(tampered_str)
