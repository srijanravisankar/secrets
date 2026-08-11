from database import engine
from fastapi import FastAPI
from models import Base

Base.metadata.create_all(engine)

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "healthy"}
