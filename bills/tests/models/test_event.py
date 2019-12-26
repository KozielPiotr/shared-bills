# pylint: disable=no-member
"""Tests for Event model."""

import pytest

from bills.models import Event


@pytest.mark.django_db
def test_event_create(sample_event):
    """sample_event should be an instance of Event class"""

    assert isinstance(sample_event, Event)


@pytest.mark.django_db
def test_event_repr(sample_event):
    """sample_event's str representation should be equal to it's name"""

    assert sample_event.__str__(), sample_event.name


@pytest.mark.django_db
def test_event_paymaster_relationship(sample_event, sample_participant):
    """sample_event's paymaster field should be related to sample_participant"""

    sample_event.paymaster = sample_participant
    sample_event.save()
    assert sample_event.paymaster == sample_participant
    assert sample_event in Event.objects.filter(paymaster=sample_participant)
    assert sample_event == Event.objects.get(paymaster=sample_participant.id)


@pytest.mark.django_db
def test_event_paymaster_delete(sample_event, sample_participant):
    """Deletion of sample_event paymaster related object should not delete sample event"""
    sample_event.paymaster = sample_participant
    sample_event.save()
    assert sample_event in Event.objects.all()
    sample_participant.delete()
    assert sample_event in Event.objects.all()
