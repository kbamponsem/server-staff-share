from _shared import asRootDict, with_key, INTEGER_TYPE, STRING_TYPE

ADD_SAMPLE_SCHEMA = asRootDict(
    properties=with_key(
        number=INTEGER_TYPE,
        street_name=STRING_TYPE
    ),
    required=['number', 'street_name']
)
