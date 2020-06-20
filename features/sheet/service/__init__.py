import os

from _shared import CONSTANTS, BaseError, get_current_time, uuid

from ..model import Sheet
from .queries import use_query
from base64 import decodestring


def add_sheets(data: dict, current_user_id: str) -> Sheet:
    params = {'id': uuid(), **data,  'uploaded_by': current_user_id,
              'created_at': get_current_time(), 'updated_at': get_current_time()}

    params['data_path'] = __save_base64_image(params.pop('base64Data'), params['id'], params['extension'])

    use_query(query_type='add-sheet', params=params)
    return params


def get_sheets(filters={}, id=None) -> Sheet:
    data = use_query(query_type='get-sheets', params={**filters, 'id': id})
    if id:
        return data[0] if len(data) else None

    return data


def delete_sheet(id):
    sheet = get_sheets(id=id)
    if not sheet:
        return

    __delete_file(sheet['data_path'])
    use_query(query_type='delete-sheet', params={'id': id})


def __save_base64_image(base64_data, filename, extension) -> str:
    if not __allowed_file(extension):
        raise BaseError(message='File extension not supported')

    filename = f'{filename}.{extension}'

    with open(os.path.join(CONSTANTS.UPLOAD_FOLDER, filename), 'wb') as f:
        f.write(decodestring(base64_data.encode('ascii')))
    return filename


def __allowed_file(extension: str):
    return extension.lower() in CONSTANTS.ALLOWED_EXTENSIONS


def __get_extension(filename: str):
    if '.' not in filename:
        raise BaseError('Unknown file extension')

    return filename.rsplit('.', 1)[1].lower()


def __delete_file(filepath):
    os.remove(filepath)
