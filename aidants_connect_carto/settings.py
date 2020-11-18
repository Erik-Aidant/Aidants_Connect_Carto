"""
Django settings for aidants_connect_carto project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import dj_database_url
from dotenv import load_dotenv


load_dotenv(verbose=True)

HOST = os.getenv("HOST")

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("APP_SECRET")

# SECURITY WARNING: don"t run with debug turned on in production!
if os.getenv("DEBUG") == "True":
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = [os.getenv("HOST")]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "rest_framework",
    "drf_yasg",
    "modelsdoc",
    "aidants_connect_carto.apps.core",
    "aidants_connect_carto.apps.web",
    "aidants_connect_carto.apps.api",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "csp.middleware.CSPMiddleware",
]

ROOT_URLCONF = "aidants_connect_carto.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "aidants_connect_carto.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if dj_database_url.config(conn_max_age=600):
    DATABASES = {"default": dj_database_url.config(conn_max_age=600)}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DATABASE_NAME"),
            "USER": os.getenv("DATABASE_USER"),
            "PASSWORD": os.getenv("DATABASE_PASSWORD"),
            "HOST": os.getenv("DATABASE_HOST"),
            "PORT": os.getenv("DATABASE_PORT"),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "fr"

TIME_ZONE = "Europe/Paris"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = "staticfiles"
STATIC_URL = "/static/"


# Security headers

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
REFERRER_POLICY = "strict-origin"


# Content security policy

_CSP_SELF = (
    "'self'",
    "'unsafe-inline'",
    "https://a.tile.openstreetmap.org/",
    "https://b.tile.openstreetmap.org/",
    "https://c.tile.openstreetmap.org/",
    "https://code.jquery.com/jquery-3.4.1.min.js",
)
CSP_DEFAULT_SRC = _CSP_SELF
CSP_IMG_SRC = _CSP_SELF + ("data:",)
CSP_SCRIPT_SRC = _CSP_SELF
CSP_STYLE_SRC = _CSP_SELF


# SSL security

SECURE_SSL_REDIRECT = False if os.getenv("SECURE_SSL_REDIRECT") == "False" else True
SECURE_HSTS_SECONDS = os.getenv("SECURE_HSTS_SECONDS", 0)


# Django Extensions: shell_plus

SHELL_PLUS_IMPORTS = [
    "from datetime import datetime, timedelta",
    "from aidants_connect_carto.apps.core import utilities",
]


# Django Extensions: graph_models

GRAPH_MODELS = {
    "all_applications": True,
    "group_models": True,
}


# django-modelsdoc: listing_models

MODELSDOC_DISPLAY_FIELDS = (
    ("Name", "name"),
    ("Fullname", "verbose_name"),
    ("Type", "db_type"),
    # ('PK', 'primary_key'),
    ("Unique", "unique"),
    # ('Index', 'db_index'),
    ("Null/Blank", "null_blank"),
    ("Comment", "comment"),
    ("Example", "help_text"),
)
MODELSDOC_MODEL_OPTIONS = (
    "unique_together",
    "index_together",
    "ordering",
)

MODELSDOC_FIELD_WRAPPER = "aidants_connect_carto.apps.core.documentation.modelsdoc_custom_field_wrapper.CustomFieldWrapper"


# Internal search engine settings

SEARCH_RESULTS_PER_PAGE = 30
