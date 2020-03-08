from functools import partial, wraps
from flask import request
from jsonschema import validate, ValidationError
from _shared.error_service import JSON_VALIDATION_ERROR
from typing import Callable
import logging as logger
from pprint import pformat


def useSchema(schema: any, func: Callable):
    ''' schema validation middleware '''

    @wraps(func)
    def wrapper(*args, ** kwargs):
        data = request.get_json()
        logger.debug(f'payload {data}')
        if schema:
            try:
                validate(instance=data, schema=schema)
            except ValidationError as error:
                try:
                    error_details = {
                        'path': '/'.join([str(p) for p in list(error.absolute_path)[1::2]]),
                        'reason': error.message
                    }
                except IndexError:
                    error_details = {'path': '', 'message': error.message}
                raise JSON_VALIDATION_ERROR(error_details)
        return func(*args, **kwargs)
    return wrapper


def withSchema(schema, inData=True):
    ''' wrapper for json schema '''
    if not inData:
        return {**schema, 'additionalProperties': False}

    return {'type': 'object', 'properties': {'data': schema}, 'required': ['data']}


def withObject(**kwargs):
    ''' object wrapper for json schema '''
    return withSchema({
        'type': 'object', 'properties': kwargs['properties'],
        'required': kwargs.get('required', [])},
        kwargs.get('inData', [])
    )


def withArray(items, inData=False):
    ''' array wrapper for json schema '''
    return withSchema({'type': 'array', 'items': items}, inData)


asRootDict = partial(withObject, inData=True)
asRootArray = partial(withArray, inData=True)
