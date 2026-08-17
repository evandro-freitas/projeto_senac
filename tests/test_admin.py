from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_admin_without_auth_returns_401():
    response = client.get("/admin")
    assert response.status_code == 401


def test_admin_student_returns_403():
    response = client.get(
        "/admin",
        headers={"Authorization": "Bearer token-aluno"},
    )

    assert response.status_code == 403


def test_admin_admin_returns_200():
    response = client.get(
        "/admin",
        headers={"Authorization": "Bearer token-admin"},
    )

    assert response.status_code == 200
