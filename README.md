# Release Tracker API

Requirements:

- UV
- Python
- Docker

Docker and alembic commands:

- docker compose up -d
- docker compose exec db psql -U release_tracker -d release_tracker
- docker compose exec db psql -U release_tracker -d release_tracker -c "SELECT id, name, slug from projects"
- uv run alembic revision --autogenerate -m "initial"
- uv run alembic upgrade head
- uv run alembic downgrade -1
