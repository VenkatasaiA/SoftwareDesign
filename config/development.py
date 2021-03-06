import os
import logging

LOG_LEVEL = logging.DEBUG
PRESERVE_CONTEXT_ON_EXCEPTION = True
DEBUG = False

SESSION_COOKIE_SAMESITE = 'strict'
SESSION_COOKIE_PATH = '/fuel_quote'
SESSION_KEY_PREFIX = "hello"
SESSION_COOKIE_NAME = "icici_session"
# SESSION_COOKIE_SECURE = True
# REMEMBER_COOKIE_SECURE = True

ROOT_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..'))
LOG_DIR = os.path.join(ROOT_DIR, 'logs')
TEMP_DIR = os.path.join(ROOT_DIR, 'temp')

DIRECTORIES = [LOG_DIR, TEMP_DIR]
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip', 'rar', '7z'}
SECRET_KEY = "Kc5c3zTk'-3<&BdL:P92O{_(:-NkY+"

ENVIRONMENT = "development"

DB_USERNAME = "root"
DB_PASSWORD = "root12345"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "fuel_quote"
DB_CONNECTION_STRING = 'mysql+mysqlconnector://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST + ':' + DB_PORT + '/' + DB_NAME


# DB_CONNECTION_STRING = "mysql+pymysql://icicimedical:icici%40medical@104.211.186.28:2512/icici_medical"
#DB_CONNECTION_STRING = "mysql+pymysql://icicimedical:icici%40medical@localhost/icici_medical"
MYSQL_CHARSET = 'utf8mb4'

PROPAGATE_EXCEPTIONS = True

CORS_HEADERS = [
    'Content-Type',
    'Authorization'
]

CORS_ORIGIN_WHITELIST = [
'127.0.0.1:5000'
]
