# Legal Chatbot - Parallel Multi-Agent RAG

Router -> parallel fan-out to 4 specialist agents -> aggregator -> citation verification.

## Layout
- `apps/`  runnable apps (API + web)
- `src/legal_agent/`  the single Python package (orchestration, agents, retrieval, ingestion, harness, ...)
- `eval/`  retrieval, e2e and ablation evaluation
- `deploy/`  standalone infra compose files

## Run
```bash
cp .env.example .env
docker compose up -d --build
```
