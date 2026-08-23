import os
from datetime import datetime, timedelta, timezone

import jwt
from dotenv import load_dotenv

load_dotenv()

JWT_SECRET = os.environ["JWT_SECRET"]
JWT_EXPIRE_MINUTES = int(os.environ["JWT_EXPIRE_MINUTES"])
ALGORITHM = "HS256"


def create_access_token(username: str) -> str:
    current_time = datetime.now(timezone.utc)
    expires_at = current_time + timedelta(minutes=JWT_EXPIRE_MINUTES)
    payload = {"sub": username, "exp": expires_at}
    encoded_jwt = jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> str:
    decoded_jwt = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
    return decoded_jwt["sub"]
