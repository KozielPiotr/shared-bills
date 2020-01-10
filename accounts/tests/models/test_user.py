"""Tests for User model."""

import pytest

from accounts.models import User


@pytest.mark.django_db
def test_user_create(sample_user):
    """Sample_user should be an instance of User class"""

    assert isinstance(sample_user, User)


@pytest.mark.django_db
def test_user_repr(sample_user):
    """sample_user's str representation should be equal to it's email"""

    assert sample_user.__str__(), sample_user.email
