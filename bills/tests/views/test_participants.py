# pylint: disable=no-member, bad-continuation
"""Tests for bills participants views"""

import json
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from bills.models import Participant
from bills.tests.utils import auth_client


@pytest.mark.django_db
def test_get_participants(
    sample_event, sample_participant, sample_participant_2, sample_user
):
    """Request should return all Participant objects data related to sample_event"""

    client = auth_client(APIClient(), sample_user.email, "testpassword")

    sample_event.participants.add(sample_participant)
    sample_event.participants.add(sample_participant_2)
    sample_event.save()

    response = client.get(
        reverse("participants-list", kwargs={"event_pk": sample_event.pk}),
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    assert json.dumps(response.data) == json.dumps(
        [
            {
                "id": sample_participant.id,
                "url": r"http://testserver{}".format(
                    reverse(
                        "participants-detail",
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
                        "participants-detail",
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
def test_get_participants_fail_logged_out(sample_event, sample_participant):
    """Only logged users should have access to this view."""

    client = APIClient()

    sample_event.participants.add(sample_participant)
    sample_event.save()

    response = client.get(
        reverse("participants-list", kwargs={"event_pk": sample_event.pk}),
        format="json",
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_get_participants_fail_other_user(
    sample_event, sample_participant, sample_user_2
):
    """User should not have access to other user's event's participants."""

    client = auth_client(APIClient(), sample_user_2.email, "testpassword")

    sample_event.participants.add(sample_participant)
    sample_event.save()

    response = client.get(
        reverse("participants-list", kwargs={"event_pk": sample_event.pk}),
        format="json",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_get_participant(sample_event, sample_participant, sample_user):
    """Request should return proper participant data."""

    client = auth_client(APIClient(), sample_user.email, "testpassword")

    sample_event.participants.add(sample_participant)
    sample_event.save()

    response = client.get(
        reverse(
            "participants-detail",
            kwargs={"event_pk": sample_event.pk, "pk": sample_participant.pk},
        ),
        format="jason",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "id": sample_participant.id,
        "url": r"http://testserver{}".format(
            reverse(
                "participants-detail",
                kwargs={"event_pk": sample_event.pk, "pk": sample_participant.pk},
            )
        ),
        "username": sample_participant.username,
    }


@pytest.mark.django_db
def test_get_participant_fail_logged_out(sample_event, sample_participant):
    """Only logged users should have access to this view."""

    client = APIClient()

    sample_event.participants.add(sample_participant)
    sample_event.save()

    response = client.get(
        reverse(
            "participants-detail",
            kwargs={"event_pk": sample_event.pk, "pk": sample_participant.pk},
        ),
        format="jason",
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_get_participant_fail_other_user(
    sample_event, sample_participant, sample_user_2
):
    """User should not have access to other user's event's participants."""

    client = auth_client(APIClient(), sample_user_2.email, "testpassword")

    sample_event.participants.add(sample_participant)
    sample_event.save()

    response = client.get(
        reverse(
            "participants-detail",
            kwargs={"event_pk": sample_event.pk, "pk": sample_participant.pk},
        ),
        format="jason",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_post_participant(sample_event, sample_user):
    """New Participant object should be created."""

    client = auth_client(APIClient(), sample_user.email, "testpassword")

    assert Participant.objects.filter(username="new participant").count() == 0
    participant_data = {"username": "new participant"}
    response = client.post(
        reverse("participants-list", kwargs={"event_pk": sample_event.pk}),
        participant_data,
        format="json",
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert Participant.objects.filter(username="new participant").count() == 1


@pytest.mark.django_db
def test_post_participant_fail_logged_out(sample_event):
    """Only logged users should have access to this view."""

    client = APIClient()

    participant_data = {"username": "new participant"}
    response = client.post(
        reverse("participants-list", kwargs={"event_pk": sample_event.pk}),
        participant_data,
        format="json",
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_delete_participant(sample_event, sample_participant, sample_user):
    """Participant object should be deleted."""

    client = auth_client(APIClient(), sample_user.email, "testpassword")

    sample_event.participants.add(sample_participant)
    sample_event.save()

    assert sample_participant in Participant.objects.filter(
        username=sample_participant.username
    )
    response = client.delete(
        reverse(
            "participants-detail",
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
def test_delete_participant_fail_logged_out(sample_event, sample_participant):
    """Only logged users should have access to this view."""

    client = APIClient()
    sample_event.participants.add(sample_participant)
    sample_event.save()

    assert sample_participant in Participant.objects.filter(
        username=sample_participant.username
    )
    response = client.delete(
        reverse(
            "participants-detail",
            kwargs={"event_pk": sample_event.pk, "pk": sample_participant.pk},
        ),
        format="json",
        follow=True,
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_patch_participant(sample_event, sample_participant, sample_user):
    """sample_participant should have a changed username."""

    client = auth_client(APIClient(), sample_user.email, "testpassword")

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
            "participants-detail",
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


@pytest.mark.django_db
def test_patch_participant_fail_logged_out(sample_event, sample_participant):
    """Only logged users should have access to this view."""

    client = APIClient()

    sample_event.participants.add(sample_participant)
    sample_event.save()

    changed_participant_data = {"username": "new test participant"}
    response = client.patch(
        reverse(
            "participants-detail",
            kwargs={"event_pk": sample_event.pk, "pk": sample_participant.pk},
        ),
        changed_participant_data,
        format="json",
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
