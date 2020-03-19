from _shared import in_query


@in_query
def test_query(**kwargs):
    return f'''SELECT {kwargs.get('value', 1)}'''


@in_query
def test_insert(**kwargs):
    return f'''INSERT INTO test (data) VALUES ("{kwargs.get('data')}") '''
