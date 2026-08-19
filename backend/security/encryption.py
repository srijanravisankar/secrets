import os

from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

SECRET_ENCRYPTION_KEY = os.environ["SECRET_ENCRYPTION_KEY"]
fernet = Fernet(SECRET_ENCRYPTION_KEY)


def encrypt(content: str) -> str:
    content_bytes = content.encode()
    encrypted_content_bytes = fernet.encrypt(content_bytes)
    encrypted_content = encrypted_content_bytes.decode()
    return encrypted_content


def decrypt(encrypted_content: str) -> str:
    encrypted_content_bytes = encrypted_content.encode()
    content_bytes = fernet.decrypt(encrypted_content_bytes)
    content = content_bytes.decode()
    return content
