import os

from .base import *  # noqa

# from .base import BASE_DIR

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-an!y*cr0ho%qwq(@tl(0fo1b#d%%k98oujtx&66ii9dk0*afzv",
)

DEBUG = os.environ.get("DJANGO_DEBUG", False)

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost,example.com").split(",")


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME", "test"),
        "USER": os.environ.get("DB_USER", "test"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "test"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}
