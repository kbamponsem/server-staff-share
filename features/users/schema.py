from typing import TypedDict

from _shared import DATE_TYPE, EMAIL_TYPE, STRING_TYPE, asRootDict, with_key

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

GOOGLE_sIGN_IN_SCHEMA = asRootDict(
    properties=with_key(
        auth_token=STRING_TYPE
    ),
    required=['auth_token']
)
