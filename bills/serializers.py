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


class EventResourceSerializer(ModelSerializer):
    """Base serializer for event related models"""

    event = HiddenField(default=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["event"].default = self.context["view"].get_event()


class ParticipantSerializer(EventResourceSerializer):
    """Serializer for Participant object"""

    url = NestedHyperlinkedIdentityField(
        view_name="participants-detail", parent_lookup_kwargs={"event_pk": "event__pk"}
    )

    class Meta:
        model = Participant
        fields = "__all__"


class BillSerializer(EventResourceSerializer):
    """Serializer for Bill object"""

    url = NestedHyperlinkedIdentityField(
        view_name="bills-detail", parent_lookup_kwargs={"event_pk": "event__pk"}
    )

    class Meta:
        model = Bill
        fields = "__all__"


class PaymentSerializer(EventResourceSerializer):
    """Serializer for Payment object"""

    url = NestedHyperlinkedIdentityField(
        view_name="payments-detail", parent_lookup_kwargs={"event_pk": "event__pk"}
    )

    class Meta:
        model = Payment
        fields = "__all__"
