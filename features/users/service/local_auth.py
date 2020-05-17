from _shared import AuthProvider, Constants, hash_value, uuid, with_key
from _shared.error_service import AUTHENICATION_ERROR

from ..schema import REGISTER_USER_DATA
from .queries import MODE, use_query


def create_new_user(data: dict, auth_provider: AuthProvider):
    """create a new user

    Arguments:
        data {dict} -- [description]
        auth_provider {AuthProvider} -- [description]

    Returns:
        [type] -- [description]
    """

    params = __init_user_data(data, auth_provider)

    if auth_provider == AuthProvider.LOCAL.value:
        params['password'] = hash_value(params['password'])

    use_query(params=params, query_type='create-new-user')
    params.pop('password')
    return params


def __init_user_data(data: dict, auth_provider: AuthProvider):

    return {
        'id': data.get('userId', uuid()),
        'email': data['email'],
        'password': data.get('password'),
        'picture': data.get('picture'),
        'first_name': data.get('given_name'),
        'surname': data.get('family_name'),
        'birthday': data.get('birthday'),
        'gender': data.get('gender'),
        'auth_provider': auth_provider or AuthProvider.LOCAL.value
    }
