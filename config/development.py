from .default import *

APP_ENV = APP_ENV_DEVELOPMENT
ENV = APP_ENV_DEVELOPMENT

DEBUG = True
FLASK_DEBUG = True

SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin@localhost/noteme_users"
