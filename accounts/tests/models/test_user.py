"""Tests for User model."""

import pytest

from accounts.models import User


@pytest.mark.django_db
def test_user_create(sample_user):
    """Sample_user should be an instance of User class"""

    assert isinstance(sample_user, User)
