# pylint: disable=too-few-public-methods,missing-class-docstring, no-member
"""
Serializers for bills application.
Id fields left to facilitate frontend work.
"""

from rest_framework.exceptions import ValidationError
from rest_framework.serializers import (
    HiddenField,
    HyperlinkedIdentityField,
    ModelSerializer,
    PrimaryKeyRelatedField,
)
from rest_framework_nested.relations import NestedHyperlinkedIdentityField

from .models import Bill, Event, Participant, Payment


class EventResourceSerializer(ModelSerializer):
    """Base serializer for event related models."""

    event = HiddenField(default=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["event"].default = self.context["view"].get_event()


class ParticipantField(PrimaryKeyRelatedField):
    """Allows to choose only from set of participants related to the event"""

    def get_queryset(self):
        event = self.context["view"].get_event()
        return Participant.objects.filter(event=event)


class ParticipantSerializer(EventResourceSerializer):
    """Serializer for Participant object."""

    url = NestedHyperlinkedIdentityField(
        view_name="participants-detail", parent_lookup_kwargs={"event_pk": "event__pk"}
    )

    class Meta:
        model = Participant
        fields = "__all__"


class ParticipantNestedSerializer(ModelSerializer):
    """Serializer for fully nested Participant object."""

    url = NestedHyperlinkedIdentityField(
        view_name="participants-detail", parent_lookup_kwargs={"event_pk": "event__pk"}
    )

    class Meta:
        model = Participant
        exclude = ["event"]


class BillSerializer(EventResourceSerializer):
    """Serializer for Bill object."""

    url = NestedHyperlinkedIdentityField(
        view_name="bills-detail", parent_lookup_kwargs={"event_pk": "event__pk"}
    )
    participants = ParticipantField(many=True, validators=[])

    class Meta:
        model = Bill
        fields = "__all__"


class BillNestedSerializer(ModelSerializer):
    """Serializer for fully nested Bill object."""

    url = NestedHyperlinkedIdentityField(
        view_name="bills-detail", parent_lookup_kwargs={"event_pk": "event__pk"}
    )
    participants = ParticipantField(many=True)

    class Meta:
        model = Bill
        fields = "__all__"


class PaymentSerializer(EventResourceSerializer):
    """Serializer for Payment object."""

    url = NestedHyperlinkedIdentityField(
        view_name="payments-detail", parent_lookup_kwargs={"event_pk": "event__pk"}
    )
    issuer = ParticipantField()
    acquirer = ParticipantField()

    class Meta:
        model = Payment
        fields = "__all__"


class PaymentNestedSerializer(ModelSerializer):
    """Serializer for fully nested Payment object."""

    url = NestedHyperlinkedIdentityField(
        view_name="payments-detail", parent_lookup_kwargs={"event_pk": "event__pk"}
    )
    issuer = ParticipantField()
    acquirer = ParticipantField()

    class Meta:
        model = Payment
        fields = "__all__"


class EventSerializer(ModelSerializer):
    """Serializer for Event object."""

    user = HiddenField(default=None)
    paymaster = ParticipantNestedSerializer(required=False)

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user"].default = self.context["request"].user

    def create(self, validated_data):
        print(validated_data)
        paymaster_data = None
        if "paymaster" in validated_data:
            paymaster_data = validated_data.pop("paymaster")

        event = Event.objects.create(**validated_data)

        if paymaster_data:
            event.paymaster = Participant.objects.create(event=event, **paymaster_data)
            event.save()
        return event


class EventRetrieveSerializer(EventSerializer):
    """Serializer for detail view of event."""

    participants = ParticipantNestedSerializer(many=True, read_only=True)
    bills = BillNestedSerializer(many=True, read_only=True)
    payments = PaymentNestedSerializer(many=True, read_only=True)
