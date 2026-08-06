from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.exc import NoResultFound
from sqlmodel import Session, select

from release_tracker.database import get_session
from release_tracker.models import Project, ProjectCreate, ProjectRead, ProjectUpdate


def slugify(value: str) -> str:
    cleaned = "".join(c for c in value.lower() if c.isalnum() or c == " ")
    return "-".join(cleaned.split()) or "project"


app = FastAPI(
    title="Release Tracker API",
    description="An API for tracking project milestones and tasks for devs.",
)

SessionDep = Annotated[Session, Depends(get_session)]


@app.get("/projects", response_model=list[ProjectRead])
def list_projects(session: SessionDep):
    statement = select(Project).order_by(Project.name)
    projects = session.exec(statement).all()

    return list(projects)


@app.get("/projects/{slug}", response_model=ProjectRead)
def get_project(session: SessionDep, slug: str):
    statement = select(Project).where(Project.slug == slug)

    try:
        project = session.exec(statement).one()
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )

    return project


@app.post("/projects", response_model=ProjectRead, status_code=status.HTTP_201_CREATED)
def create_project(
    session: SessionDep,
    payload: ProjectCreate,
):
    project = Project.model_validate(payload, update={"slug": slugify(payload.name)})
    session.add(project)
    session.commit()
    session.refresh(project)
    return project


@app.patch("/projects/{project_id}", response_model=ProjectRead)
def update_project(session: SessionDep, project_id: int, payload: ProjectUpdate):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Project not found"
        )

    updated_fields = payload.model_dump(exclude_unset=True)
    project.sqlmodel_update(updated_fields)

    if "name" in updated_fields and updated_fields["name"] is not None:
        project.slug = slugify(updated_fields["name"])

    session.add(project)
    session.commit()
    session.refresh(project)
    return project


@app.get("/projects/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(session: SessionDep, project_id: int):
    project = session.get(Project, project_id)

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )

    session.delete(project)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
