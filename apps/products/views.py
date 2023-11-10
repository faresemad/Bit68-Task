from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from apps.products.filters import PackageFilter
from apps.products.models import Package, Subscription
from apps.products.serializers import PackageSerializer, SubscriptionGETSerializer, SubscriptionPOSTSerializer


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all().order_by("price")
    serializer_class = PackageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PackageFilter

    def get_permissions(self):
        if self.action == "list" or self.action == "retrieve":
            return [IsAuthenticated()]
        else:
            return [IsAdminUser()]


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return SubscriptionGETSerializer
        else:
            return SubscriptionPOSTSerializer


class UserSubscriptions(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Returns all subscriptions of the user
    """

    queryset = Subscription.objects.all()
    serializer_class = SubscriptionGETSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)
