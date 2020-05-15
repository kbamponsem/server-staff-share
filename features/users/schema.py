from _shared import EMAIL_TYPE, STRING_TYPE, asRootDict, with_key, DATE_TYPE
from typing import TypedDict

REGISTER_USER_DATA = TypedDict('REGISTER_USER_DATA', {
    'email': str,
    'password': str,
    'dob': str
})

REGISTER_USER_SCHEMA = asRootDict(
    properties=with_key(
        email=EMAIL_TYPE,
        password=STRING_TYPE,
        dob=DATE_TYPE
    ),
    required=['email', 'password', 'dob']
)
