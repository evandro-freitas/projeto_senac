from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_list_courses_returns_200():
    response = client.get("/courses")
    assert response.status_code == 200


def test_list_courses_only_active():
    response = client.get("/courses")
    assert response.status_code == 200
    assert all(course["active"] is True for course in response.json())


def test_get_nonexistent_course_returns_404():
    response = client.get("/courses/999")
    assert response.status_code == 404


def test_delete_course_returns_204():
    response = client.delete("/courses/1")
    assert response.status_code == 204
    assert response.text == ""
