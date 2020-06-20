import datetime as dt
from datetime import date
from typing import TypedDict, Union

import _shared


class Sheet(TypedDict):
    id: str
    title: str
    subtitle: Union[str, None]
    composer: str
    uploaded_by: Union[str, dict]
    genre: str
    keySignature: str
    data_path: str
    created_at: date
    updated_at: date
