"""Standard result returned by every agent so the aggregator can treat them uniformly."""
from typing import Literal
from pydantic import BaseModel, Field
from legal_agent.schemas.citation import Citation


class AgentResult(BaseModel):
    agent: str
    answer: str = ""
    citations: list[Citation] = Field(default_factory=list)
    confidence: float = 0.0
    status: Literal["ok", "timeout", "error"] = "ok"
    error: str | None = None
    latency_ms: int = 0
