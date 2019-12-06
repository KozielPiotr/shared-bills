"""Models for bills_app."""

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    User model. Overwrites default model.
    """

    def __str__(self):
        return self.username


class Event(models.Model):
    """Settlement for whole event, eg. kayaks."""
    name = models.CharField(max_length=500, unique=True)
    cashier = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL,
                                related_name="cashier")
    participators = models.ManyToManyField(CustomUser, related_name="participates")

    def __str__(self):
        return self.name


class Receipt(models.Model):
    """Single bill, eg. for car, food, fuel etc."""
    for_what = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    paid_by = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.PROTECT,
                                related_name="paid_for")
    bought_by = models.ManyToManyField(CustomUser, related_name="bought")

    def __str__(self):
        return self.for_what


class Payment(models.Model):
    """Payment from one to another."""
    who_pays = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="paid_cash")
    for_who = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="got_cash")
    event = models.ForeignKey(Event, on_delete=models.PROTECT)

    def __str__(self):
        return "{} to {} ({})".format(self.who_pays, self.for_who, self.event)
