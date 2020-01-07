# pylint: disable=no-member, redefined-outer-name
"""Fixtures for tests."""

import pytest

from accounts.models import User
from accounts.tests.utils import create, delete
from bills.models import Participant


@pytest.fixture
def sample_user():
    """Creates new User object"""

    yield User.objects.create_user(email="sample@user.com", password="testpassword")


@pytest.fixture
def sample_user_2():
    """Creates new User object"""

    yield User.objects.create_user(email="sample2@user.com", password="testpassword")


@pytest.fixture
def sample_participant(sample_user):
    """Creates new Participant object"""

    participant = Participant(username="Sample participant", user=sample_user)
    if participant not in Participant.objects.all():
        yield create(participant)
    if participant in Participant.objects.all():
        for bill in participant.payer.all():
            bill.delete()
        delete(participant)


@pytest.fixture
def sample_participant_2(sample_user):
    """Creates new Participant object"""

    participant = Participant(username="Sample participant 2", user=sample_user)
    if participant not in Participant.objects.all():
        yield create(participant)
    if participant in Participant.objects.all():
        for bill in participant.payer.all():
            bill.delete()
        delete(participant)
