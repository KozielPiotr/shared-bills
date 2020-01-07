# pylint: disable=no-member, bad-continuation
"""Tests for bills event views."""

import json
import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from bills.models import Event


@pytest.mark.django_db
def test_get_events(
    sample_event, sample_event_2, sample_participant, sample_bill, sample_payment
):
    """Request should return all Event objects data."""

    client = APIClient()
    sample_event.participants.add(sample_participant)
    sample_event.bills.add(sample_bill)
    sample_event.payments.add(sample_payment)
    sample_event.save()
    response = client.get(reverse("bills:events-list"), format="json")
    assert response.status_code == status.HTTP_200_OK
    assert json.dumps(response.data) == json.dumps(
        [
            {
                "id": sample_event.pk,
                "url": r"http://testserver{}".format(
                    reverse("bills:events-detail", kwargs={"pk": sample_event.pk})
                ),
                "participants_url": r"http://testserver{}".format(
                    reverse(
                        "bills:participants-list", kwargs={"event_pk": sample_event.pk}
                    )
                ),
                "bills_url": r"http://testserver{}".format(
                    reverse("bills:bills-list", kwargs={"event_pk": sample_event.pk})
                ),
                "payments_url": r"http://testserver{}".format(
                    reverse("bills:payments-list", kwargs={"event_pk": sample_event.pk})
                ),
                "name": sample_event.name,
                "paymaster": sample_event.paymaster,
            },
            {
                "id": sample_event_2.pk,
                "url": "http://testserver{}".format(
                    reverse("bills:events-detail", kwargs={"pk": sample_event_2.pk})
                ),
                "participants_url": "http://testserver{}".format(
                    reverse(
                        "bills:participants-list",
                        kwargs={"event_pk": sample_event_2.pk},
                    )
                ),
                "bills_url": "http://testserver{}".format(
                    reverse("bills:bills-list", kwargs={"event_pk": sample_event_2.pk})
                ),
                "payments_url": "http://testserver{}".format(
                    reverse(
                        "bills:payments-list", kwargs={"event_pk": sample_event_2.pk}
                    )
                ),
                "name": sample_event_2.name,
                "paymaster": sample_event_2.paymaster,
            },
        ]
    )


@pytest.mark.django_db
def test_get_event(
    sample_event, sample_participant, sample_bill, sample_payment, sample_user
):
    """Request should return proper event data."""

    client = APIClient()
    sample_event.participants.add(sample_participant)
    sample_event.bills.add(sample_bill)
    sample_event.payments.add(sample_payment)
    sample_event.save()
    response = client.get(
        reverse("bills:events-detail", kwargs={"pk": sample_event.pk}), format="json"
    )
    assert response.status_code == status.HTTP_200_OK
    assert json.dumps(response.data) == json.dumps(
        {
            "id": sample_event.pk,
            "url": "http://testserver{}".format(
                reverse("bills:events-detail", kwargs={"pk": sample_event.pk})
            ),
            "participants_url": "http://testserver{}".format(
                reverse("bills:participants-list", kwargs={"event_pk": sample_event.pk})
            ),
            "bills_url": "http://testserver{}".format(
                reverse("bills:bills-list", kwargs={"event_pk": sample_event.pk})
            ),
            "payments_url": "http://testserver{}".format(
                reverse("bills:payments-list", kwargs={"event_pk": sample_event.pk})
            ),
            "participants": [
                {
                    "id": sample_participant.pk,
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
                    "event": sample_event.pk,
                    "user": sample_user.pk,
                }
            ],
            "bills": [
                {
                    "id": sample_bill.pk,
                    "url": r"http://testserver{}".format(
                        reverse(
                            "bills:bills-detail",
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
                            "bills:payments-detail",
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
        }
    )


@pytest.mark.django_db
def test_post_event():
    """New Event object should be created."""

    assert Event.objects.filter(name="new test event").count() == 0
    client = APIClient()
    event_data = {"name": "new test event"}
    response = client.post(reverse("bills:events-list"), event_data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert Event.objects.filter(name="new test event").count() == 1


@pytest.mark.django_db
def test_delete_event(sample_event):
    """Event object should be deleted"""

    assert sample_event in Event.objects.filter(name=sample_event.name)
    client = APIClient()
    response = client.delete(
        reverse("bills:events-detail", kwargs={"pk": sample_event.pk}),
        format="json",
        follow=True,
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert sample_event not in Event.objects.filter(name=sample_event.name)


@pytest.mark.django_db
def test_put_event(sample_event):
    """sample_event should have a changed name."""

    changed_event_data = {"name": "new test event"}
    assert sample_event in Event.objects.filter(name=sample_event.name)
    assert Event.objects.filter(name=changed_event_data["name"]).count() == 0
    client = APIClient()
    response = client.put(
        reverse("bills:events-detail", kwargs={"pk": sample_event.pk}),
        changed_event_data,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    assert sample_event not in Event.objects.filter(name=sample_event.name)
    assert Event.objects.filter(name=changed_event_data["name"]).count() == 1
