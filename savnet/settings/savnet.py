from .base import *
import django.middleware.clickjacking
import os

DEBUG = True
BASE_DIR = os.path.abspath(os.path.join(os.getcwd()))
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

SILENCED_SYSTEM_CHECKS = [
    'security.W004', 'security.W008'
]

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    'rest_framework.renderers.JSONRenderer',
)

ALLOWED_HOSTS = ['*']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'HOST': 'localhost',
#         'PORT': 5432,
#         'USER': 'postgres',
#         'PASSWORD': '123qwe4r',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

USE_TZ = True

TIME_ZONE = 'Asia/Shanghai'
