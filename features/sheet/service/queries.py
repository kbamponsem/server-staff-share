from typing import Literal

from _shared import and_where, in_query, or_where
from _shared.error_service import QUERY_NOT_FOUND

MODE = Literal[
    'add-sheet',
    'get-sheet'
]


@in_query
def use_query(params: dict, query_type: MODE):
    query = ''

    if query_type == 'add-sheet':
        query = '''
            INSERT into sheet (id, title, subtitle, composer, uploaded_by,
            genre, keySignature, data_path, created_at, updated_at)
            VALUES (
                %(id)s,
                %(title)s,
                %(subtitle)s,
                %(composer)s,
                %(uploaded_by)s,
                %(genre)s,
                %(keySignature)s,
                %(data_path)s,
                %(created_at)s,
                %(created_at)s
            )
            ON DUPLICATE KEY UPDATE
                title=VALUES(title),
                subtitle=VALUES(subtitle),
                composer=VALUES(composer),
                genre=VALUES(genre),
                keySignature=VALUES(keySignature),
                data_path=VALUES(data_path),
                updated_at=VALUES(updated_at)
        '''

    elif query_type == 'get-sheets':
        query = '''
            SELECT id, title, subtitle, composer, uploaded_by, genre, keySignature, data_path,
                    created_at, updated_at
            FROM sheet
        '''
        query += and_where(params=params, filters=['id', 'genre', 'composer'])

    else:
        raise QUERY_NOT_FOUND(query_type)

    return query
