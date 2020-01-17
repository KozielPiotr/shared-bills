# pylint: disable=no-member, bad-continuation, too-many-arguments, unused-argument
"""Tests for bills event views."""

import json
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from bills.models import Event
from bills.tests.utils import auth_client


@pytest.mark.django_db
def test_get_events(
    sample_event,
    sample_event_2,
    sample_participant,
    sample_bill,
    sample_payment,
    sample_user,
):
    """
    Request should return all related to sample_user Event objects data.
    Sample_event_2 data should not be returned, as it's not event related to logged user.
    """

    client = auth_client(APIClient(), sample_user.email, "testpassword")

    sample_event.participants.add(sample_participant)
    sample_event.bills.add(sample_bill)
    sample_event.payments.add(sample_payment)
    sample_event.save()
    response = client.get(reverse("events-list"), format="json")
    assert response.status_code == status.HTTP_200_OK
    assert json.dumps(response.data) == json.dumps(
        [
            {
                "id": sample_event.pk,
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
                "user": sample_user.pk,
            }
        ]
    )


@pytest.mark.django_db
def test_get_events_fail_logged_out():
    """Only logged users should have access to this view."""

    client = APIClient()

    response = client.get(reverse("events-list"), format="json")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_get_event(
    sample_event, sample_participant, sample_bill, sample_payment, sample_user
):
    """Request should return proper event data."""

    client = auth_client(APIClient(), sample_user.email, "testpassword")

    sample_event.participants.add(sample_participant)
    sample_event.bills.add(sample_bill)
    sample_event.payments.add(sample_payment)
    sample_event.save()
    response = client.get(
        reverse("events-detail", kwargs={"pk": sample_event.pk}), format="json"
    )
    assert response.status_code == status.HTTP_200_OK
    assert json.dumps(response.data) == json.dumps(
        {
            "id": sample_event.pk,
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
            "participants": [
                {
                    "id": sample_participant.pk,
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
                    "event": sample_event.pk,
                }
            ],
            "bills": [
                {
                    "id": sample_bill.pk,
                    "url": r"http://testserver{}".format(
                        reverse(
                            "bills-detail",
                            kwargs={"event_pk": sample_event.pk, "pk": sample_bill.pk},
                        )
                    ),
                    "participants": [],
                    "title": sample_bill.title,
                    "amount_currency": "PLN",
                    "amount": "0.00",
                    "event": sample_event.pk,
                    "payer": sample_bill.payer,
                }
            ],
            "payments": [
                {
                    "id": sample_payment.pk,
                    "url": r"http://testserver{}".format(
                        reverse(
                            "payments-detail",
                            kwargs={
                                "event_pk": sample_event.pk,
                                "pk": sample_payment.pk,
                            },
                        )
                    ),
                    "issuer": sample_payment.issuer.pk,
                    "acquirer": sample_payment.acquirer.pk,
                    "title": sample_payment.title,
                    "amount_currency": "PLN",
                    "amount": "0.00",
                    "event": sample_event.pk,
                }
            ],
            "name": sample_event.name,
            "paymaster": sample_event.paymaster,
            "user": sample_user.pk,
        }
    )


@pytest.mark.django_db
def test_get_event_fail_logged_out(sample_event):
    """Only logged users should have access to this view."""

    client = APIClient()

    response = client.get(
        reverse("events-detail", kwargs={"pk": sample_event.pk}), format="json"
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_get_event_fail_other_user_event(sample_event_2, sample_user):
    """User should not have access to other user's events."""

    client = auth_client(APIClient(), sample_user.email, "testpassword")

    response = client.get(
        reverse("events-detail", kwargs={"pk": sample_event_2.pk}), format="json"
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_post_event(sample_user):
    """New Event object should be created."""

    client = auth_client(APIClient(), sample_user.email, "testpassword")

    assert Event.objects.filter(name="new test event").count() == 0

    event_data = {"name": "new test event", "user": sample_user.id}
    response = client.post(reverse("events-list"), event_data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Event.objects.filter(name="new test event").count() == 1


@pytest.mark.django_db
def test_post_event_fail_logged_out(sample_user):
    """Only logged users should have access to this view."""

    client = APIClient()

    event_data = {"name": "new test event", "user": sample_user.id}
    response = client.post(reverse("events-list"), event_data, format="json")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_delete_event(sample_event, sample_user):
    """Event object should be deleted"""

    client = auth_client(APIClient(), sample_user.email, "testpassword")

    assert sample_event in Event.objects.filter(name=sample_event.name)
    response = client.delete(
        reverse("events-detail", kwargs={"pk": sample_event.pk}),
        format="json",
        follow=True,
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert sample_event not in Event.objects.filter(name=sample_event.name)


@pytest.mark.django_db
def test_delete_event_fail_logged_out():
    """Only logged users should have access to this view."""

    client = APIClient()

    response = client.delete(reverse("events-list"), format="json")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_put_event(sample_event, sample_user):
    """sample_event should have a changed name."""

    client = auth_client(APIClient(), sample_user.email, "testpassword")

    changed_event_data = {"name": "new test event", "user": sample_user.id}
    assert sample_event in Event.objects.filter(name=sample_event.name)
    assert Event.objects.filter(name=changed_event_data["name"]).count() == 0
    response = client.put(
        reverse("events-detail", kwargs={"pk": sample_event.pk}),
        changed_event_data,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    assert sample_event not in Event.objects.filter(name=sample_event.name)
    assert Event.objects.filter(name=changed_event_data["name"]).count() == 1


@pytest.mark.django_db
def test_put_event_fail_logged_out(sample_event, sample_user):
    """sample_event should have a changed name."""

    client = APIClient()

    changed_event_data = {"name": "new test event", "user": sample_user.id}
    response = client.put(
        reverse("events-detail", kwargs={"pk": sample_event.pk}),
        changed_event_data,
        format="json",
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
