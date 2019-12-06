"""Settings for admin."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Event, Payment, Receipt


class CustomUserAdmin(UserAdmin):
    """Admin view for Custom User."""
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username"]


class EventAdmin(admin.ModelAdmin):
    """Admin view for Event."""
    model = Event
    list_display = ["name", "cashier"]


class ReceiptAdmin(admin.ModelAdmin):
    """Admin view for Receipt."""
    model = Receipt
    list_display = ["for_what", "amount", "event"]


class PaymentAdmin(admin.ModelAdmin):
    """Admin view for Payment."""
    model = Payment
    fields = ("who_pays", "for_who", "event")


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Receipt, ReceiptAdmin)
admin.site.register(Payment, PaymentAdmin)
