import os

from dotenv import load_dotenv
from schemas.secrets import SecretContent

load_dotenv()

SECRET_ENCRYPTION_KEY = os.environ["SECRET_ENCRYPTION_KEY"]


def encrypt_secret(secret_content: SecretContent):
    print(secret_content)


def decrypt_secret():
    pass
