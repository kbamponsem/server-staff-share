from flask import Flask
from _shared import inScope
from features import sample


def registerUrls(app: Flask):
    ### REGISTER ROUTES ###
    inScope(app, '/sample', sample.expose)
