from typing import Literal

from _shared import in_query
from _shared.error_service import QUERY_NOT_FOUND

MODE = Literal[
    'create-new-user'
]


@in_query
def use_query(params: dict, query_type: MODE):
    query = ''

    if query_type == 'create-new-user':
        query = '''
            INSERT into user (id, email, password, auth_provider, name, username)
            VALUES (%(id)s, %(email)s, %(password)s, %(auth_provider)s, %(name)s, %(username)s)
            ON DUPLICATE KEY UPDATE
                id=VALUES(id),
                name=VALUES(name)
        '''

    elif query_type == 'get-user-by-username-or-email':
        query = '''
            SELECT id, email, password, auth_provider, name, username
            FROM user
            WHERE username=%(username)s OR email=%(email)s
        '''
    else:
        raise QUERY_NOT_FOUND(query_type)

    return query
