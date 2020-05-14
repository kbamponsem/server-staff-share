from _shared import with_key

from .queries import test_insert, test_query


def test_select_query():
    return with_key(results=test_query(value=1)[0])


def test_insert_query():
    return with_key(results=test_insert(data='Hello world from python'))
