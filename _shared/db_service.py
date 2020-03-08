from typing import Union, List, Tuple
from MySQLdb.cursors import Cursor, DictCursor
from MySQLdb import Connection, escape_string  # pylint: disable=no-name-in-module
from functools import wraps
from typing import Callable
import _shared.constants as Constants
import MySQLdb
from _shared.utilities import compose
from flask.logging import logging as logger
from flask import g

CONNECTION_PARAMS = {
    'host': Constants.DB_HOST,
    'user': Constants.DB_USER,
    'passwd': Constants.DB_PASS,
    'db': Constants.DB_NAME,
    'port': Constants.DB_PORT,
}

if not Constants.IS_DEV:
    CONNECTION_PARAMS['unix_socket'] = Constants.SOCKET_PATH


def getDbConnection() -> Connection:
    '''get a connection from the pool'''
    conn = None
    try:
        conn = getattr(g, 'db_connection')
    except AttributeError:
        conn = MySQLdb.connect(**CONNECTION_PARAMS)
    finally:
        setattr(g, 'db_connection', conn)
    return conn


def endDbConnection(_=None):
    '''end mysql database connection'''
    try:

        conn: Connection = getattr(g, 'db_connection')
        conn.close()
        logger.debug('Database connection closed')
    except AttributeError:
        logger.debug('Database connection does not exist')


def withEscape(func):
    '''
    In order to avoid SQL Injection attacks,
    you should always escape any user provided data
    before using it inside a SQL query.
    '''

    @wraps(func)
    def wrapper(*args, **kwargs):
        args = [escape_string(arg) for arg in args]
        kwargs = {k: escape_string(v) if isinstance(
            v, str) else v for k, v in kwargs.items()}
        return func(*args, **kwargs)

    return wrapper


def inQuery(query_func):

    @wraps(query_func)
    @withEscape
    def wrapper(*args, **kwargs):
        conn = getDbConnection()
        cur = getCursor(conn)
        return runPreparedQuery(cur, query_func(*args, **kwargs))

    return wrapper


def runInTransaction(func: Callable):
    '''
    higher order function
    takes in a function and
    returns a function that executes the passed in function within a transaction
    should probably be called wrapped in a try catch as it does not handle
    any errors, other than rolling back the transaction
    '''

    @wraps(func)
    def wrapper(*args, **kwargs):
        conn = getDbConnection()
        conn.begin()  # start transaction
        logger.debug('[SQL] BEGIN')
        try:
            results = func(*args, **kwargs)
            conn.commit()
            logger.debug('[SQL] COMMIT')
            return results
        except Exception as e:
            rollback(conn)
            logger.debug('[SQL] ROLLBACK')
            raise e

    return wrapper


def rollback(conn: Connection = None):
    conn = conn or getDbConnection()
    if conn:
        conn.rollback()
        logger.debug('ROLLBACK')


@runInTransaction
def runPreparedQuery(cur: Cursor, preparedQuery: str, params: List[Tuple] = [], dim: Union['single', 'multi'] = 'single'):
    '''
    Executes a database query and returns a PROMISE that resolves with the data
    USE ONLY FOR, CREATE, UPDATE, DELETE,

    !!!!!  DO NOT USE FOR READ !!!!!!
    prepared query shd look like this:
    'INSERT INTO movies (title, rating) VALUES (?, ?)'
    Array should look like this:
    [['Taxi Driver', 100], ['Taxi Driver', 100]]
    '''

    logger.debug(f'[SQL] {preparedQuery}')
    if dim == 'multi':
        cur.executemany(preparedQuery, params)
    else:
        cur.execute(preparedQuery, params)

    return cur.fetchall()


def getCursor(conn: Connection) -> Cursor:
    ''' get database cursor '''
    return conn.cursor(DictCursor)


def getLastId(cur: Cursor) -> int:
    ''' get last inserted id '''
    return cur.lastrowid


def getLastIds(cur: Cursor) -> List[int]:
    ''' get last inserted ids '''
    return [getLastId(cur) + row for row in range(cur.rowcount)]
