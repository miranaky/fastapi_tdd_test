from datetime import datetime
from sqlmodel import SQLModel, Field


class TextSummary(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    url: str
    summary: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class SummaryPayloadSchema(SQLModel):
    url: str
