# pylint: disable=no-member
"""Tests for bills application."""

# from django.test import TestCase
from djmoney.money import Money

from .models import Participant, Event, Bill


def create_participant(username):
    """
    Creates new Participant object.
    :param username: given name
    :return: new Participant object
    """
    return Participant.objects.create(username=username)


def create_event(name):
    """
    Creates new Event object.
    :param name: given name
    :return: new Event object
    """
    return Event.objects.create(name=name)


def create_bill(title, amount, event, payer, participants):
    """
    Creates new Bill object.
    :param title: string with data for representation
    :param amount: decimal with price
    :param event: Event object to make relationship
    :param payer: Participant object to make relationship
    :param participants: list of Participant objects to make relationship
    :return: new Bill object
    """
    bill = Bill.objects.create(
        title=title, balance=Money(amount, "PLN"), event=event, payer=payer
    )
    bill.participants.add(participants)
    return bill
