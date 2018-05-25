"""
Django settings for coffeehouse project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = '/django/projects/coffeehouse'  PROJECT_DIR='/django/projects/coffeehouse/src'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = (os.path.join(PROJECT_DIR, 'templates'),)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=f2dw)crjsi13kt3whc2+=8%dd&hx_xd&9x90=o6t39^nav=l&'

# Reduce threshold to DEBUG level in settings.py
from django.contrib.messages import constants as message_constants
MESSAGE_LEVEL = message_constants.DEBUG

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.about.templates.about',
    'django.contrib.admindocs',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'coffeehouse.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['%s' % TEMPLATE_DIR, ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': False,
            # 'autoescape': False,
            # “”“You can either use the {% autoescape off %} tag  {% autoescape on %}
            #  to disable auto-escaping on a section of a Django template
            # or the safe filter to disable auto-escaping on a single Django template variable.”“”

            # 'string_if_invalid': "**** WARNING INVALID VARIABLE %s ****",
            # 'string_if_invalid': InvalidTemplateVariable("%s"),
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            # 'builtins': [
            #     'coffeehouse.builtins',
            #     'thirdpartyapp.customtags.really_useful_tags_and_filters',
            # ],
            # 'libraries': {
            #    'coffeehouse_tags': 'coffeehouse.tags_filters.common',  # {% load coffeehouse_tags %}
            # },
            #'loaders': [
                 # 'django.template.loaders.filesystem.Loader',
            #      'django.template.loaders.app_directories.Loader',
            #  ],
        },
    },
]

WSGI_APPLICATION = 'coffeehouse.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql', #'django.db.backends.mysql' 'django.db.backends.oracle'
#         'NAME': 'mydatabase',
#         'USER': 'mydatabaseuser',
#         'PASSWORD': 'mypassword',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #'' 'django.db.backends.oracle'
        'NAME': 'coffeehouse',
        'USER': 'djangouser',
        'PASSWORD': 'djangouser',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
# CREATE USER 'djangouser'@'localhost' IDENTIFIED BY 'djangouser';
# GRANT ALL PRIVILEGES ON *.* TO 'djangouser'@'localhost' IDENTIFIED BY 'djangouser' REQUIRE NONE WITH GRANT OPTION MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
# CREATE DATABASE IF NOT EXISTS `coffeehouse` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;
# GRANT ALL PRIVILEGES ON `coffeehouse`.* TO 'coffeehouse'@'localhost';


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

 INTERNAL_IPS = ['127.0.0.1', ]