from _shared import AuthProvider, Constants, hash_value, uuid, with_key, hash_value, verify_hash, encode_jwt
from _shared.error_service import AUTHENICATION_ERROR

from ..model import User
from .queries import MODE, use_query


def create_new_user(data: dict, auth_provider: AuthProvider = AuthProvider.LOCAL) -> User:
    """create a new user

    Arguments:
        data {dict} -- [description]
        auth_provider {AuthProvider} -- [description]

    Returns:
        [type] -- [description]
    """

    params = __init_user_data(data, auth_provider.value)

    if auth_provider == AuthProvider.LOCAL:
        params['password'] = hash_value(params['password'])

    use_query(params=params, query_type='create-new-user')
    params.pop('password')
    params.pop('auth_provider')
    return params


def verify_user(data):
    user = use_query(query_type='get-user-by-username-or-email', params={
        'email': data['email_or_username'],
        'username': data['email_or_username']
    })
    if not len(user):
        raise AUTHENICATION_ERROR
    else:
        user = user[0]
    # verify passowrd
    if not verify_hash(user['password'], data['password']):
        raise AUTHENICATION_ERROR
    user.pop('password')
    user['auth_token'] = encode_jwt(user)
    return user


def __init_user_data(data: dict, auth_provider: AuthProvider):

    return {
        'id': data.get('userId', uuid()),
        'email': data['email'],
        'password': data.get('password'),
        'name': data.get('name'),
        'username': data.get('username'),
        'auth_provider': auth_provider or AuthProvider.LOCAL.value
    }
