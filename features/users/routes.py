from flask import request

from _shared import BaseError, use_delete, use_get, use_post, use_put
from _shared.error_service import AUTHENICATION_ERROR

from . import service
from . import schema


@use_post(path='/register', schema=schema.REGISTER_USER_SCHEMA)
def register_user():
    data = request.get_json()['data']
    response = service.create_new_user(data)
    return {'data': response}


@use_post(path='/verify', schema=schema.VERIFY_USER_SCHEMA)
def verify():
    data = request.get_json()['data']
    response = service.verify_user(data)
    return {'data': response}


# @use_post(path='/signin/google', schema={})
# def sign_in_with_google():

#     # If this request does not have `X-Requested-With` header, this could be a CSRF
#     if not request.headers.get('X-Requested-With'):
#         raise AUTHENICATION_ERROR

#     data = request.get_json()['data']
#     response = service.sign_in_with_google(data['auth_token'])
#     return {'data': response}


@use_put(path='/update', schema={})
def update_user():
    pass
