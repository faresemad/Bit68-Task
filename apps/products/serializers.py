from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.products.models import Package, Subscription

User = get_user_model()


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = "__all__"


class SubscriptionPOSTSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Subscription
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
        ]


class SubscriptionGETSerializer(serializers.ModelSerializer):
    packages = PackageSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Subscription
        fields = "__all__"
