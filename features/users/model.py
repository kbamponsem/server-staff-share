from typing import Union, TypedDict
import _shared
import datetime as dt


class User(TypedDict):
    id: int  # unsigned
    first_name: str
    middle_name: Union[str, None]
    surname: str

    dob: dt.date
    occupation: Union[str, None]

    phone_number: Union[str, None]
    email: str
    password: str
    auth_provider: _shared.AuthProvider
