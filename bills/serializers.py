# pylint: disable=too-few-public-methods,missing-class-docstring
"""
Serializers for bills application.
Id fields left to facilitate frontend work.
Nested fields for the same reason.
"""

from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer

from .models import Bill, Event, Participant, Payment


class EventSerializer(ModelSerializer):
    """Serializer for Event object"""

    url = HyperlinkedIdentityField(view_name="event-detail")

    class Meta:
        model = Event
        fields = "__all__"


class ParticipantSerializer(ModelSerializer):
    """Serializer for Participant object"""

    url = HyperlinkedIdentityField(view_name="participant-detail")
    event = EventSerializer(read_only=True, many=False)

    class Meta:
        model = Participant
        fields = "__all__"


class BillSerializer(ModelSerializer):
    """Serializer for Bill object"""

    url = HyperlinkedIdentityField(view_name="bill-detail")
    event = EventSerializer(read_only=True, many=False)

    payer = ParticipantSerializer(read_only=True, many=False)
    participants = ParticipantSerializer(read_only=True, many=True)

    class Meta:
        model = Bill
        fields = "__all__"


class PaymentSerializer(ModelSerializer):
    """Serializer for Payment object"""

    url = HyperlinkedIdentityField(view_name="payment-detail")
    issuer = ParticipantSerializer(read_only=True, many=False)
    acquirer = ParticipantSerializer(read_only=True, many=False)
    event = EventSerializer(read_only=True, many=False)

    class Meta:
        model = Payment
        fields = "__all__"
