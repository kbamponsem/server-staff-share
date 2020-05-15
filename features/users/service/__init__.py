from _shared import with_key, AuthProvider, uuid, hash_value
from .queries import use_query, MODE
from ..schema import REGISTER_USER_DATA


def create_new_user(data: REGISTER_USER_DATA):
    params = {**data.copy(), 'auth_provider': AuthProvider.LOCAL.value, 'id': '60ac5774-e0fb-4467-8c32-06e28f6e32ad'}
    params['password'] = hash_value(params['password'])
    use_query(params=params, query_type='create-new-user')
    params.pop('password')
    return params
