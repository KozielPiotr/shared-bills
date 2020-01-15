# pylint: disable=no-member, unused-argument
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


# UserViewset.change_password
@pytest.mark.django_db
def test_change_password(sample_user):
    """User object password should be changed."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    password_data = {"password": "testpassword", "new_password": "changed_password"}
    response = client.post(
        reverse("user-change-password"), password_data, format="json"
    )
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_change_password_fail_wrong_password(sample_user):
    """
    User object password should not be changed
    with incorrect password provided.
    """

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    password_data = {"password": "wrongpassword", "new_password": "changed_password"}
    response = client.post(
        reverse("user-change-password"), password_data, format="json"
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_change_password_fail_short_password(sample_user):
    """
    User object password should not be changed
    with too short password provided.
    """

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    password_data = {"password": "a", "new_password": "changed_password"}
    response = client.post(
        reverse("user-change-password"), password_data, format="json"
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_change_password_fail_while_logged_out():
    """Access should be forbidden for not logged user."""

    client = APIClient()

    password_data = {"old_password": "testpassword", "new_password": "changed_password"}
    response = client.patch(
        reverse("user-change-password"), password_data, format="json"
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_change_password_fail_get(sample_user):
    """GET method should not be allowed."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    response = client.get(reverse("user-change-password"), format="json")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_change_password_fail_put(sample_user):
    """PUT method should not be allowed."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    password_data = {"email": "test@test.com", "password": "testpassword"}
    response = client.put(reverse("user-change-password"), password_data, format="json")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_change_password_fail_put(sample_user):
    """PUT method should not be allowed."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    password_data = {"email": "test@test.com", "password": "testpassword"}
    response = client.put(reverse("user-change-password"), password_data, format="json")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_change_password_fail_delete(sample_user):
    """DELETE method should not be allowed."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    response = client.delete(reverse("user-change-password"), format="json")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_change_password_fail_wrong_data(sample_user):
    """Passing wrong data (eg. email instead of password) should return HTTP_400."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    password_data = {"email": "test@test.com"}
    response = client.post(
        reverse("user-change-password"), password_data, format="json"
    )
    assert response.status_code == status.HTTP_400_BAD_REQUEST


# UserViewset.delete_user
@pytest.mark.django_db
def test_delete_user(sample_user):
    """Sample_user object should be deleted."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    assert User.objects.filter(email=sample_user.email).count() == 1
    password_data = {"password": "testpassword"}

    response = client.post(reverse("user-delete-user"), password_data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert User.objects.filter(email=sample_user.email).count() == 0


@pytest.mark.django_db
def test_delete_user_fail_wrong_password(sample_user):
    """Sample_user object should not be deleted with wrong password provided."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    assert User.objects.filter(email=sample_user.email).count() == 1
    password_data = {"password": "wrongpassword"}

    response = client.post(reverse("user-delete-user"), password_data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert User.objects.filter(email=sample_user.email).count() == 1


@pytest.mark.django_db
def test_delete_user_fail_short_password(sample_user):
    """Sample_user object should not be deleted with too short password provided."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    assert User.objects.filter(email=sample_user.email).count() == 1
    password_data = {"password": "a"}

    response = client.post(reverse("user-delete-user"), password_data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert User.objects.filter(email=sample_user.email).count() == 1


@pytest.mark.django_db
def test_delete_user_fail_while_logged_out(sample_user):
    """Access should be forbidden for not logged user."""

    client = APIClient()

    assert User.objects.all().count() == 1
    password_data = {"password": "testpassword"}

    response = client.post(reverse("user-delete-user"), password_data, format="json")
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert User.objects.all().count() == 1


@pytest.mark.django_db
def test_delete_user_fail_get(sample_user):
    """GET method should not be allowed."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    assert User.objects.all().count() == 1

    response = client.get(reverse("user-delete-user"), format="json")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    assert User.objects.all().count() == 1


@pytest.mark.django_db
def test_delete_user_fail_put(sample_user):
    """PUT method should not be allowed."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    assert User.objects.all().count() == 1
    password_data = {"password": "testpassword"}

    response = client.put(reverse("user-delete-user"), password_data, format="json")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    assert User.objects.all().count() == 1


@pytest.mark.django_db
def test_delete_user_fail_patch(sample_user):
    """PATCH method should not be allowed."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    assert User.objects.all().count() == 1
    password_data = {"password": "testpassword"}

    response = client.patch(reverse("user-delete-user"), password_data, format="json")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    assert User.objects.all().count() == 1


@pytest.mark.django_db
def test_delete_user_fail_delete(sample_user):
    """DELETE method should not be allowed."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    assert User.objects.all().count() == 1

    response = client.delete(reverse("user-delete-user"), format="json")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    assert User.objects.all().count() == 1


@pytest.mark.django_db
def test_delete_user_fail_wrong_data(sample_user):
    """Passing wrong data (eg. email instead of password) should return HTTP_400."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    assert User.objects.all().count() == 1

    password_data = {"email": "test@test.com"}
    response = client.post(reverse("user-delete-user"), password_data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert User.objects.all().count() == 1
