# tests/test_views.py
import pytest
from django.urls import reverse

from users.models import CustomUser


@pytest.fixture
def create_user():
    return CustomUser.objects.create_user(username="testuser", password="password")


@pytest.mark.django_db
def test_user_login(client, create_user):
    login_url = reverse("login")
    response = client.post(login_url, {"username": "testuser", "password": "password"})
    assert response.status_code == 200  # or whatever status is expected


@pytest.mark.django_db
def test_user_logout(client, create_user):
    logout_url = reverse("logout")
    client.login(username="testuser", password="password")
    response = client.get(logout_url)
    assert response.status_code == 302  # Redirect status code after logout
