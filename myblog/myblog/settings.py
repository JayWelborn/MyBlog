"""
Django settings for myblog project.

Generated by 'django-admin startproject' using Django 1.10.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import os
from .private_settings import *


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '192.168.2.113',
    'localhost',
    '127.0.0.1',
    'jaywelborn.pythonanywhere.com',
]

# Application definition

INSTALLED_APPS = [
    'home.apps.HomeConfig',
    'polls.apps.PollsConfig',
    'blog.apps.BlogConfig',
    'bingo.apps.BingoConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',
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

ROOT_URLCONF = 'myblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'myblog.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_URL = '/static/'

# Media files (images uploaded via admin page/authenticated users)
# https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-MEDIA_ROOT
MEDIA_URL = '/media/'


# Add Email info
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'jesse.welborn@gmail.com'
EMAIL_HOST_USER = 'jesse.welborn@gmail.com'

# Change max upload size to accommodate MP3s
MAX_UPLOAD_MEMORY_SIZE = 10485760

# Enable tinyMCE plugins
TINYMCE_DEFAULT_CONFIG = {
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': 'link image preview codesample contextmenu table code charmap textcolor colorpicker '
                'hr paste textpattern',
    'toolbar1': 'bold italic underline forecolor backcolor| alignleft aligncenter alignright alignjustify '
               '| bullist numlist | outdent indent | table | link image | codesample | preview code | charmap ',
    'contextmenu': 'formats | link image | forecolor backcolor',
    'menubar': True,
    'inline': False,
    'statusbar': True,
    'height': 360,
    'paste_data_images': True,
    'textpattern_patterns': [
        {'start': '*', 'end': '*', 'format': 'italic'},
        {'start': '**', 'end': '**', 'format': 'bold'},
        {'start': '#', 'format': 'h1'},
        {'start': '##', 'format': 'h2'},
        {'start': '###', 'format': 'h3'},
        {'start': '####', 'format': 'h4'},
        {'start': '#####', 'format': 'h5'},
        {'start': '######', 'format': 'h6'},
        {'start': '1. ', 'cmd': 'InsertOrderedList'},
        {'start': '* ', 'cmd': 'InsertUnorderedList'},
        {'start': '- ', 'cmd': 'InsertUnorderedList'}
    ],
}
TINYMCE_SPELLCHECKER = False
