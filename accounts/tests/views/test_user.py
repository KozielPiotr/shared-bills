# pylint: disable=no-member
"""Tests for bills user views."""

import json
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from accounts.serializers import (
    PasswordCheckSerializer,
    UserChangePasswordSerializer,
    UserSerializer,
)
from accounts.views import UserViewset


@pytest.mark.django_db
def test_user_viewset_get_serializer_class_register():
    """When action==register function should return UserSerializer class."""

    viewset = UserViewset(action="register")
    assert viewset.get_serializer_class() == UserSerializer


@pytest.mark.django_db
def test_user_viewset_get_serializer_class_change_password():
    """
    When action==change_password function should return
    UserChangePasswordSerializer class.
    """

    viewset = UserViewset(action="change_password")
    assert viewset.get_serializer_class() == UserChangePasswordSerializer


@pytest.mark.django_db
def test_user_viewset_get_serializer_class_delete_user():
    """When action==delete_user function should return UserDeleteSerializer class."""

    viewset = UserViewset(action="delete_user")
    assert viewset.get_serializer_class() == PasswordCheckSerializer


@pytest.mark.django_db
def test_user_viewset_get_serializer_class_other():
    """Default serializer class should be UserSerializer."""

    viewset = UserViewset(action="other")
    assert viewset.get_serializer_class() == UserSerializer


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
def test_fail_delete_detail_user(sample_user):
    """DELETE method should not be allowed."""

    client = APIClient()
    client.login(email=sample_user.email, password="testpassword")

    response = client.delete(reverse("user-detail"), format="json")
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


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
