# pylint: disable=too-few-public-methods,missing-class-docstring
"""Models for bills application."""

from django.db import models
from djmoney.models.fields import MoneyField

from accounts.models import User


class Participant(models.Model):
    """Model for event's participants."""

    event = models.ForeignKey(
        "Event",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="participants",
    )
    username = models.CharField(max_length=100)

    class Meta:
        unique_together = [["event", "username"]]

    def __str__(self):
        return self.username


class Event(models.Model):
    """Settlement for whole event, eg. kayaks."""

    name = models.CharField(max_length=500, unique=True)
    paymaster = models.ForeignKey(
        Participant,
        default=None,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="paymaster",
    )
    user = models.ForeignKey(
        User,
        default=None,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="events",
    )

    def __str__(self):
        return self.name


class Bill(models.Model):
    """Single bill, eg. for car, food, fuel etc."""

    title = models.CharField(max_length=100)
    amount = MoneyField(
        max_digits=7, decimal_places=2, default_currency="PLN", default=0
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="bills")
    payer = models.ForeignKey(
        Participant,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="payer",
    )
    participants = models.ManyToManyField(Participant, related_name="bills")

    def __str__(self):
        return self.title


class Payment(models.Model):
    """Payment from one to another."""

    title = models.CharField(max_length=500)
    issuer = models.ForeignKey(
        Participant, on_delete=models.PROTECT, related_name="paid"
    )
    acquirer = models.ForeignKey(
        Participant, on_delete=models.PROTECT, related_name="acquired"
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="payments")
    amount = MoneyField(
        max_digits=7, decimal_places=2, default_currency="PLN", default=0
    )

    def __str__(self):
        return "{} to {} for {} ({})".format(
            self.issuer, self.acquirer, self.title, self.event
        )
