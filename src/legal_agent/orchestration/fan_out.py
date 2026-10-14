"""Fan-out: runs the selected agents concurrently with a per-branch timeout.

A failed or timed-out branch never blocks the others; partial results are returned.
"""
import asyncio
from legal_agent.schemas.agent_result import AgentResult


async def _run_branch(agent, query, ctx, timeout_s: float) -> AgentResult:
    try:
        return await asyncio.wait_for(agent.run(query, ctx), timeout=timeout_s)
    except asyncio.TimeoutError:
        return AgentResult(agent=agent.name, status="timeout")
    except Exception as exc:  # keep other branches alive
        return AgentResult(agent=agent.name, status="error", error=str(exc))


async def fan_out(agents, query, ctx, timeout_s: float = 20.0) -> list[AgentResult]:
    """Run all agents in parallel and collect their results."""
    return await asyncio.gather(*(_run_branch(a, query, ctx, timeout_s) for a in agents))
