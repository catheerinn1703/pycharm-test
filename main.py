import pytest

from method import generate_username, register_contract, get_user_by_username
from test_data import firstName, lastName, email, password, phone, userStatus

@pytest.mark.test
def test_create_user():
    username = generate_username()

    response, data = register_contract(username)
    assert response.status_code == 200
    assert data["message"] is not None
    assert data["type"] == "unknown"
    user_id = int(data["message"])

    response, data = get_user_by_username(username)
    assert response.status_code == 200
    assert data["id"] == user_id, "id not found"
    assert data["username"] == username
    assert data["firstName"] == firstName
    assert data["lastName"] == lastName
    assert data["email"] == email
    assert data["password"] == password
    assert data["phone"] == phone
    assert data["userStatus"] == userStatus
