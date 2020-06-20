from flask import Flask

import _shared.constants as Constants

from .utilities import with_key


def configure_app(app: Flask):
    """ configure flask app """
    app.config.update(**with_key(
        SECRET_KEY=Constants.SECRET_KEY,
        ENV=Constants.MODE,
        MAX_CONTENT_LENGTH=Constants.MAX_CONTENT_LENGTH,
        PROPAGATE_EXCEPTIONS=Constants.PROPAGATE_EXCEPTIONS,
        UPLOAD_FOLDER=Constants.UPLOAD_FOLDER
    ))
    return app
