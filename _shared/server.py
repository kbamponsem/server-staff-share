from flask import Flask
from .utilities import withKey
import _shared.constants as Constants


def configure_app(app: Flask):
    ''' configure flask app '''
    app.config.update(**withKey(
        SECRET_KEY=Constants.SECRET_KEY,
        ENV=Constants.MODE,
        MAX_CONTENT_LENGTH=Constants.MAX_CONTENT_LENGTH,
        PROPAGATE_EXCEPTIONS=Constants.PROPAGATE_EXCEPTIONS,
    ))
    return app
