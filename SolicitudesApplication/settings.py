"""
Django settings for SolicitudesApplication project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3dnaamr5!-76uqjoz)hnc-0pqfj#e(t83jx^ll)5m7uqnzx7ql'

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
    'solicitudes',
    'rest_framework',
    'clientes',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SolicitudesApplication.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'SolicitudesApplication.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'UsersAndSol',
        'USER': 'admin',
        'PASSWORD': 'isis2503',
        'HOST': '172.23.192.7',
        'PORT': '',
    },
}



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = "/login/auth0" 
LOGIN_REDIRECT_URL = "" 
LOGOUT_REDIRECT_URL = "https://isis2503trodriten.us.auth0.com/v2/logout?returnTo=http%3A%2F%2Fhttps://bancolosalpes.xyz" 
SOCIAL_AUTH_TRAILING_SLASH = False # Remove end slash from routes 
SOCIAL_AUTH_AUTH0_DOMAIN = 'isis2503trodriten.us.auth0.com' 
SOCIAL_AUTH_AUTH0_KEY = 'qukDwvWR7N4OHN8T9KdcPXdTDUWRn83S' 
SOCIAL_AUTH_AUTH0_SECRET = 'ZAZh2WA1WSwhUGbViyp0X95hlEA7Boq4Z9a81isVrJn5OYNszKAHRnihI-YH3gdG' 
SOCIAL_AUTH_AUTH0_SCOPE = [ 'openid', 'profile','email','role', ] 
AUTHENTICATION_BACKENDS = { 'SolicitudesApplication.auth0backend.Auth0', 'django.contrib.auth.backends.ModelBackend', }
