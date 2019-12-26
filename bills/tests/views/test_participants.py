# pylint: disable=no-member
"""Tests for bills participants views"""

import json
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from bills.models import Participant


@pytest.mark.django_db
def test_get_participants(sample_participant, sample_participant_2):
    """Request should return all Participant objects data"""

    client = APIClient()
    response = client.get(reverse("participant-list"), format="json")
    assert response.status_code == status.HTTP_200_OK
    assert json.dumps(response.data) == json.dumps(
        [
            {
                "id": sample_participant.id,
                "url": r"http://testserver{}".format(
                    reverse("participant-detail", kwargs={"pk": sample_participant.pk})
                ),
                "username": sample_participant.username,
                "event": sample_participant.event,
            },
            {
                "id": sample_participant_2.id,
                "url": r"http://testserver{}".format(
                    reverse(
                        "participant-detail", kwargs={"pk": sample_participant_2.pk}
                    )
                ),
                "username": sample_participant_2.username,
                "event": sample_participant_2.event,
            },
        ]
    )


@pytest.mark.django_db
def test_get_participant(sample_participant):
    """Request should return proper participant data"""

    client = APIClient()
    response = client.get(
        reverse("participant-detail", kwargs={"pk": sample_participant.pk}),
        format="jason",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "id": sample_participant.id,
        "url": r"http://testserver{}".format(
            reverse("participant-detail", kwargs={"pk": sample_participant.pk})
        ),
        "username": sample_participant.username,
        "event": sample_participant.event,
    }


@pytest.mark.django_db
def test_post_participant():
    """New Participant object should be created"""

    assert Participant.objects.filter(username="new participant").count() == 0
    client = APIClient()
    participant_data = {"username": "new participant"}
    response = client.post(reverse("participant-list"), participant_data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Participant.objects.filter(username="new participant").count() == 1


@pytest.mark.django_db
def test_delete_participant(sample_participant):
    """Participant object should be deleted"""

    assert sample_participant in Participant.objects.filter(
        username=sample_participant.username
    )
    client = APIClient()
    response = client.delete(
        reverse("participant-detail", kwargs={"pk": sample_participant.pk}),
        format="json",
        follow=True,
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert sample_participant not in Participant.objects.filter(
        username=sample_participant.username
    )


@pytest.mark.django_db
def test_put_participant(sample_participant):
    """sample_participant should have a changed username"""

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
    client = APIClient()
    response = client.put(
        reverse("participant-detail", kwargs={"pk": sample_participant.pk}),
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
