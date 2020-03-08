from dotenv import load_dotenv
from .utilities import getEnv

load_dotenv()

MODE = getEnv('ENV', 'development')
IS_DEV = getEnv('ENV') != 'production'
MAX_CONTENT_LENGTH = getEnv('MAX_CONTENT_LENGTH')
SECRET_KEY = getEnv('SECRET_KEY')
PORT = getEnv('PORT')

# Exceptions are re-raised rather than being handled
# by the app’s error handlers. If not set,
# this is implicitly true if TESTING or DEBUG is enabled.
PROPAGATE_EXCEPTIONS = getEnv('PROPAGATE_EXCEPTIONS', True)

DB_HOST = getEnv('DB_HOST')
DB_USER = getEnv('DB_USER')
DB_PASS = getEnv('DB_PASS')
DB_NAME = getEnv('DB_NAME')
DB_PORT = getEnv('DB_PORT', 3306)
SOCKET_PATH = getEnv('SOCKET_PATH')
