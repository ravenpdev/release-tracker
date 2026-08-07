from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

from release_tracker.routers import projects

app = FastAPI(
    title="Release Tracker API",
    description="An API for tracking projects milestones and developer tasks.",
)

app.include_router(projects.router)


@app.exception_handler(IntegrityError)
def handle_integrity_error(request: Request, exc: IntegrityError):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"detail": "Data conflict occurred (e.g., duplicate entry)."},
    )


@app.get("/")
def read_root() -> dict[str, str]:
    return {"app": "Release Tracker API", "docs": "/docs"}
