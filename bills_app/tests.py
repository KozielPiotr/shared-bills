# pylint: disable=no-member
"""Tests for bills_app."""

# from django.test import TestCase

from .models import CustomUser, Event, Receipt


def create_customuser(username):
    """
    Creates new CustomUser object.
    :param username: given name
    :return: new CustomUser object
    """
    return CustomUser.objects.create(username=username)


def create_event(name):
    """
    Creates new Event object.
    :param name: given name
    :return: new Event object
    """
    return Event.objects.create(name=name)


def create_receipt(for_what, amount, event, paid_by, bought_by):
    """
    Creates new Receipt object.
    :param for_what: string with data for representation
    :param amount: decimal with price
    :param event: Event object to make relationship
    :param paid_by: CustomUser object to make relationship
    :param bought_by: list of CustomUser objects to make relationship
    :return: new Receipt object
    """
    receipt = Receipt.objects.create(
        for_what=for_what,
        amount=amount,
        event=event,
        paid_by=paid_by
    )
    receipt.bought_by.add(bought_by)
    return receipt
