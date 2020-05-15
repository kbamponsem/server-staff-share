from _shared import BaseError, use_delete, use_get, use_post, use_put
from flask import request
from .schema import REGISTER_USER_SCHEMA
from .service import create_new_user


@use_post(path='/register', schema=REGISTER_USER_SCHEMA)
def register_user():
    data = request.get_json()['data']
    response = create_new_user(data)
    return {'data': response}


@use_put(path='/update', schema={})
def update_user():
    pass
