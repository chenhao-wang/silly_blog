# choose settings between Developement and Deploy
import os
from os.path import join, dirname, abspath
import platform

node = platform.node()
dev_machines = ('inofance')

if node in dev_machines:
    # folder My_Blog
    # My_Blog = os.path.dirname(os.path.dirname(__file__))
    # project dir, contains static and media folder under DEV environment
    My_Blog = dirname(abspath(__file__))
    PROJECT_DIR = dirname(dirname(My_Blog))
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(My_Blog, 'db.sqlite3'),
        }
    }
    STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
    STATIC_URL = '/static/'
    MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
    MEDIA_URL = '/media/'
    TEMPLATE_DIRS = [os.path.join(My_Blog, 'templates')]
    ALLOWED_HOSTS = ['*']
else:
    DEBUG = False
    # DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'silly_database',
            'USER': 'inofance',
            'PASSWORD': 'DJANGO_DB_PASSWORD',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
    # PROJECT_DIR = '/home/inofance/silly_blog/'
    PROJECT_DIR = dirname(dirname(abspath(__file__)))
    # MEDIA_ROOT = '/home/inofance/silly_blog/media'
    MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')
    MEDIA_URL = '/media/'
    # STATIC_ROOT = '/home/inofance/silly_blog/my_blog/static'
    STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
        os.path.join(PROJECT_DIR, 'static'),
    )

    TEMPLATE_DIRS = (
        os.path.join(PROJECT_DIR, 'templates'),
    )

    ALLOWED_HOSTS = [
        '18.221.38.12',
        '.showforit.com',
    ]

    # cache entire site
    MIDDLEWARE_CLASSES_ADDITION_FIRST = (
        'django.middleware.cache.UpdateCacheMiddleware',
    )

    MIDDLEWARE_CLASSES_ADDITION_LAST = (
        'django.middleware.cache.FetchFromCacheMiddleware',
    )

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:8000',
        }
    }
