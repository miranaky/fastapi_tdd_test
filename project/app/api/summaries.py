import logging

from fastapi import APIRouter, Depends

from app.api import crud
from app.models.text_summary import (
    SummaryPayloadSchema,
    SummaryResponseSchema,
    TextSummary,
)
from app.postgresql import get_session

logger = logging.getLogger("summary")
router = APIRouter()


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema, session=Depends(get_session)) -> SummaryResponseSchema:
    return await crud.post(session, payload)


@router.get("/{id}/", response_model=TextSummary, status_code=200)
async def get_summary(id: int, session=Depends(get_session)) -> TextSummary:
    return await crud.get(session, id)


@router.get("/", response_model=list[TextSummary], status_code=200)
async def get_all_summaries(session=Depends(get_session)) -> list[TextSummary]:
    return await crud.get_all(session)
