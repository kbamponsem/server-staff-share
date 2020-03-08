from flask import jsonify
from _shared.error_service import BaseError, format_error, HTTP_404_ERROR, HTTP_503_ERROR, HTTP_500_ERROR, HTTP_405_ERROR
from typing import Union, Callable, List, Union, Tuple
from functools import partial
from flask import Flask
from _shared.db_service import rollback
import traceback
from flask.logging import logging as logger


def withError(err_type: BaseError, static=True):
    ''' api error handler wrapper '''
    def errorResponse(error):
        error = error if not static else err_type
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        logger.error(traceback.format_exc())
        return response
    return errorResponse


handleError = withError(BaseError, False)
handle404Error = withError(HTTP_404_ERROR)
handle503Error = withError(HTTP_503_ERROR)
handle500Error = withError(HTTP_500_ERROR)
handle405Error = withError(HTTP_405_ERROR)


def registerErrorHandlers(app: Flask):
    handlers = [
        (handleError, BaseError),
        (handle404Error, 404),
        (handle500Error, 500),
        (handle500Error, Exception),
        (handle503Error, 503),
        (handle405Error, 405)
    ]
    return [app.errorhandler(arg)(func) for func, arg in handlers]
