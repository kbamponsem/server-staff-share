from typing import TypedDict

from _shared import DATE_TYPE, EMAIL_TYPE, STRING_TYPE, asRootDict, with_key, NULLABLE_STRING_TYPE, EXTENSIONS

ADD_SHEET_SCHEMA = asRootDict(
    properties=with_key(
        title=STRING_TYPE,
        subtitle=NULLABLE_STRING_TYPE,
        composer=NULLABLE_STRING_TYPE,
        genre=STRING_TYPE,
        keySignature=STRING_TYPE,
        base64Data=STRING_TYPE,
        extension=EXTENSIONS
    ),
    required=['title', 'genre', 'keySignature', 'base64Data', 'extension']
)
