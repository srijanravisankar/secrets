import os

from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

SECRET_ENCRYPTION_KEY = os.environ["SECRET_ENCRYPTION_KEY"]
fernet = Fernet(SECRET_ENCRYPTION_KEY)


def encrypt_secret(secret_content: str) -> str:
    secret_content_bytes = secret_content.encode()
    encrypted_secret_content = fernet.encrypt(secret_content_bytes)
    encrypted_secret = encrypted_secret_content.decode()
    return encrypted_secret


def decrypt_secret(encrypted_secret: str) -> str:
    encrypted_secret_bytes = encrypted_secret.encode()
    secret_content_encrypted = fernet.decrypt(encrypted_secret_bytes)
    secret_content = secret_content_encrypted.decode()
    return secret_content
