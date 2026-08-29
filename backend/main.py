import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, gifs, secrets, users

load_dotenv()

app = FastAPI()
app.include_router(secrets.router)
app.include_router(auth.router)
app.include_router(gifs.router)
app.include_router(users.router)

origins = os.environ["CORS_ORIGINS"].split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
