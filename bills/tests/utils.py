"""Utilities for tests."""

from django.urls import reverse


def create(db_object):
    """Creates new database object and returns it."""

    db_object.save()
    return db_object


def delete(db_object):
    """Deletes given database object."""

    db_object.delete()


def auth_client(client, email, password):
    """Returns client with correct credentials."""

    resp = client.post(
        reverse("token-obtain-pair"),
        {"email": email, "password": password},
        format="json",
    )
    token = resp.data["access"]
    client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

    return client
