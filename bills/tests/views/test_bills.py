# pylint: disable=no-member
"""Tests for bills bills views"""

import json
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from bills.models import Bill


@pytest.mark.django_db
def test_get_bills(sample_event, sample_bill, sample_bill_2, sample_participant):
    """Request should return all Bill objects data related to sample_event"""

    client = APIClient()
    sample_bill.participants.add(sample_participant)
    sample_bill.save()
    sample_event.bills.add(sample_bill)
    sample_event.bills.add(sample_bill_2)
    sample_event.save()

    response = client.get(
        reverse("bills-list", kwargs={"event_pk": sample_event.pk}), format="json"
    )
    assert response.status_code == status.HTTP_200_OK
    assert json.dumps(response.data) == json.dumps(
        [
            {
                "id": sample_bill.id,
                "url": r"http://testserver{}".format(
                    reverse(
                        "bills-detail",
                        kwargs={"event_pk": sample_event.pk, "pk": sample_bill.pk},
                    )
                ),
                "title": sample_bill.title,
                "amount_currency": "PLN",
                "amount": "0.00",
                "payer": sample_bill.payer,
                "participants": [sample_participant.id],
            },
            {
                "id": sample_bill_2.id,
                "url": r"http://testserver{}".format(
                    reverse(
                        "bills-detail",
                        kwargs={"event_pk": sample_event.pk, "pk": sample_bill_2.pk},
                    )
                ),
                "title": sample_bill_2.title,
                "amount_currency": "PLN",
                "amount": "0.00",
                "payer": sample_bill_2.payer,
                "participants": [],
            },
        ]
    )


@pytest.mark.django_db
def test_get_bill(sample_event, sample_bill, sample_participant):
    """Request should return proper bill data"""

    client = APIClient()
    sample_bill.participants.add(sample_participant)
    sample_bill.save()
    sample_event.bills.add(sample_bill)
    sample_event.save()

    response = client.get(
        reverse(
            "bills-detail", kwargs={"event_pk": sample_event.pk, "pk": sample_bill.pk}
        ),
        format="jason",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data == {
        "id": sample_bill.id,
        "url": r"http://testserver{}".format(
            reverse(
                "bills-detail",
                kwargs={"event_pk": sample_event.pk, "pk": sample_bill.pk},
            )
        ),
        "title": sample_bill.title,
        "amount_currency": "PLN",
        "amount": "0.00",
        "payer": sample_bill.payer,
        "participants": [sample_participant.id],
    }


@pytest.mark.django_db
def test_post_bill(sample_event, sample_participant):
    """New Bill object should be created"""

    client = APIClient()

    assert Bill.objects.filter(title="new bill").count() == 0
    bill_data = {"title": "new bill", "participants": [sample_participant.id]}
    response = client.post(
        reverse("bills-list", kwargs={"event_pk": sample_event.pk}),
        bill_data,
        format="json",
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert (
        Bill.objects.filter(title="new bill", participants=sample_participant).count()
        == 1
    )


@pytest.mark.django_db
def test_delete_bill(sample_event, sample_bill):
    """Bill object should be deleted"""

    client = APIClient()
    sample_event.bills.add(sample_bill)
    sample_event.save()

    assert sample_bill in Bill.objects.filter(title=sample_bill.title)
    response = client.delete(
        reverse(
            "bills-detail", kwargs={"event_pk": sample_event.pk, "pk": sample_bill.pk}
        ),
        format="json",
        follow=True,
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert sample_bill not in Bill.objects.filter(title=sample_bill.title)


@pytest.mark.django_db
def test_patch_bill(sample_event, sample_bill):
    """sample_bill should have a changed title"""

    client = APIClient()
    sample_event.bills.add(sample_bill)
    sample_event.save()

    changed_bill_data = {"title": "new test bill"}
    assert sample_bill in Bill.objects.filter(title=sample_bill.title)
    assert Bill.objects.filter(title=changed_bill_data["title"]).count() == 0
    response = client.patch(
        reverse(
            "bills-detail", kwargs={"event_pk": sample_event.pk, "pk": sample_bill.pk}
        ),
        changed_bill_data,
        format="json",
    )
    assert response.status_code == status.HTTP_200_OK
    assert sample_bill not in Bill.objects.filter(title=sample_bill.title)
    assert Bill.objects.filter(title=changed_bill_data["title"]).count() == 1
