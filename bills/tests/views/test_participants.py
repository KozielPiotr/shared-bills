# pylint: disable=no-member, bad-continuation
"""Tests for bills participants views"""

import json
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from bills.models import Participant


@pytest.mark.django_db
def test_get_participants(sample_event, sample_participant, sample_participant_2):
    """Request should return all Participant objects data related to sample_event"""

    client = APIClient()
    sample_event.participants.add(sample_participant)
    sample_event.participants.add(sample_participant_2)
    sample_event.save()

    response = client.get(
        reverse("bills:participants-list", kwargs={"event_pk": sample_event.pk}),
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    assert json.dumps(response.data) == json.dumps(
        [
            {
                "id": sample_participant.id,
                "url": r"http://testserver{}".format(
                    reverse(
                        "bills:participants-detail",
                        kwargs={
                            "event_pk": sample_event.pk,
                            "pk": sample_participant.pk,
                        },
                    )
                ),
                "username": sample_participant.username,
            },
            {
                "id": sample_participant_2.id,
                "url": r"http://testserver{}".format(
                    reverse(
                        "bills:participants-detail",
                        kwargs={
                            "event_pk": sample_event.pk,
                            "pk": sample_participant_2.pk,
                        },
                    )
                ),
                "username": sample_participant_2.username,
            },
        ]
    )


@pytest.mark.django_db
def test_get_participant(sample_event, sample_participant):
    """Request should return proper participant data"""

    client = APIClient()
    sample_event.participants.add(sample_participant)
    sample_event.save()

    response = client.get(
        reverse(
            "bills:participants-detail",
            kwargs={"event_pk": sample_event.pk, "pk": sample_participant.pk},
        ),
        format="jason",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "id": sample_participant.id,
        "url": r"http://testserver{}".format(
            reverse(
                "bills:participants-detail",
                kwargs={"event_pk": sample_event.pk, "pk": sample_participant.pk},
            )
        ),
        "username": sample_participant.username,
    }


@pytest.mark.django_db
def test_post_participant(sample_event):
    """New Participant object should be created"""

    client = APIClient()

    assert Participant.objects.filter(username="new participant").count() == 0
    participant_data = {"username": "new participant"}
    response = client.post(
        reverse("bills:participants-list", kwargs={"event_pk": sample_event.pk}),
        participant_data,
        format="json",
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert Participant.objects.filter(username="new participant").count() == 1


@pytest.mark.django_db
def test_delete_participant(sample_event, sample_participant):
    """Participant object should be deleted"""

    client = APIClient()
    sample_event.participants.add(sample_participant)
    sample_event.save()

    assert sample_participant in Participant.objects.filter(
        username=sample_participant.username
    )
    response = client.delete(
        reverse(
            "bills:participants-detail",
            kwargs={"event_pk": sample_event.pk, "pk": sample_participant.pk},
        ),
        format="json",
        follow=True,
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert sample_participant not in Participant.objects.filter(
        username=sample_participant.username
    )


@pytest.mark.django_db
def test_patch_participant(sample_event, sample_participant):
    """sample_participant should have a changed username"""

    client = APIClient()
    sample_event.participants.add(sample_participant)
    sample_event.save()

    changed_participant_data = {"username": "new test participant"}
    assert sample_participant in Participant.objects.filter(
        username=sample_participant.username
    )
    assert (
        Participant.objects.filter(
            username=changed_participant_data["username"]
        ).count()
        == 0
    )
    response = client.patch(
        reverse(
            "bills:participants-detail",
            kwargs={"event_pk": sample_event.pk, "pk": sample_participant.pk},
        ),
        changed_participant_data,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    assert sample_participant not in Participant.objects.filter(
        username=sample_participant.username
    )
    assert (
        Participant.objects.filter(
            username=changed_participant_data["username"]
        ).count()
        == 1
    )
