import os
import logging

LOG_LEVEL = logging.DEBUG
PRESERVE_CONTEXT_ON_EXCEPTION = True
DEBUG = False

SESSION_COOKIE_SAMESITE = 'strict'
SESSION_COOKIE_PATH = '/fuel_quote'
SESSION_KEY_PREFIX = "hello"
SESSION_COOKIE_NAME = "fuel_quote_session"
# SESSION_COOKIE_SECURE = True
# REMEMBER_COOKIE_SECURE = True

ROOT_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..'))
LOG_DIR = os.path.join(ROOT_DIR, 'logs')
TEMP_DIR = os.path.join(ROOT_DIR, 'temp')

DIRECTORIES = [LOG_DIR, TEMP_DIR]
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip', 'rar', '7z'}
SECRET_KEY = "Kc5c3zTk'-3<&BdL:P92O{_(:-NkY+"

ENVIRONMENT = "development"

MYSQL_CHARSET = 'utf8mb4'

PROPAGATE_EXCEPTIONS = True

CORS_HEADERS = [
    'Content-Type',
    'Authorization'
]

CORS_ORIGIN_WHITELIST = [
'127.0.0.1:5000'
]
