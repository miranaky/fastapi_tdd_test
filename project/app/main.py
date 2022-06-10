import logging

from fastapi import FastAPI

from app.api import ping, summaries
from app.postgresql import postgresql_connection

logger = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(summaries.router, prefix="/summaries", tags=["summaries"])

    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    logger.info("Starting up...")
    await postgresql_connection()


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutdown ...")
