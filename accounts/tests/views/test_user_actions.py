# pylint: disable=no-member
"""Tests for bills user views actions."""

import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from accounts.models import User


# UserViewset.register
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
    """Access should be forbidden for logged user."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    assert User.objects.filter(email="test@test.com").count() == 0

    user_data = {"email": "test@test.com", "password": "testpassword"}
    response = client.post(reverse("user-register"), user_data, format="json")
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_register_user_fail_get():
    """GET method should not be allowed."""

    client = APIClient()

    response = client.get(reverse("user-register"))
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_register_user_fail_put():
    """PUT method should not be allowed."""

    client = APIClient()

    user_data = {"email": "test@test.com", "password": "testpassword"}
    response = client.put(reverse("user-register"), user_data, format="json")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_register_user_fail_patch():
    """PATCH method should not be allowed."""

    client = APIClient()

    user_data = {"email": "test@test.com", "password": "testpassword"}
    response = client.patch(reverse("user-register"), user_data, format="json")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_register_user_fail_delete():
    """DELETE method should not be allowed."""

    client = APIClient()

    response = client.delete(reverse("user-register"), format="json")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_register_user_fail_wrong_data():
    """Passing wrong data should return HTTP_400."""

    client = APIClient()

    user_data = {"email": "test@test.com"}
    response = client.post(reverse("user-register"), user_data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_change_data(sample_user):
    """New User object email and password hould be changed."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    assert User.objects.filter(email="test@test.com").count() == 0

    user_data = {"email": "test@test.com", "password": "othertestpassword"}
    response = client.patch(reverse("user-change-data"), user_data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert User.objects.filter(email="test@test.com").count() == 1
    assert User.objects.all().count() == 1


@pytest.mark.django_db
def test_change_data_fail_while_logged():
    """Access should be forbidden for not logged user."""

    client = APIClient()

    assert User.objects.filter(email="test@test.com").count() == 0

    user_data = {"email": "test@test.com", "password": "othertestpassword"}
    response = client.post(reverse("user-change-data"), user_data, format="json")
    assert response.status_code == status.HTTP_403_FORBIDDEN


# UserViewset.change_data
@pytest.mark.django_db
def test_change_data_fail_get(sample_user):
    """GET method should not be allowed."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    response = client.get(reverse("user-change-data"), format="json")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_change_data_fail_post(sample_user):
    """POST method should not be allowed."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    user_data = {"email": "test@test.com", "password": "testpassword"}
    response = client.post(reverse("user-change-data"), user_data, format="json")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_change_data_fail_put(sample_user):
    """PUT method should not be allowed."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    user_data = {"email": "test@test.com", "password": "testpassword"}
    response = client.put(reverse("user-change-data"), user_data, format="json")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_change_data_fail_delete(sample_user):
    """DELETE method should not be allowed."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    response = client.delete(reverse("user-change-data"), format="json")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_change_data_fail_wrong_data(sample_user):
    """Passing wrong data should return HTTP_400."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    user_data = {"email": "test@test.com"}
    response = client.patch(reverse("user-change-data"), user_data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
