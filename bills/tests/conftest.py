# pylint: disable=no-member, redefined-outer-name
"""Fixtures for tests."""

import pytest

from bills.tests.utils import create, delete
from bills.models import Bill, Event, Payment, Participant


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
def sample_event():
    """Creates new Event object"""

    event = Event(name="Sample event")
    if event not in Event.objects.all():
        yield create(event)
    if event in Event.objects.all():
        delete(event)


@pytest.fixture
def sample_event_2():
    """Creates new Event object"""

    event = Event(name="Sample event 2")
    if event not in Event.objects.all():
        yield create(event)
    if event in Event.objects.all():
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
