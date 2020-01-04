# pylint: disable=no-member, bad-continuation
"""Tests for Bill model."""

import pytest
from django.db.models.deletion import ProtectedError

from bills.models import Bill, Event, Participant


@pytest.mark.django_db
def test_bill_create(sample_bill):
    """sample_event should be an instance of Event class"""

    assert isinstance(sample_bill, Bill)


@pytest.mark.django_db
def test_bill_repr(sample_bill):
    """sample_bill's str representation should be equal to it's title"""

    assert sample_bill.__str__() == sample_bill.title


@pytest.mark.django_db
def test_bill_event_relationship(sample_bill):
    """Event object has to be related to the bill when bill is created"""

    event = sample_bill.event
    assert isinstance(event, Event)
    assert sample_bill in Bill.objects.filter(event=event)
    assert sample_bill == Bill.objects.get(event=event)
    assert sample_bill in event.bills.all()


@pytest.mark.django_db
def test_bill_event_delete(sample_bill):
    """Deletion of related event object should delete sample_bill"""

    event = sample_bill.event
    assert sample_bill in Bill.objects.all()
    event.delete()
    assert sample_bill not in Bill.objects.all()


@pytest.mark.django_db
def test_bill_payer_relationship(sample_bill, sample_participant):
    """sample_bill's payer field should be related to sample_participant"""

    sample_bill.payer = sample_participant
    sample_bill.save()
    assert sample_bill.payer == sample_participant
    assert sample_bill in Bill.objects.filter(payer=sample_participant)
    assert sample_bill == Bill.objects.get(payer=sample_participant)
    assert sample_bill in sample_participant.payer.all()


@pytest.mark.django_db
def test_bill_payer_delete(sample_bill, sample_participant):
    """
    It should not be possible to delete sample_participant
    if related to sample_bill's payer field
    """

    sample_bill.payer = sample_participant
    sample_bill.save()
    with pytest.raises(Exception) as e_info:
        sample_participant.delete()
    assert e_info.type == ProtectedError


@pytest.mark.django_db
def test_bill_participants_relationship(
    sample_bill, sample_bill_2, sample_participant, sample_participant_2
):
    """
    sample_bill and sample_bill_2 should be related to
    sample_participant and sample_participant_2
    """
    sample_bill.participants.add(sample_participant, sample_participant_2)
    sample_bill_2.participants.add(sample_participant, sample_participant_2)
    sample_bill.save()
    assert sample_participant in sample_bill.participants.all()
    assert sample_participant_2 in sample_bill.participants.all()
    assert sample_participant in sample_bill_2.participants.all()
    assert sample_participant_2 in sample_bill_2.participants.all()


@pytest.mark.django_db
def test_bill_participants_relationship_backref(
    sample_bill, sample_bill_2, sample_participant, sample_participant_2
):
    """
    sample_bill and sample_bill_2 should be related to
    sample_participant and sample_participant_2
    """
    sample_participant.bills.add(sample_bill, sample_bill_2)
    sample_participant_2.bills.add(sample_bill, sample_bill_2)
    sample_bill.save()
    assert sample_bill in sample_participant.bills.all()
    assert sample_bill_2 in sample_participant.bills.all()
    assert sample_bill in sample_participant_2.bills.all()
    assert sample_bill_2 in sample_participant_2.bills.all()


@pytest.mark.django_db
def test_bill_participants_delete_participants(sample_bill, sample_participant):
    """Deletion of sample_participant sholud not affect sample_bill"""

    sample_bill.participants.add(sample_participant)
    sample_bill.save()
    sample_participant.delete()
    assert sample_bill in Bill.objects.all()


@pytest.mark.django_db
def test_bill_participants_delete_bill(sample_bill, sample_participant):
    """Deletion of sample_bill should not affect sample_participant"""

    sample_bill.participants.add(sample_participant)
    sample_bill.save()
    sample_bill.delete()
    assert sample_participant in Participant.objects.all()
