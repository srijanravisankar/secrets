import bcrypt


def hash_password(password: str) -> str:
    password_bytes = password.encode()
    salt = bcrypt.gensalt()
    hashed_password_bytes = bcrypt.hashpw(password_bytes, salt)
    hashed_password = hashed_password_bytes.decode()
    return hashed_password


def verify_password(user_input: str, hashed_password: str) -> bool:
    user_input_bytes = user_input.encode()
    hashed_password_bytes = hashed_password.encode()
    verification_result = bcrypt.checkpw(user_input_bytes, hashed_password_bytes)
    return verification_result
