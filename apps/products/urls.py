from rest_framework.routers import DefaultRouter

from apps.products.views import PackageViewSet, SubscriptionViewSet, UserSubscriptions

router = DefaultRouter()

router.register("packages", PackageViewSet, basename="packages")
router.register("subscribe", SubscriptionViewSet, basename="scriptions")
router.register("user-subscriptions", UserSubscriptions, basename="user-subscriptions")

urlpatterns = router.urls
