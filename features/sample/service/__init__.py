from .queries import testQuery, testInsert
from _shared import withKey


def test_query():
    return withKey(results=testQuery(value=1)[0])


def test_insert_query():
    return withKey(results=testInsert(data='Hello world from python'))
