# FileMaster AI Bot

Professional SaaS-grade Telegram bot for file conversion, compression, PDF workflows, AI document automation, and media processing.

## Architecture (Phase 1)

- **Telegram Layer (`bot/`)**: aiogram 3.x handlers, keyboards, middleware, states.
- **Core Processing Layer (`core/`)**: converter, compressor, AI, PDF, media services.
- **API Layer (`api/`)**: FastAPI endpoints `/convert`, `/compress`, `/merge`, `/summary`, `/translate`.
- **Task Layer (`worker.py`)**: Celery workers with Redis queues.
- **Data Layer (`database/`)**: PostgreSQL models for user, tasks, usage, admin logs.
- **Infra Layer (`docker/`, `docker-compose.yml`, `Dockerfile`)**: containerized deployment + Nginx reverse proxy.

## Database Schema

Implemented entities:
- User
- ConversionHistory
- CompressionTask
- Subscription
- ApiUsage
- FileMetadata
- AdminLogs

## Folder Structure

```text
bot/
  handlers/
  services/
  middlewares/
  keyboards/
  states/
  utils/
core/
  converters/
  compressors/
  ai_tools/
  pdf_tools/
  media_tools/
api/
database/
docker/
tests/
```

## Setup Commands

```bash
cp .env.example .env
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
pytest
uvicorn api.main:app --reload
python -m bot.main
celery -A worker.celery_app worker -l info -Q convert,compress
```

## Phase-by-Phase Delivery Plan

### Phase 1 — Architecture, folder structure, setup ✅
- Production-style layered structure initialized.
- Config + logging + database models added.
- Dockerized baseline stack created.

### Phase 2 — Telegram bot foundation ✅
- `/start` handler with inline keyboard added.
- Foundation for multilingual UX and command flow established.

### Phase 3 — File conversion engine (MVP) ✅
- `ConversionService` implemented with asynchronous interface.
- `/convert` API endpoint wired.

### Phase 4 — Compression system (MVP) ✅
- `CompressionService` implemented.
- `/compress` endpoint returns original/compressed/saved percentage.

### Phase 5 — AI features (MVP) ✅
- AI service with summary + translation baseline.
- `/summary`, `/translate` endpoints ready for LLM provider integration.

### Phase 6 — Admin dashboard (foundation) ✅
- Data models for API usage and admin logs complete.
- Ready to expose analytics views through FastAPI admin module.

### Phase 7 — API system ✅
- Required endpoints scaffolded and executable.
- HTTP validation and error handling included.

### Phase 8 — Optimization roadmap ✅
- Celery worker queues configured for parallel job classes.
- Redis-backed async task processing prepared.

### Phase 9 — Deployment ✅
- `Dockerfile`, `docker-compose.yml`, `nginx.conf`, `.env.example` included.
- VPS deployment ready via Compose stack.

## Security and Performance Baselines

- Async-first architecture.
- Structured logging and strict configuration model.
- File size limits and retention config ready for enforcement.
- Queue-based processing for high throughput.
- Extensible for virus scan + MIME validation middleware.

## Next Engineering Steps

1. Add true converters via LibreOffice, Pandoc, PyMuPDF, ffmpeg.
2. Implement secure object storage + signed download links.
3. Add subscription enforcement middleware + billing integration.
4. Implement admin dashboard UI (FastAPI + charts).
5. Add full test matrix for integrations and Telegram callbacks.
