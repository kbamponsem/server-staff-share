from _shared import usePost, useGet, usePut, useDelete, BaseError
from flask import jsonify, make_response
from .schema import ADD_SAMPLE_SCHEMA
from .service import test_query, test_insert_query
import logging as logger


@usePost(path='/addSample', schema=ADD_SAMPLE_SCHEMA)
def addSample():
    test_insert_query()
    return {'message': 'success'}


@useGet(path='/getSample')
def getSample():
    res = test_query()
    return res


@usePut(path='/updateSample', schema={})
def updateSample():
    return {'message': 'updateSample'}


@useDelete(path='/deleteSample', schema={})
def deleteSample():
    return {'message': 'deleteSample'}


@useGet(path='/broken')
def broken():
    raise BaseError(message='Broken')
