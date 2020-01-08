# pylint: disable=no-member
"""Tests for bills bills views."""

import json
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from accounts.models import User


@pytest.mark.django_db
def test_get_user(sample_user):
    """Request should return proper event data."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    response = client.get(reverse("user-detail"), format="json")
    assert response.status_code == status.HTTP_200_OK
    assert json.dumps(response.data) == json.dumps(
        {"id": sample_user.pk, "email": sample_user.email}
    )


@pytest.mark.django_db
def test_delete_detail_user(sample_user):
    """DELETE method should be allowed."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    response = client.delete(reverse("user-detail"), format="json")
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_fail_post_detail_user(sample_user):
    """POST method should not be allowed."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    user_data = {"email": "new@testuser.com", "password": "testpassword"}
    response = client.post(reverse("user-detail"), user_data, format="json")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_fail_put_detail_user(sample_user):
    """PUT method should not be allowed."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    user_data = {"email": "new@testuser.com", "password": "testpassword"}
    response = client.put(reverse("user-detail"), user_data, format="json")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_fail_patch_detail_user(sample_user):
    """PATCH method should not be allowed."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    user_data = {"email": "new@testuser.com", "password": "testpassword"}
    response = client.patch(reverse("user-detail"), user_data, format="json")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_register_user():
    """New User object should be created."""

    client = APIClient()
    assert User.objects.filter(email="test@test.com").count() == 0

    user_data = {"email": "test@test.com", "password": "testpassword"}
    response = client.post(reverse("user-register"), user_data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(email="test@test.com").count() == 1


@pytest.mark.django_db
def test_register_user_fail_while_logged(sample_user):
    """New User object should be created."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    assert User.objects.filter(email="test@test.com").count() == 0

    user_data = {"email": "test@test.com", "password": "testpassword"}
    response = client.post(reverse("user-register"), user_data, format="json")
    assert response.status_code == status.HTTP_403_FORBIDDEN
