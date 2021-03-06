"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

from environs import Env

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# We want to protect our secret key below, so we add it to our .env file and reference it here. When adding it to our .env file, leave out the quotes!
# I've generated a new secret key so the below is not valid. Using:
# python -c "import secrets; print(secrets.token_urlsafe())"
# old SECRET_KEY = 'dz&(zq9!tx^sl8abb_6(+4316f)530shyt=nr2nqvs1yypp0vp'
SECRET_KEY = env.str("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# DEBUG = False
# When we set the above to False and save it our local server will stop because django assumes we are trying to push the project into live production. We need to update ALLOWED_HOSTS below to fix it.
# We want DEBUG=True to be true for our local dev, but false for production. To do this we add the debug to our .env file and have it exported to be read from this file. We rewrite the code to look like so:
DEBUG = env.bool("DEBUG", default=False)
# What's in the quotes is what we used as the name in our .env file. It could technically be anything we want and not using the same "DEBUG" to reference the debug here in this file.
# DEBUG = env.bool("ANYTHING")
# Best practice is to set a default value, in this case False, meaning that if an environment variable can't be found, our production setting will be used. This is to avoid exposing secrets to the open.

ALLOWED_HOSTS = ['.herokuapp.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    
    "whitenoise.runserver_nostatic",
    
    'django.contrib.staticfiles',
    
    # 3rd Party
    "crispy_forms",
    
    # Our apps
    "accounts",
    "pages",
    "articles",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    
    "whitenoise.middleware.WhiteNoiseMiddleware",
    
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath("templates"))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# Our current database configuration is for SQLite, but we want to be able to switch to PostgreSQL for production on Heroku. When we installed environs, it takes all the db configurations needed for our db (SQ or POSTgreS) and creates a DATABASE_URL environment variable.
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Update our db to the following
# Afterwards we specify the specific SQL in our .env file.
DATABASES = {
    "default": env.dj_db_url("DATABASE_URL")
}
# We need to install Psycopg which is a db adapter that lets python apps tal to PostgreSQL db. Heroku needs it in deployment
# pipenv install psycopg2-binary

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# We want to use our own User model in place of the built in one. So we specify the below to do so.
AUTH_USER_MODEL = "accounts.CustomUser"

# Creating redirect for login and logout
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

# config/settings.py
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Adding functionality for emailing user if they forgot their password.
# /accounts/password_reset/
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# Modifying the above to use sendgrid emails using smtp
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# The below block of code is needed to be able to send the emails
# We should be using environment variables, and not plain text. As such i'll be omitting the below for now.
DEFAULT_FROM_EMAIL = 'your_custom_email_account'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = 'sendgrid_password'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
