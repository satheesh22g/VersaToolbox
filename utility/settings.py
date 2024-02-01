"""
Django settings for utility project.

Generated by 'django-admin startproject' using Django 3.2.19.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@rnlzud8lpc7u6byqr9q6@@z4m%^w#@b$i)hexklg+*7)+$!$d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']



AUTH_USER_MODEL = 'users.CustomUser'



LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',  # This should point to your static directory
    os.path.join(BASE_DIR, 'rest_framework', 'static'),
]

#AUTH_USER_MODEL = 'authentications.User'


INSTALLED_APPS = [
    'qr_maker.apps.QrMakerConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'extract',
    'plagiarism',
    'api',
    'rest_framework',
    'fetch_data',
    'TextForge',
    'quotegenerator',
    'convertor',
    'mealrecipes',
     'users',
     'calories_tracker',
     'bootstrap4',
     'expense_tracker',
     'quiz',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'quiz.middleware.QuizRestrictionMiddleware',

]

ROOT_URLCONF = 'utility.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # Add paths to your template directories
            os.path.join(BASE_DIR, 'extract/templates'),
            os.path.join(BASE_DIR, 'qr_maker/templates'),
            # ... other directories
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'users.context_processors.common_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'utility.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTHENTICATION_BACKENDS = [
    'users.backends.CustomUserAuthentication',
    'django.contrib.auth.backends.ModelBackend',
    # ... other backends
]

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_TZ = False

# TIME_ZONE = 'UTC' 

TIME_ZONE = 'Asia/Kolkata'


USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# Set session timeout to 15 minutes (900 seconds)
SESSION_COOKIE_AGE = 900
# Save the session on every request
SESSION_SAVE_EVERY_REQUEST = True