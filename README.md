# Release Tracker API

A hands-on backend development course from [Master.dev](https://master.dev/courses/pro-python) focused on building production-ready applications with modern Python and FastAPI.

## Overview

This repository contains my work and notes from completing **Python for Professional Developers**. The course covers modern Python development, REST API design, database integration, authentication, testing, containerization, and professional development tooling.

## What I Learned

- **Modern Python**

  - Type hints and static typing
  - Classes, dataclasses, enums, generics, and comprehensions
  - Decorators, context managers, generators, and exception handling
  - Modern Python development practices

- **FastAPI**

  - REST API development
  - Request and response validation with Pydantic
  - Dependency injection
  - API routers and application structure
  - Error handling and middleware
  - OpenAPI documentation

- **Database Development**

  - PostgreSQL integration
  - SQLModel and relational data modeling
  - CRUD operations and database queries
  - Alembic migrations
  - Database seeding
  - Relationship loading and avoiding N+1 queries

- **Authentication & Security**

  - JWT-based authentication
  - OAuth2 password bearer authentication
  - Password hashing with Argon2
  - Authentication dependencies
  - Authorization concepts and protected endpoints

- **Testing & Code Quality**

  - Pytest and test fixtures
  - API and database testing
  - MyPy for static type checking
  - Ruff for linting and formatting
  - Pre-commit hooks
  - Test coverage

- **DevOps & Deployment**

  - Docker and Docker Compose
  - Environment configuration and secrets
  - Application health checks
  - Logging and middleware
  - GitHub Actions and CI workflows
  - Reproducible dependency management with UV

## Technologies

| Category             | Technologies           |
| -------------------- | ---------------------- |
| Language             | Python                 |
| Framework            | FastAPI                |
| Validation           | Pydantic               |
| ORM                  | SQLModel               |
| Database             | PostgreSQL             |
| Migrations           | Alembic                |
| Authentication       | JWT, OAuth2, Argon2    |
| Testing              | Pytest                 |
| Type Checking        | MyPy                   |
| Linting & Formatting | Ruff                   |
| Package Management   | UV                     |
| Containers           | Docker, Docker Compose |
| CI                   | GitHub Actions         |

## Project

As part of the course, I built a production-style **Release Tracker REST API**.

The application demonstrates:

- Project and task management
- CRUD operations
- Relational database models
- Filtering and querying
- Request validation
- Database migrations
- JWT authentication
- Protected API endpoints
- Automated tests
- Logging and middleware
- Docker-based development

## Development

### Requirements

- Python 3.14+
- UV
- Docker
- Docker Compose

### Install Dependencies

```bash
uv sync
```

### Start PostgreSQL

```bash
docker compose up -d
```

### Run Migrations

```bash
uv run alembic upgrade head
```

### Run the Application

```bash
uv run fastapi dev
```

The API documentation is available through FastAPI's automatically generated OpenAPI documentation.

### Run Tests

```bash
uv run pytest
```

### Run Code Quality Checks

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy .
```

## Course

**Python for Professional Developers**
Master.dev

Course: https://master.dev/courses/pro-python

## Certificate

Completed the **Python for Professional Developers** course, covering modern Python backend development and production-ready API engineering.
