# pylint: disable=no-member, bad-continuation
"""Tests for bills payments views."""

import json
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from bills.models import Payment


@pytest.mark.django_db
def test_get_payments(
    sample_event,
    sample_payment,
    sample_payment_2,
    sample_participant,
    sample_participant_2,
):
    """Request should return all Payment objects data related to sample_event."""

    client = APIClient()
    sample_payment.issuer = sample_participant
    sample_payment.acquirer = sample_participant_2
    sample_payment.save()
    sample_event.payments.add(sample_payment)
    sample_event.payments.add(sample_payment_2)
    sample_event.save()

    response = client.get(
        reverse("payments-list", kwargs={"event_pk": sample_event.pk}), format="json"
    )
    assert response.status_code == status.HTTP_200_OK
    assert json.dumps(response.data) == json.dumps(
        [
            {
                "id": sample_payment.id,
                "url": r"http://testserver{}".format(
                    reverse(
                        "payments-detail",
                        kwargs={"event_pk": sample_event.pk, "pk": sample_payment.pk},
                    )
                ),
                "issuer": sample_payment.issuer.id,
                "acquirer": sample_payment.acquirer.id,
                "title": sample_payment.title,
                "amount_currency": "PLN",
                "amount": "0.00",
            },
            {
                "id": sample_payment_2.id,
                "url": r"http://testserver{}".format(
                    reverse(
                        "payments-detail",
                        kwargs={"event_pk": sample_event.pk, "pk": sample_payment_2.pk},
                    )
                ),
                "issuer": sample_payment_2.issuer.id,
                "acquirer": sample_payment_2.acquirer.id,
                "title": sample_payment_2.title,
                "amount_currency": "PLN",
                "amount": "0.00",
            },
        ]
    )


@pytest.mark.django_db
def test_get_payment(sample_event, sample_payment, sample_participant):
    """Request should return all Payment objects data related to sample_event."""

    client = APIClient()
    sample_payment.issuer = sample_participant
    sample_payment.save()
    sample_event.payments.add(sample_payment)
    sample_event.save()

    response = client.get(
        reverse(
            "payments-detail",
            kwargs={"event_pk": sample_event.pk, "pk": sample_payment.pk},
        ),
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    assert json.dumps(response.data) == json.dumps(
        {
            "id": sample_payment.id,
            "url": r"http://testserver{}".format(
                reverse(
                    "payments-detail",
                    kwargs={"event_pk": sample_event.pk, "pk": sample_payment.pk},
                )
            ),
            "issuer": sample_payment.issuer.id,
            "acquirer": sample_payment.acquirer.id,
            "title": sample_payment.title,
            "amount_currency": "PLN",
            "amount": "0.00",
        }
    )


@pytest.mark.django_db
def test_post_payment(sample_event, sample_participant, sample_participant_2):
    """New Payment object should be created."""

    client = APIClient()
    sample_event.participants.add(sample_participant, sample_participant_2)
    sample_event.save()

    assert Payment.objects.filter(title="new payment").count() == 0
    bill_data = {
        "title": "new payment",
        "issuer": sample_participant.id,
        "acquirer": sample_participant_2.id,
    }
    response = client.post(
        reverse("payments-list", kwargs={"event_pk": sample_event.pk}),
        bill_data,
        format="json",
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert Payment.objects.filter(title="new payment").count() == 1
    Payment.objects.get(title="new payment").delete()


@pytest.mark.django_db
def test_delete_payment(sample_event, sample_payment):
    """Payment object should be deleted."""

    client = APIClient()
    sample_event.payments.add(sample_payment)
    sample_event.save()

    assert sample_payment in Payment.objects.filter(title=sample_payment.title)
    response = client.delete(
        reverse(
            "payments-detail",
            kwargs={"event_pk": sample_event.pk, "pk": sample_payment.pk},
        ),
        format="json",
        follow=True,
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert sample_payment not in Payment.objects.filter(title=sample_payment.title)


@pytest.mark.django_db
def test_patch_payment(sample_event, sample_payment):
    """sample_payment should have a changed title."""

    client = APIClient()
    sample_event.payments.add(sample_payment)
    sample_event.save()

    changed_payment_data = {"title": "new test bill"}
    assert sample_payment in Payment.objects.filter(title=sample_payment.title)
    assert Payment.objects.filter(title=changed_payment_data["title"]).count() == 0
    response = client.patch(
        reverse(
            "payments-detail",
            kwargs={"event_pk": sample_event.pk, "pk": sample_payment.pk},
        ),
        changed_payment_data,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    assert sample_payment not in Payment.objects.filter(title=sample_payment.title)
    assert Payment.objects.filter(title=changed_payment_data["title"]).count() == 1
