from flask import Flask
from _shared import (
    Constants, configure_app,
    BaseError, registerErrorHandlers,
    addMiddlewares
)
from urls import registerUrls
from logging.config import dictConfig
from logging import StreamHandler
import logging

# logging.setLoggerClass(ColoredLogger)

# dictConfig({
#     'version': 1,
#     'formatters': {'default': {
#         'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
#     }},
#     'handlers': {'wsgi': {
#         'class': 'logging.StreamHandler',
#         'stream': 'ext://flask.logging.wsgi_errors_stream',
#         'formatter': 'default'
#     }},
#     'root': {
#         'level': 'DEBUG',
#         'handlers': ['wsgi']
#     }
# })
app = Flask(__name__)
app = configure_app(app)

registerErrorHandlers(app)
registerUrls(app)
addMiddlewares(app)

if __name__ == "__main__":
    app.run(port=Constants.PORT, debug=Constants.IS_DEV)
