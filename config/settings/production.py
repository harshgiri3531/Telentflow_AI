from .base import *
from decouple import config
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

# Security settings for production
# SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True