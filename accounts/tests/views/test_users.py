# pylint: disable=no-member
"""Tests for bills bills views."""

import json
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from accounts.models import User


@pytest.mark.django_db
def test_get_users(sample_user, sample_user_2):
    """Request should return all User objects data."""

    client = APIClient()

    response = client.get(reverse("accounts:users-list"), format="json")
    assert response.status_code == status.HTTP_200_OK
    assert json.dumps(response.data) == json.dumps(
        [
            {
                "id": sample_user.pk,
                "url": r"http://testserver{}".format(
                    reverse("accounts:users-detail", kwargs={"pk": sample_user.pk})
                ),
                "email": sample_user.email,
            },
            {
                "id": sample_user_2.pk,
                "url": r"http://testserver{}".format(
                    reverse("accounts:users-detail", kwargs={"pk": sample_user_2.pk})
                ),
                "email": sample_user_2.email,
            },
        ]
    )


@pytest.mark.django_db
def test_get_user(sample_user):
    """Request should return proper event data."""

    client = APIClient()

    response = client.get(
        reverse("accounts:users-detail", kwargs={"pk": sample_user.pk}), format="json"
    )
    assert response.status_code == status.HTTP_200_OK
    assert json.dumps(response.data) == json.dumps(
        {
            "id": sample_user.pk,
            "url": r"http://testserver{}".format(
                reverse("accounts:users-detail", kwargs={"pk": sample_user.pk})
            ),
            "email": sample_user.email,
        }
    )


@pytest.mark.django_db
def test_fail_post_list_user():
    """POST method should not be allowed."""

    client = APIClient()

    user_data = {"email": "new@testuser.com", "password": "testpassword"}
    response = client.post(reverse("accounts:users-list"), user_data, format="json")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_fail_put_list_user():
    """PUT method should not be allowed."""

    client = APIClient()

    user_data = {"email": "new@testuser.com", "password": "testpassword"}
    response = client.put(reverse("accounts:users-list"), user_data, format="json")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_fail_patch_list_user():
    """PATCH method should not be allowed."""

    client = APIClient()

    user_data = {"email": "new@testuser.com", "password": "testpassword"}
    response = client.patch(reverse("accounts:users-list"), user_data, format="json")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_fail_delete_list_user():
    """DELETE method should not be allowed."""

    client = APIClient()

    response = client.delete(reverse("accounts:users-list"), format="json")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_fail_post_detail_user(sample_user):
    """POST method should not be allowed."""

    client = APIClient()

    user_data = {"email": "new@testuser.com", "password": "testpassword"}
    response = client.post(
        reverse("accounts:users-detail", kwargs={"pk": sample_user.pk}),
        user_data,
        format="json",
    )
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_fail_put_detail_user(sample_user):
    """PUT method should not be allowed."""

    client = APIClient()

    user_data = {"email": "new@testuser.com", "password": "testpassword"}
    response = client.put(
        reverse("accounts:users-detail", kwargs={"pk": sample_user.pk}),
        user_data,
        format="json",
    )
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_fail_patch_detail_user(sample_user):
    """PATCH method should not be allowed."""

    client = APIClient()

    user_data = {"email": "new@testuser.com", "password": "testpassword"}
    response = client.patch(
        reverse("accounts:users-detail", kwargs={"pk": sample_user.pk}),
        user_data,
        format="json",
    )
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


@pytest.mark.django_db
def test_fail_delete_detail_user(sample_user):
    """DELETE method should not be allowed."""

    client = APIClient()

    response = client.patch(
        reverse("accounts:users-detail", kwargs={"pk": sample_user.pk}), format="json"
    )
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


# @pytest.mark.django_db
# def test_register_user():
#     """New User object should be created."""
#
#     client = APIClient()
#     assert User.objects.all().count() == 0
#
#     user_data = {"email": "test@test.com", "password": "testpassword"}
#     response = client.post("accounts:users-register", user_data, format="json")
#     assert response.status_code == status.HTTP_201_CREATED
