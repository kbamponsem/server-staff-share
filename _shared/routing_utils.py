from .typings import RouterParams, HTTP_METHODS
from typing import Any, Callable, List
from . import useSchema
from functools import partial, wraps
from .utilities import withKey
from flask import Flask, make_response, jsonify
import logging as logger


def withResponse(func: Any, status_code: int):
    ''' serialize api response '''

    @wraps(func)
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        logger.debug(f'response {response}')
        return make_response(jsonify(response), status_code)
    return wrapper


def withRouter(**params: RouterParams):
    ''' configure route '''

    method = params['method'] or HTTP_METHODS.GET
    schema = params.get('schema')
    status_code = params.get(
        'status_code') or 200 if method == HTTP_METHODS.GET else 201

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            handler = lambda *args, **kwargs: func(*args, **kwargs)
            handler = useSchema(schema, handler)
            handler = withResponse(handler, status_code)
            return withKey(path=params['path'], method=method, handler=handler)

        return wrapper

    return decorator


def usePost(path: str, schema: Any = None):
    ''' configure route as HTTP POST REQUEST '''
    return withRouter(**withKey(schema=schema, path=path, method=HTTP_METHODS.POST))


def useGet(path: str):
    ''' configure route as HTTP GET REQUEST '''
    return withRouter(**withKey(path=path, method=HTTP_METHODS.GET))


def usePut(path: str, schema: Any):
    ''' configure route as HTTP PUT REQUEST '''
    return withRouter(**withKey(schema=schema, path=path, method=HTTP_METHODS.PUT))


def useDelete(path: str, schema: Any):
    ''' configure route as HTTP DELETE REQUEST '''
    return withRouter(**withKey(schema=schema, path=path, method=HTTP_METHODS.DELETE))


def addRoute(app: Flask, basePath: str, path: str, handler: Callable, method: HTTP_METHODS, endpoint=None):
    ''' add route to flask apis '''

    path = f'{basePath}{path}'
    app.add_url_rule(rule=path, view_func=handler,
                     methods=[method.value], endpoint=path)


def inScope(app: Flask, basePath: str, handlers: List[Any]):
    ''' group route in api scope '''

    return [addRoute(app=app, basePath=basePath, **child()) for child in handlers]
