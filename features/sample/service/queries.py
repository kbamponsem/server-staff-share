from _shared import inQuery


@inQuery
def testQuery(**kwargs):
    return f'''SELECT {kwargs.get('value', 1)}'''


@inQuery
def testInsert(**kwargs):
    return f'''INSERT INTO test (data) VALUES ("{kwargs.get('data')}") '''
