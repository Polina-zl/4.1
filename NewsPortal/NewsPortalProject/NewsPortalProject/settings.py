"""
Django settings for NewsPortalProject project.
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-qm^$lqya%^h^)3g_pp!m11$9(pyey9h+!mmhr@9$3#r%%5nxak'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'news',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'NewsPortalProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'NewsPortalProject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'pzlobina42@gmail.com'
EMAIL_HOST_PASSWORD = 'qcbqbqoncllmxccn'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25

SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_LOGIN_METHODS = {'email', 'username'}
ACCOUNT_SIGNUP_FIELDS = ['email*', 'username*', 'password1*', 'password2*']
ACCOUNT_FORMS = {'signup': 'news.forms.BasicSignupForm'}

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/news/'
LOGOUT_REDIRECT_URL = '/news/'

FORBIDDEN_WORDS = ['редиска', 'дурак', 'идиот', 'глупый', 'журналист']

CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',

    'formatters': {
        'console_debug': {
            'format': '{levelname} {asctime} {message}',
            'style': '{',
        },
        'console_warning': {
            'format': '{levelname} {asctime} {message} {pathname}',
            'style': '{',
        },
        'console_error': {
            'format': '{levelname} {asctime} {message} {pathname} {exc_info}',
            'style': '{',
        },
        'general': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'errors': {
            'format': '{levelname} {asctime} {message} {pathname} {exc_info}',
            'style': '{',
        },
        'security': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'mail': {
            'format': '{levelname} {asctime} {message} {pathname}',
            'style': '{',
        },
    },

    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_debug',
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_warning',
        },
        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_error',
        },
        'general': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'general.log',
            'formatter': 'general',
        },
        'errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'errors.log',
            'formatter': 'errors',
        },
        'security': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'security.log',
            'formatter': 'security',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'mail',
        },
    },

    'loggers': {
        'django': {
            'handlers': ['console', 'console_warning', 'console_error', 'general'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['errors', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['errors', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['errors'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['errors'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['security'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}