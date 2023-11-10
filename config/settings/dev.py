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
        "NAME": env("DB_NAME", default="bit68"),
        "USER": env("DB_USER", default="faresemad"),
        "PASSWORD": env("DB_PASSWORD", default="test@123"),
        "HOST": env("DB_HOST", default="localhost"),
        "PORT": env("DB_PORT", default="5432"),
    }
}
