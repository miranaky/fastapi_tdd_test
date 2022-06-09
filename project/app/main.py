import logging

from fastapi import FastAPI

from app.postgresql import postgresql_connection
from app.api import ping

logger = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    logger.info("Starting up...")
    await postgresql_connection()


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutdown ...")
