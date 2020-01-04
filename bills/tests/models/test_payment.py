# pylint: disable=no-member
"""Tests for Payment model."""

import pytest
from django.db.models.deletion import ProtectedError

from bills.models import Payment, Participant


@pytest.mark.django_db
def test_payment_create(sample_payment):
    """sample_participant should be an instance of Participant class"""

    assert isinstance(sample_payment, Payment)


@pytest.mark.django_db
def test_payment_repr(sample_payment):
    """
    sample_payment str representation should be like:
    'issuer' to 'acquirer' for 'title' ('event')
    """

    assert sample_payment.__str__() == "{} to {} for {} ({})".format(
        sample_payment.issuer,
        sample_payment.acquirer,
        sample_payment.title,
        sample_payment.event,
    )


@pytest.mark.django_db
def test_payment_issuer_relationship(sample_payment):
    """sample_payment's issuer should be a Participant object"""

    issuer = sample_payment.issuer
    assert isinstance(issuer, Participant)
    assert sample_payment in issuer.paid.all()


@pytest.mark.django_db
def test_payment_issuer_delete(sample_payment):
    """
    It should not be possible to delete Participant object
    related to sample_payment's issuer field
    """

    issuer = sample_payment.issuer
    with pytest.raises(Exception) as e_info:
        issuer.delete()
    assert e_info.type == ProtectedError


@pytest.mark.django_db
def test_payment_acquirer_relationship(sample_payment):
    """sample_payment's acquirer should be a Participant object"""

    acquirer = sample_payment.acquirer
    assert isinstance(acquirer, Participant)
    assert sample_payment in acquirer.acquired.all()


@pytest.mark.django_db
def test_payment_acquirer_delete(sample_payment):
    """
    It should not be possible to delete Participant object
    related to sample_payment's issuer field
    """

    acquirer = sample_payment.acquirer
    with pytest.raises(Exception) as e_info:
        acquirer.delete()
    assert e_info.type == ProtectedError
