from fastapi import Depends, FastAPI

from app.config import Settings, get_settings
from app.postgresql import postgresql_connection

app = FastAPI()


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }


@app.on_event("startup")
async def startup():
    await postgresql_connection()
