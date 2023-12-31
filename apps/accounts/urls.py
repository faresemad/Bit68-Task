from django.urls import path

from .views import user_login, user_registration

urlpatterns = [
    path("register/", user_registration, name="user-registration"),
    path("login/", user_login, name="user-login"),
]
