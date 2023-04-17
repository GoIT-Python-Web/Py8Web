from unittest.mock import MagicMock, patch, AsyncMock

import pytest

from src.database.models import User
from src.services.auth import auth_service


@pytest.fixture()
def access_token(client, user, session, monkeypatch):
    mock_send_email = MagicMock()
    monkeypatch.setattr("src.routes.auth.send_email", mock_send_email)
    client.post("/api/auth/signup", json=user)
    current_user: User = session.query(User).filter(User.email == user.get('email')).first()
    current_user.confirmed = True
    session.commit()
    response = client.post(
        "/api/auth/login",
        data={"username": user.get('email'), "password": user.get('password')},
    )
    data = response.json()
    return data["access_token"]


def test_create_cat(client, access_token):
    with patch.object(auth_service, 'redis') as r_mock:
        r_mock.get.return_value = None
        response = client.post(
            "/api/owners",
            json={"email": "test_owner@gmail.com"},
            headers={"Authorization": f"Bearer {access_token}"}
        )
        data = response.json()
        owner_id = data["id"]
        response = client.post(
            "/api/cats",
            json={"nickname": "Barsik", "age": 4, "description": "Just cat", "owner_id": owner_id},
            headers={"Authorization": f"Bearer {access_token}"}
        )
        assert response.status_code == 201, response.text
        data = response.json()
        assert "id" in data


def test_get_cats(client, access_token, monkeypatch):
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.redis", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.identifier", AsyncMock())
    monkeypatch.setattr("fastapi_limiter.FastAPILimiter.http_callback", AsyncMock())
    with patch.object(auth_service, 'redis') as r_mock:
        r_mock.get.return_value = None
        response = client.get(
            "/api/cats",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert type(data) == list
        assert "id" in data[0]
        assert "age" in data[0]
