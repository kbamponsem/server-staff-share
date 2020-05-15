from _shared import in_query
from _shared.error_service import QUERY_NOT_FOUND
from typing import Literal

MODE = Literal[
    'create-new-user'
]


@in_query
def use_query(params: dict, query_type: MODE):
    query = ''

    if query_type == 'create-new-user':
        query = '''
            INSERT into user (id, email, password, auth_provider)
            VALUES (%(id)s, %(email)s, %(password)s, %(auth_provider)s)
            ON DUPLICATE KEY UPDATE
                id=VALUES(id),
                password=VALUES(password)

        '''

    else:
        raise QUERY_NOT_FOUND(query_type)

    return query
