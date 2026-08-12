from fastapi import FastAPI
from routers import secrets

app = FastAPI()
app.include_router(secrets.router)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
