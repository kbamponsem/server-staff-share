from _shared import withSchema, asRootDict, withKey, INTEGER_TYPE, STRING_TYPE

ADD_SAMPLE_SCHEMA = asRootDict(
    properties=withKey(
        number=INTEGER_TYPE,
        street_name=STRING_TYPE
    ),
    required=['number', 'street_name']
)
