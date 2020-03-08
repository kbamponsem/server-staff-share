from .utilities import withKey
from typing import Any


class BaseError(Exception):
    '''
    Base exception for all the custom API errors
    '''

    def __init__(self, message=None, status_code=400, payload=None):
        super(BaseError, self).__init__(message)
        self.status_code = status_code
        self.payload = payload
        self.message = message

    def to_dict(self):
        '''
        Get a dictionary representation of this error instance
        '''
        return format_error(self.message, self.status_code, self.payload)


def format_error(message: str, status_code: int, data=None):
    return {'error': {**withKey(message=message, data=data)}, **withKey(statusCode=status_code)}


HTTP_404_ERROR = BaseError('Requested url not found', 404)
HTTP_503_ERROR = BaseError('Service Unavailable', 503)
HTTP_405_ERROR = BaseError('Method not allowed', 405)
HTTP_500_ERROR = BaseError(
    'Something went wrong, our team will investigate into this', 500)

AUTHENICATION_ERROR = BaseError('Authentication Failed', 401)
PERMISSION_DENIED = BaseError('Permission Denied', 401)


def JSON_VALIDATION_ERROR(data): return BaseError(
    'Invalid json data', 442, data)
