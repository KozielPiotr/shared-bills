"""Utilities for tests."""


def create(db_object):
    """Creates new database object and returns it"""

    db_object.save()
    return db_object


def delete(db_object):
    """Deletes given database object"""

    db_object.delete()
