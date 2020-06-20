from flask import request

from _shared import (BaseError, get_current_user, use_delete, use_get,
                     use_post, use_put, authenticate_request)
from _shared.error_service import AUTHENICATION_ERROR

from . import service
from .schema import ADD_SHEET_SCHEMA


@use_post(path='/add', schema=ADD_SHEET_SCHEMA)
@authenticate_request
def add_sheet():
    data = request.get_json()['data']
    response = service.add_sheets(data, get_current_user()['id'])
    return {'data': response}


@use_get(path='/')
@authenticate_request
def get_sheets():
    filters = {}
    data = service.get_sheets(filters=filters)
    return {'data': data}


@use_delete(path='/remove/:id', schema={})
@authenticate_request
def delete_sheet(id):
    service.delete_sheet(id=id)
    return {'data': 'success'}
