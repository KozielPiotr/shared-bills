# pylint: disable=no-member
"""Tests for Participant model."""

import pytest

from bills.models import Participant


@pytest.mark.django_db
def test_participant_create(sample_participant):
    """sample_participant should be an instance of Participant class"""

    assert isinstance(sample_participant, Participant)


@pytest.mark.django_db
def test_participant_repr(sample_participant):
    """sample_participant's str representation should be equal to it's username"""

    assert sample_participant.__str__(), sample_participant.username


@pytest.mark.django_db
def test_participant_event_relationship(sample_participant, sample_event):
    """sample_event should be related to sample_participant and after deletion"""

    sample_participant.event = sample_event
    sample_participant.save()
    assert sample_participant.event == sample_event
    assert sample_participant in Participant.objects.filter(event=sample_event)
    assert sample_participant == Participant.objects.get(event=sample_event.id)
    assert sample_participant in sample_event.participants.all()


@pytest.mark.django_db
def test_participant_event_delete(sample_participant, sample_event):
    """After deletion of event participant should be also deleted"""

    sample_participant.event = sample_event
    sample_participant.save()

    assert sample_participant in sample_event.participants.all()
    sample_event.delete()
    assert sample_participant not in sample_event.participants.all()
