from flask import Flask

from _shared import in_scope
from features import sample


def register_urls(app: Flask):
    # --- REGISTER ROUTES ---
    in_scope(app, '/sample', sample.expose)
