from functools import wraps

from flask import g, request

from .error_service import AUTHENICATION_ERROR
from .utilities import decode_jwt


def authenticate_request(func):
    """decorator to authenticate requests

    Arguments:
        func {Callable} -- wrapped function

    Returns:
        Callable -- decorated function
    """

    @wraps(func)
    def decor(*args, **kwargs):
        # --- IMPLEMENT YOUR AUTHENTICATION HERE -- #
        token = request.headers.get('Authorization')
        if not token:
            raise AUTHENICATION_ERROR

        user = decode_jwt(token.replace('Bearer ', ''))
        set_current_user(user_id=user['id'], **user)
        return func(*args, **kwargs)

    return decor


def set_current_user(user_id, privileges=None, **kwargs):
    """ Set the currently logged in user for a session """
    user_data = {'user_id': user_id, 'privileges': privileges or []}
    user_data.update(kwargs)
    setattr(g, 'current_user', user_data)


def get_current_user():
    """
    Get the currently logged in user.
    This AuthUser object would have been stored
    in the global g object of flask

    :returns (AuthUser): Represents the currently logged in user

    :raises: :AuthenticationFailedError: no session user data
    """
    try:
        user_data = getattr(g, 'current_user')
    except Exception:
        # no user data has been attached to g yet.
        # This means no user has been authenticated for this session
        raise AUTHENICATION_ERROR
    return user_data
