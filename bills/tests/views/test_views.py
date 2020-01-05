"""Tests for bills viewsets creators"""

from bills.models import Event
from bills.serializers import EventSerializer
from bills.views import create_nested_viewset


def test_create_nested_viewset_classname():
    """Name of created class should be the same as model's name"""

    view = create_nested_viewset(EventSerializer, Event)()

    assert Event.__name__ == view.__class__.__name__
