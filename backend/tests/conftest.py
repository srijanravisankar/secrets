import pytest
from models import Base
from schemas.secrets import SecretCreateRequest
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker


@pytest.fixture
def db():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    SessionLocal = sessionmaker(engine)

    Base.metadata.create_all(engine)

    with SessionLocal() as session:
        yield session


@pytest.fixture
def secret_request():
    secret_message = "meet me at noon"
    font_style = "serif"
    gif_url = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExam8xdWhpbW5qMThtamt1bTNpeDgwcjRoNXFhMDIxMDE3dHRnaXdwdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/f5ehe7RcZPIuFllGOi/giphy.gif"
    background_colour = "#123456"
    secret_prompt = "which country are you from"
    secret_password = "India"

    secret_request = SecretCreateRequest.model_validate(
        {
            "secret_message": secret_message,
            "font_style": font_style,
            "gif_url": gif_url,
            "background_colour": background_colour,
            "secret_prompt": secret_prompt,
            "secret_password": secret_password,
        }
    )

    return secret_request
