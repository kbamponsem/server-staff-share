from _shared import INTEGER_TYPE, STRING_TYPE, asRootDict, with_key

ADD_SAMPLE_SCHEMA = asRootDict(
    properties=with_key(
        number=INTEGER_TYPE,
        street_name=STRING_TYPE
    ),
    required=['number', 'street_name']
)
