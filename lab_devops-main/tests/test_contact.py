from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_empty_contact_returns_400():
    response = client.post(
        "/contact",
        json={"name": "", "email": "", "message": ""},
    )

    assert response.status_code == 400


def test_valid_contact_returns_201():
    response = client.post(
        "/contact",
        json={
            "name": "Maria",
            "email": "maria@example.com",
            "message": "Olá",
        },
    )

    assert response.status_code == 201
