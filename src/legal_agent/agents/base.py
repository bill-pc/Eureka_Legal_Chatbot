"""Base agent interface. Every specialist agent implements `run` and returns an AgentResult."""
from abc import ABC, abstractmethod
from legal_agent.schemas.agent_result import AgentResult


class BaseAgent(ABC):
    name: str = "base"

    @abstractmethod
    async def run(self, query: str, ctx: dict) -> AgentResult:
        """Process the query with the shared context (intent, entities, time reference)."""
