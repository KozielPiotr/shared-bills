# pylint: disable=no-member, redefined-outer-name
"""Fixtures for tests."""

import pytest

from accounts.models import User
from bills.models import Bill, Event, Payment, Participant
from bills.tests.utils import create, delete


@pytest.fixture
def sample_user():
    """Creates new User object"""

    yield User.objects.create_user(email="Sample user", password="testpassword")


@pytest.fixture
def sample_user_2():
    """Creates new User object"""

    yield User.objects.create_user(email="Sample user 2", password="testpassword")


@pytest.fixture
def sample_participant():
    """Creates new Participant object"""

    participant = Participant(username="Sample participant")
    if participant not in Participant.objects.all():
        yield create(participant)
    if participant in Participant.objects.all():
        for bill in participant.payer.all():
            bill.delete()
        delete(participant)


@pytest.fixture
def sample_participant_2():
    """Creates new Participant object"""

    participant = Participant(username="Sample participant 2")
    if participant not in Participant.objects.all():
        yield create(participant)
    if participant in Participant.objects.all():
        for bill in participant.payer.all():
            bill.delete()
        delete(participant)


@pytest.fixture
def sample_event(sample_user):
    """Creates new Event object"""

    event = Event(name="Sample event", user=sample_user)
    if event not in Event.objects.all():
        yield create(event)
    if event in Event.objects.filter():
        delete(event)


@pytest.fixture
def sample_event_2(sample_user_2):
    """Creates new Event object"""

    event = Event(name="Sample event 2", user=sample_user_2)
    if event not in Event.objects.all():
        yield create(event)
    if event in Event.objects.filter():
        delete(event)


@pytest.fixture
def sample_bill(sample_event):
    """Creates new Bill object"""

    bill = Bill(title="test bill", event=sample_event)
    if bill not in Bill.objects.all():
        yield create(bill)
    if bill in Bill.objects.all():
        delete(bill)


@pytest.fixture
def sample_bill_2(sample_event):
    """Creates new Bill object"""

    bill = Bill(title="test bill 2", event=sample_event)
    if bill not in Bill.objects.all():
        yield create(bill)
    if bill in Bill.objects.all():
        delete(bill)


@pytest.fixture
def sample_payment(sample_participant, sample_participant_2, sample_event):
    """Creates new Payment object"""

    payment = Payment(
        title="sample payment",
        issuer=sample_participant,
        acquirer=sample_participant_2,
        event=sample_event,
    )
    if payment not in Payment.objects.all():
        yield create(payment)
    if payment in Payment.objects.all():
        delete(payment)


@pytest.fixture
def sample_payment_2(sample_participant, sample_participant_2, sample_event):
    """Creates new Payment object"""

    payment = Payment(
        title="sample payment",
        issuer=sample_participant,
        acquirer=sample_participant_2,
        event=sample_event,
    )
    if payment not in Payment.objects.all():
        yield create(payment)
    if payment in Payment.objects.all():
        delete(payment)
