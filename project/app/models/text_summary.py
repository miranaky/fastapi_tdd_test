from datetime import datetime

from sqlmodel import Field, SQLModel


class TextSummary(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, index=True, nullable=False)
    url: str
    summary: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class SummaryPayloadSchema(SQLModel):
    url: str


class SummaryResponseSchema(SummaryPayloadSchema):
    id: int
