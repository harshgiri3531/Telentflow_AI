from .base import *
from decouple import config
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}