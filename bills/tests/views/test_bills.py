# pylint: disable=no-member, bad-continuation
"""Tests for bills bills views."""

import json
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from bills.models import Bill
from bills.tests.utils import auth_client


@pytest.mark.django_db
def test_get_bills(
    sample_event, sample_bill, sample_bill_2, sample_participant, sample_user
):
    """Request should return all Bill objects data related to sample_event."""

    client = auth_client(APIClient(), sample_user.email, "testpassword")

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
                "participants": [sample_participant.id],
                "title": sample_bill.title,
                "amount_currency": "PLN",
                "amount": "0.00",
                "payer": sample_bill.payer,
            },
            {
                "id": sample_bill_2.id,
                "url": r"http://testserver{}".format(
                    reverse(
                        "bills-detail",
                        kwargs={"event_pk": sample_event.pk, "pk": sample_bill_2.pk},
                    )
                ),
                "participants": [],
                "title": sample_bill_2.title,
                "amount_currency": "PLN",
                "amount": "0.00",
                "payer": sample_bill_2.payer,
            },
        ]
    )


@pytest.mark.django_db
def test_get_bills_fail_logged_out(sample_event):
    """Only logged users should have access to this view."""

    client = APIClient()

    response = client.get(
        reverse("bills-list", kwargs={"event_pk": sample_event.pk}), format="json"
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_get_bills_fail_other_user(sample_event, sample_bill, sample_user_2):
    """User should not have access to other user's event's bills."""

    client = auth_client(APIClient(), sample_user_2.email, "testpassword")

    sample_event.bills.add(sample_bill)
    sample_event.save()

    response = client.get(
        reverse("bills-list", kwargs={"event_pk": sample_event.pk}), format="jason"
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_get_bill(sample_event, sample_bill, sample_participant, sample_user):
    """Request should return proper bill data."""

    client = auth_client(APIClient(), sample_user.email, "testpassword")

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
def test_get_bill_fail_other_user(sample_event, sample_bill, sample_user_2):
    """User should not have access to other user's event's bills."""

    client = auth_client(APIClient(), sample_user_2.email, "testpassword")

    sample_event.bills.add(sample_bill)
    sample_event.save()

    response = client.get(
        reverse(
            "bills-detail", kwargs={"event_pk": sample_event.pk, "pk": sample_bill.pk}
        ),
        format="jason",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_get_bill_fail_logged_out(sample_event, sample_bill):
    """Only logged users should have access to this view."""

    client = APIClient()

    sample_event.bills.add(sample_bill)
    sample_event.save()

    response = client.get(
        reverse(
            "bills-detail", kwargs={"event_pk": sample_event.pk, "pk": sample_bill.pk}
        ),
        format="jason",
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_post_bill(sample_event, sample_participant, sample_user):
    """New Bill object should be created."""

    client = auth_client(APIClient(), sample_user.email, "testpassword")

    sample_event.participants.add(sample_participant)
    sample_event.save()

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
def test_post_bill_fail_logged_out(sample_event, sample_participant):
    """Only logged users should have access to this view."""

    client = APIClient()

    sample_event.participants.add(sample_participant)
    sample_event.save()

    bill_data = {"title": "new bill", "participants": [sample_participant.id]}
    response = client.post(
        reverse("bills-list", kwargs={"event_pk": sample_event.pk}),
        bill_data,
        format="json",
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_delete_bill(sample_event, sample_bill, sample_user):
    """Bill object should be deleted."""

    client = auth_client(APIClient(), sample_user.email, "testpassword")

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
def test_delete_bill_fail_logged_out(sample_event, sample_bill):
    """Only logged users should have access to this view."""

    client = APIClient()

    sample_event.bills.add(sample_bill)
    sample_event.save()

    response = client.delete(
        reverse(
            "bills-detail", kwargs={"event_pk": sample_event.pk, "pk": sample_bill.pk}
        ),
        format="json",
        follow=True,
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_patch_bill(sample_event, sample_bill, sample_user):
    """sample_bill should have a changed title."""

    client = auth_client(APIClient(), sample_user.email, "testpassword")

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


@pytest.mark.django_db
def test_patch_bill_fail_logged_out(sample_event, sample_bill):
    """Only logged users should have access to this view."""

    client = APIClient()

    sample_event.bills.add(sample_bill)
    sample_event.save()

    changed_bill_data = {"title": "new test bill"}
    response = client.patch(
        reverse(
            "bills-detail", kwargs={"event_pk": sample_event.pk, "pk": sample_bill.pk}
        ),
        changed_bill_data,
        format="json",
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
