from django.contrib import admin
from django.urls import include, path

api_prefix = "api/v1/"
urlpatterns = [
    path("admin/", admin.site.urls),
    path(f"{api_prefix}users/", include("apps.accounts.urls")),
    path(f"{api_prefix}products/", include("apps.products.urls")),
]
