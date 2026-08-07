from fastapi import status
from fastapi.testclient import TestClient

from release_tracker.main import app

client = TestClient(app)


def test_list_projects():
    response = client.get("/projects")

    assert response.status_code == 200
    assert len(response.json()) == 4


def test_get_project_by_id():
    response = client.get("/projects/2")

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data["id"] == 2


def test_get_project_by_id_not_found():
    response = client.get("/projects/999")

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_create_project():
    pass


def test_delete_project_by_id_not_found():
    response = client.delete("/projects/5")
    assert response.status_code == status.HTTP_404_NOT_FOUND


# def test_get_project():
#     response = client.get("/projects/1")
#     assert response.status_code == status.HTTP_200_OK
#     assert response.json()["name"] == "Frontend Redesign"


# def test_get_project_not_found():
#     response = client.get("/projects/999")
#     assert response.status_code == status.HTTP_404_NOT_FOUND
