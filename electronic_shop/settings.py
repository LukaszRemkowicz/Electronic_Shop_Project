from pathlib import Path
import os
import logging.config

from dotenv import load_dotenv

from django.contrib.messages import constants as messages

from .const import LOCAL_DB, IS_DOCKER


dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# print(os.environ)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "Profile.apps.ProfileConfig",
    # 'Profile',
    "ProductApp.apps.ProductappConfig",
    "AddressBookApp.apps.AddressbookappConfig",
    "MessagesApp.apps.MessagesappConfig",
    "ShoppingCardApp.apps.ShoppingcardappConfig",
    "Articles.apps.ArticlesConfig",
    "Emails.apps.EmailsConfig",
    "Landingpage.apps.LandingpageConfig",
    "API.apps.ApiConfig",
    "widget_tweaks",
    "reset_migrations",
    "rest_framework.authtoken",
    "rest_framework",
    "django_filters",
    "django.contrib.humanize",
    # 'ckeditor',
    "mptt",
    "electronic_shop",
    # "debug_toolbar",
]

MIDDLEWARE = [
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # 'electronic_shop.middlewere.LoginFormMiddleware',
]

ROOT_URLCONF = "electronic_shop.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "electronic_shop.custom_context_processor.login_form_content",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# TEMPLATE_CONTEXT_PROCESSORS = (
#     "electronic_shop.custom_context_processor.login_form_content",
# )

WSGI_APPLICATION = "electronic_shop.wsgi.application"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases



def choose_db(db):
    return [
        os.getenv(f"{db}_NAME"),
        os.getenv(f"{db}_USER"),
        os.getenv(f"{db}_PASSWORD"),
        os.getenv(f"{db}_HOST"),
        5432 if db == "LOCAL" else os.getenv("DROPLET_PORT"),
        {},
    ]

if LOCAL_DB:
    name, user, password, host, port, options= choose_db('LOCAL')

else:
    name, user, password, host, port, options = choose_db("DROPLET")

if IS_DOCKER:
    name = os.getenv("DOCKER_DB_NAME")
    host = "db"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": name,
        "USER": user,
        "PASSWORD": password,
        "HOST": host,
        "PORT": port,
        "OPTIONS": options,
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": os.getenv("DB_NAME"),
#         "USER": os.getenv("DB_USER"),
#         "PASSWORD": os.getenv("DB_PASSWORD"),
#         "HOST": os.getenv("DB_HOST"),
#         "PORT": 5432,
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Warsaw"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/media/"


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "electronic_shop/static"),
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "media"),
]

# STATIC_ROOT = os.path.join(BASE_DIR, "static")

# STATIC_ROOT = '/vol/web/static'
# MEDIA_ROOT = '/vol/web/media'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

LOGIN_URL = "landing-page"

# AUTH_USER_MODEL = 'auth.User'
AUTH_USER_MODEL = "Profile.User"


REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.authentication.TokenAuthentication",
    ),
    # 'DEFAULT_PARSER_CLASSES': [
    #     'rest_framework.parsers.JSONParser',
    # ]
}

INTERNAL_IPS = ["127.0.0.1"]


# def show_toolbar(request):
#     return True


# DEBUG_TOOLBAR_CONFIG = {
#     "SHOW_TOOLBAR_CALLBACK": show_toolbar,
# }


def get_logging_structure(LOGFILE_ROOT):
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': "[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s] %(message)s",
                'datefmt': "%d/%b/%Y %H:%M:%S"
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'profiles_file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOGFILE_ROOT, 'profiles.log'),
                'formatter': 'verbose'
            },
            'data_log_file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOGFILE_ROOT, 'data.log'),
                'formatter': 'verbose'
            },
            'django_log_file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOGFILE_ROOT, 'django.log'),
                'formatter': 'verbose'
            },
            'proj_log_file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOGFILE_ROOT, 'project.log'),
                'formatter': 'verbose'
            },
            'route_updater': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(LOGFILE_ROOT, 'route.updater.log'),
                'formatter': 'verbose'
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            }
        },
        'loggers': {
            'profiles': {
                'handlers': ['console', 'profiles_file'],
                'level': 'DEBUG',
            },

            'django': {
                'handlers': ['django_log_file'],
                'propagate': True,
                'level': 'ERROR',
            },
            'project': {
                'handlers': ['proj_log_file'],
                'level': 'DEBUG',
            },
            'route_updater': {
                'handlers': ['console', 'route_updater'],
                'level': 'DEBUG',
            },
        }
    }

# Reset logging
# (see http://www.caktusgroup.com/blog/2015/01/27/Django-Logging-Configuration-logging_config-default-settings-logger/)
LOGGING_CONFIG = None
LOGGING = get_logging_structure('_logs')
logging.config.dictConfig(LOGGING)

logger = logging.getLogger(f'project.{__name__}')
