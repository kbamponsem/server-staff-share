from typing import TypedDict

from _shared import DATE_TYPE, EMAIL_TYPE, STRING_TYPE, asRootDict, with_key

REGISTER_USER_SCHEMA = asRootDict(
    properties=with_key(
        email=EMAIL_TYPE,
        name=STRING_TYPE,
        username=STRING_TYPE,
        password=STRING_TYPE
    ),
    required=['email', 'password', 'username', 'name']
)

GOOGLE_sIGN_IN_SCHEMA = asRootDict(
    properties=with_key(
        auth_token=STRING_TYPE
    ),
    required=['auth_token']
)

VERIFY_USER_SCHEMA = asRootDict(
    properties=with_key(
        email_or_username=STRING_TYPE,
        password=STRING_TYPE
    )
)
