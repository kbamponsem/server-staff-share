from flask import Flask
from _shared.db_service import endDbConnection, getDbConnection
import logging as logger


def addMiddlewares(app: Flask):
    app.teardown_appcontext(endDbConnection)
