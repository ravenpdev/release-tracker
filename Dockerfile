# Optionally use a Docker container with uv already installed.
# More on the trade-offs: https://docs.astral.sh/uv/guides/integration/docker/
FROM python:3.14-slim

# Copy uv from the official image
COPY --from=ghcr.io/astral-sh/uv:0.11.6 /uv /uvx /bin/

# Compile bytecode for faster startup
ENV UV_COMPILE_BYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

COPY pyproject.toml uv.lock README.md ./
COPY src ./src
COPY alembic.ini ./
COPY alembic ./alembic
COPY scripts ./scripts

RUN uv sync --frozen --no-dev

EXPOSE 8000

# `fastapi run` defaults to 0.0.0.0:8000 with a single worker. For multiple
# workers, pass --workers directly:
#   CMD ["fastapi", "run", "--workers", "2"]
# For full control over timeouts, logging, or to use gunicorn, drop to uvicorn:
#   CMD ["uvicorn", "release_tracker.main:app", \
#        "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
CMD ["fastapi", "run"]
