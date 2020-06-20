from flask import Flask

from _shared import in_scope
from features import users
from features import sheet


def register_urls(app: Flask):
    # --- REGISTER ROUTES ---
    in_scope(app, '/users', users.expose)
    in_scope(app, '/sheets', sheet.expose)
