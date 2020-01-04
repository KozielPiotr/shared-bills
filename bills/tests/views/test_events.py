# pylint: disable=no-member
"""Tests for bills event views."""

import json
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from bills.models import Event


@pytest.mark.django_db
def test_get_events(sample_event, sample_event_2):
    """Request should return all Event objects data"""

    client = APIClient()
    response = client.get(reverse("events-list"), format="json")
    assert response.status_code == status.HTTP_200_OK
    assert json.dumps(response.data) == json.dumps(
        [
            {
                "id": sample_event.id,
                "url": r"http://testserver{}".format(
                    reverse("events-detail", kwargs={"pk": sample_event.pk})
                ),
                "participants_url": r"http://testserver{}".format(
                    reverse("participants-list", kwargs={"event_pk": sample_event.pk})
                ),
                "bills_url": r"http://testserver{}".format(
                    reverse("bills-list", kwargs={"event_pk": sample_event.pk})
                ),
                "payments_url": r"http://testserver{}".format(
                    reverse("payments-list", kwargs={"event_pk": sample_event.pk})
                ),
                "name": sample_event.name,
                "paymaster": sample_event.paymaster,
            },
            {
                "id": sample_event_2.id,
                "url": "http://testserver{}".format(
                    reverse("events-detail", kwargs={"pk": sample_event_2.pk})
                ),
                "participants_url": "http://testserver{}".format(
                    reverse("participants-list", kwargs={"event_pk": sample_event_2.pk})
                ),
                "bills_url": "http://testserver{}".format(
                    reverse("bills-list", kwargs={"event_pk": sample_event_2.pk})
                ),
                "payments_url": "http://testserver{}".format(
                    reverse("payments-list", kwargs={"event_pk": sample_event_2.pk})
                ),
                "name": sample_event_2.name,
                "paymaster": sample_event_2.paymaster,
            },
        ]
    )


@pytest.mark.django_db
def test_get_event(sample_event):
    """Request should return proper event data"""

    client = APIClient()
    response = client.get(
        reverse("events-detail", kwargs={"pk": sample_event.pk}), format="json"
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "id": sample_event.id,
        "url": "http://testserver{}".format(
            reverse("events-detail", kwargs={"pk": sample_event.pk})
        ),
        "participants_url": "http://testserver{}".format(
            reverse("participants-list", kwargs={"event_pk": sample_event.pk})
        ),
        "bills_url": "http://testserver{}".format(
            reverse("bills-list", kwargs={"event_pk": sample_event.pk})
        ),
        "payments_url": "http://testserver{}".format(
            reverse("payments-list", kwargs={"event_pk": sample_event.pk})
        ),
        "name": sample_event.name,
        "paymaster": sample_event.paymaster,
    }


@pytest.mark.django_db
def test_post_event():
    """New Event object should be created"""

    assert Event.objects.filter(name="new test event").count() == 0
    client = APIClient()
    event_data = {"name": "new test event"}
    response = client.post(reverse("events-list"), event_data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Event.objects.filter(name="new test event").count() == 1


@pytest.mark.django_db
def test_delete_event(sample_event):
    """Event object should be deleted"""

    assert sample_event in Event.objects.filter(name=sample_event.name)
    client = APIClient()
    response = client.delete(
        reverse("events-detail", kwargs={"pk": sample_event.pk}),
        format="json",
        follow=True,
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert sample_event not in Event.objects.filter(name=sample_event.name)


@pytest.mark.django_db
def test_put_event(sample_event):
    """sample_event should have a changed name"""

    changed_event_data = {"name": "new test event"}
    assert sample_event in Event.objects.filter(name=sample_event.name)
    assert Event.objects.filter(name=changed_event_data["name"]).count() == 0
    client = APIClient()
    response = client.put(
        reverse("events-detail", kwargs={"pk": sample_event.pk}),
        changed_event_data,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    assert sample_event not in Event.objects.filter(name=sample_event.name)
    assert Event.objects.filter(name=changed_event_data["name"]).count() == 1
