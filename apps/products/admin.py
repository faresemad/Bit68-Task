from django.contrib import admin

from apps.products.models import Package, Subscription


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
    search_fields = ["name", "price"]


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["user", "timestamp"]
    search_fields = ["user", "timestamp"]
