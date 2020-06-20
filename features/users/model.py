import datetime as dt
from typing import TypedDict, Union

import _shared


class User(TypedDict):
    id: str
    name: str
    username: str
    email: str
    password: Union[str, None]
    auth_provider: _shared.AuthProvider
