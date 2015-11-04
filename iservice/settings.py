
# this will beeeeeee  eeeeee
# from ConfigParser import RawConfigParser
import os
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
project_path = lambda a: os.path.join(PROJECT_PATH, a)
here = lambda a: os.path.join(os.path.abspath(os.path.dirname(__file__)), a)
# config = RawConfigParser()
# config.read(os.path.join(here(''), 'config.cfg'))

"""
Django settings for iservice project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gi=69ud9c381_mo3r!3hjh3uw_420yoo+uf8&8__^ntn1o2zs#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'iservice',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'iservice.urls'

WSGI_APPLICATION = 'iservice.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': config.get('db_pgsql', 'ENGINE'), # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': config.get('db_pgsql', 'NAME'),                    # Or path to database file if using sqlite3.
#         'USER': config.get('db_pgsql', 'USER'),                     # Not used with sqlite3.
#         'PASSWORD': config.get('db_pgsql', 'PASSWORD'),              # Not used with sqlite3.
#         'HOST': config.get('db_pgsql', 'HOST'),                      # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': config.get('db_pgsql', 'PORT'),                        # Set to empty string for default. Not used with sqlite3.
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
