from .base import *  # noqa
from .base import env

# GENERAL
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-an!y*cr0ho%qwq(@tl(0fo1b#d%%k98oujtx&66ii9dk0*afzv",
)

DEBUG = env.bool("DJANGO_DEBUG", True)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])


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
