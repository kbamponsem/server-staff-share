from google.auth.transport import requests
from google.oauth2 import id_token

from _shared import AuthProvider, Constants, hash_value, uuid, with_key
from _shared.error_service import AUTHENICATION_ERROR

from ..schema import REGISTER_USER_DATA
from .local_auth import create_new_user
from .queries import MODE, use_query


def sign_in_with_google(auth_token: str):
    """handle sign in with google

    Arguments:
        auth_token {str} -- authorization code
    """

    user_data = __verify_google_issuer(auth_token)
    return create_new_user(user_data, AuthProvider.GOOGLE.value)


def __verify_google_issuer(auth_token: str):
    """verify token and get user data from google

    Arguments:
        auth_token {str} -- auth token from client

    Raises:
        AUTHENICATION_ERROR: authentication failed

    Returns:
        {dict} -- user data
    """

    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), Constants.GOOGLE_CLIENT_ID)
    except Exception:
        raise AUTHENICATION_ERROR

    # verify issuer
    if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
        raise AUTHENICATION_ERROR

    # https://www.googleapis.com/oauth2/v2/userinfo
    # get user info

    user_data = {
        'id': idinfo['sub'],
        'email': idinfo['email'],
        'picture': idinfo['picture'],
        'first_name': idinfo['given_name'],
        'surname': idinfo['family_name'],
        'birthday': idinfo['birthday'],
        'gender': idinfo['gender']
    }

    return user_data
