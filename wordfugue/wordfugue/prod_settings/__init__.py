from wordfugue.settings import *
import dj_database_url

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

DEBUG = False

PROTOCOL = 'https://'

ALLOWED_HOSTS = [
    'localhost',
    '.herokuapp.com',
    '.wordfugue.com',
    '.philipjohnjames.com',
]

SECRET_KEY = get_env_variable("WORDFUGUE_SECRET_KEY")

INSTALLED_APPS += (
    'gunicorn',
    'opbeat.contrib.django',
)

MIDDLEWARE_CLASSES = [
    'opbeat.contrib.django.middleware.OpbeatAPMMiddleware',
    'opbeat.contrib.django.middleware.Opbeat404CatchMiddleware',
] + MIDDLEWARE_CLASSES

OPBEAT = {
    'ORGANIZATION_ID': get_env_variable("OPBEAT_ORG_ID"),
    'APP_ID': get_env_variable("OPBEAT_APP_ID"),
    'SECRET_TOKEN': get_env_variable("OPBEAT_SECRET_KEY"),
}

STATIC_URL = '//wordfugue.s3.amazonaws.com/assets/'
