import os

from .base import *  # noqa

# from .base import BASE_DIR

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-an!y*cr0ho%qwq(@tl(0fo1b#d%%k98oujtx&66ii9dk0*afzv",
)

DEBUG = os.environ.get("DJANGO_DEBUG", True)

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "bit68",
        "USER": "faresemad",
        "PASSWORD": "test@123",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
