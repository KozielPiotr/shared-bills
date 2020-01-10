"""Tests for User model's user_manager."""

import pytest

from accounts.models import User


@pytest.mark.django_db
def test_user_manager_not_email():
    """Not delivering email should return ValueError"""

    with pytest.raises(ValueError):
        User.objects.create_user(email=None, password="testpassword")


@pytest.mark.django_db
def test_user_manager_create_superuser():
    """Not delivering email should return ValueError"""

    user = User.objects.create_superuser(
        email="super@user.com", password="testpassword"
    )
    assert user.is_superuser
