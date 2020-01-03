# pylint: disable=too-few-public-methods,missing-class-docstring
"""
Serializers for bills application.
Id fields left to facilitate frontend work.
"""

from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    HiddenField,
)
from rest_framework_nested.relations import NestedHyperlinkedIdentityField
from .models import Bill, Event, Participant, Payment


class EventSerializer(ModelSerializer):
    """Serializer for Event object"""

    url = HyperlinkedIdentityField(view_name="events-detail")
    participants_url = HyperlinkedIdentityField(
        view_name="participants-list", lookup_url_kwarg="event_pk"
    )
    bills_url = HyperlinkedIdentityField(
        view_name="bills-list", lookup_url_kwarg="event_pk"
    )
    payments_url = HyperlinkedIdentityField(
        view_name="payments-list", lookup_url_kwarg="event_pk"
    )

    class Meta:
        model = Event
        fields = "__all__"


class ParticipantSerializer(ModelSerializer):
    """Serializer for Participant object"""

    url = NestedHyperlinkedIdentityField(
        view_name="participants-detail", parent_lookup_kwargs={"event_pk": "event__pk"}
    )
    event = HiddenField(default=None)

    class Meta:
        model = Participant
        fields = "__all__"


class BillSerializer(ModelSerializer):
    """Serializer for Bill object"""

    url = NestedHyperlinkedIdentityField(
        view_name="bills-detail", parent_lookup_kwargs={"event_pk": "event__pk"}
    )
    event = HiddenField(default=None)

    class Meta:
        model = Bill
        fields = "__all__"


class PaymentSerializer(ModelSerializer):
    """Serializer for Payment object"""

    url = NestedHyperlinkedIdentityField(
        view_name="payments-detail", parent_lookup_kwargs={"event_pk": "event__pk"}
    )
    event = HiddenField(default=None)

    class Meta:
        model = Payment
        fields = "__all__"
