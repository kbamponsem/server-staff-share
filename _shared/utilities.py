import os
from functools import reduce


def getEnv(key: str, default=None):
    ''' get value from environment '''
    return os.getenv(key) or default


def withKey(**kwargs):
    ''' spread arguments to key - value pairs '''
    return {k: v for k, v in kwargs.items()}


def getTemplatePath(name: str):
    ''' get path to template file '''
    return os.path.join(__file__, '../templates', name)


def compose(*fs):
    def inner(f, g):
        return lambda *a, **kw: f(g(*a, **kw))
    return reduce(inner, fs)
