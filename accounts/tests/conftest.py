# pylint: disable=no-member, redefined-outer-name
"""Fixtures for tests."""

import pytest

from accounts.models import User
from accounts.tests.utils import create, delete
from bills.models import Event


@pytest.fixture
def sample_user():
    """Creates new User object"""

    yield User.objects.create_user(email="sample@user.com", password="testpassword")


@pytest.fixture
def sample_user_2():
    """Creates new User object"""

    yield User.objects.create_user(email="sample2@user.com", password="testpassword")


@pytest.fixture
def sample_event():
    """Creates new Event object"""

    event = Event(name="Sample event", user=sample_user)
    if event not in Event.objects.all():
        yield create(event)
    if event in Event.objects.filter():
        delete(event)


@pytest.fixture
def sample_event_2():
    """Creates new Event object"""

    event = Event(name="Sample event 2", user=sample_user)
    if event not in Event.objects.all():
        yield create(event)
    if event in Event.objects.filter():
        delete(event)
