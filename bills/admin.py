# pylint: disable=too-few-public-methods
"""Settings for admin."""

from django.contrib import admin

from .models import Event, Participant, Payment, Bill


class ParticipantAdmin(admin.ModelAdmin):
    """Admin view for Custom User."""

    model = Participant
    list_display = ["username"]


class EventAdmin(admin.ModelAdmin):
    """Admin view for Event."""

    model = Event
    list_display = ["name", "paymaster"]


class BillAdmin(admin.ModelAdmin):
    """Admin view for Bill."""

    model = Bill
    list_display = ["title", "amount", "event"]


class PaymentAdmin(admin.ModelAdmin):
    """Admin view for Payment."""

    model = Payment
    list_display = ["title", "issuer", "acquirer", "event", "amount"]


admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(Payment, PaymentAdmin)
