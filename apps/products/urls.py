from rest_framework.routers import DefaultRouter

from apps.products.views import PackageViewSet, SubscriptionViewSet

router = DefaultRouter()

router.register("packages", PackageViewSet, basename="packages")
router.register("subscriptions", SubscriptionViewSet, basename="subscriptions")

urlpatterns = router.urls
