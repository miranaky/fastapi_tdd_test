from fastapi import HTTPException
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.text_summary import (
    SummaryPayloadSchema,
    SummaryResponseSchema,
    TextSummary,
)


async def post(session: AsyncSession, payload: SummaryPayloadSchema) -> SummaryResponseSchema:
    summary = TextSummary(url=payload.url, summary="dummy summary")
    session.add(summary)
    await session.commit()
    await session.refresh(summary)
    return summary


async def get(session: AsyncSession, id: int) -> TextSummary:
    summary = await session.get(TextSummary, id)
    if summary is None:
        raise HTTPException(status_code=404, detail=f"{TextSummary.__name__} with id {id} not found.")
    return summary


async def get_all(session: AsyncSession) -> list[TextSummary]:
    summary_list = await session.execute(select(TextSummary))
    return summary_list.scalars().all()
