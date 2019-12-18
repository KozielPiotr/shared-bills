# pylint: disable=too-few-public-methods,missing-class-docstring
"""
Serializers for bills application.
Id fields left to facilitate frontend work.
"""

from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer

from .models import Bill, Event, Participant, Payment


class EventSerializer(ModelSerializer):
    """Serializer for Event object"""

    url = HyperlinkedIdentityField(view_name="event-detail")
    participants_url = HyperlinkedIdentityField(
        view_name="event-participants-list", lookup_url_kwarg="event_pk"
    )
    bills_url = HyperlinkedIdentityField(
        view_name="event-bills-list", lookup_url_kwarg="event_pk"
    )
    payments_url = HyperlinkedIdentityField(
        view_name="event-payments-list", lookup_url_kwarg="event_pk"
    )

    class Meta:
        model = Event
        fields = "__all__"


class ParticipantSerializer(ModelSerializer):
    """Serializer for Participant object"""

    url = HyperlinkedIdentityField(view_name="participant-detail")

    class Meta:
        model = Participant
        fields = "__all__"


class BillSerializer(ModelSerializer):
    """Serializer for Bill object"""

    url = HyperlinkedIdentityField(view_name="bill-detail")

    class Meta:
        model = Bill
        fields = "__all__"


class PaymentSerializer(ModelSerializer):
    """Serializer for Payment object"""

    url = HyperlinkedIdentityField(view_name="payment-detail")

    class Meta:
        model = Payment
        fields = "__all__"
