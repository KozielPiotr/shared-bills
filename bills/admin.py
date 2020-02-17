# pylint: disable=too-few-public-methods
"""Settings for admin."""

from django.contrib import admin

from .models import Event, Participant, Payment, Bill


class ParticipantAdmin(admin.ModelAdmin):
    """Admin view for Participant."""

    model = Participant
    list_display = ["username", "event"]
    list_filter = ["event"]


class EventAdmin(admin.ModelAdmin):
    """Admin view for Event."""

    model = Event
    list_display = ["name", "user"]
    list_filter = ["user"]


class BillAdmin(admin.ModelAdmin):
    """Admin view for Bill."""

    model = Bill
    list_display = ["event", "title", "amount", "payer"]
    list_filter = ["event"]


class PaymentAdmin(admin.ModelAdmin):
    """Admin view for Payment."""

    model = Payment
    list_display = ["event", "title", "amount", "issuer", "acquirer"]
    list_filter = ["event"]


admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Bill, BillAdmin)
admin.site.register(Payment, PaymentAdmin)
