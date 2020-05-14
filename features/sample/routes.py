from _shared import BaseError, use_delete, use_get, use_post, use_put

from .schema import ADD_SAMPLE_SCHEMA
from .service import test_insert_query, test_select_query


@use_post(path='/addSample', schema=ADD_SAMPLE_SCHEMA)
def add_sample():
    test_insert_query()
    return {'message': 'success'}


@use_get(path='/getSample')
def get_sample():
    res = test_select_query()
    return res


@use_put(path='/updateSample', schema={})
def update_sample():
    return {'message': 'updateSample'}


@use_delete(path='/deleteSample', schema={})
def delete_sample():
    return {'message': 'deleteSample'}


@use_get(path='/broken')
def broken():
    raise BaseError(message='Broken')
