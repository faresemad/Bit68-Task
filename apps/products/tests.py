import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from apps.products.models import Package, Subscription

User = get_user_model()


class PackageTestCase(TestCase):
    def setUp(self):
        Package.objects.create(name="Package1", price=100)
        Package.objects.create(name="Package2", price=200)

    def test_package(self):
        package1 = Package.objects.get(name="Package1")
        package2 = Package.objects.get(name="Package2")
        self.assertEqual(package1.name, "Package1")
        self.assertEqual(package2.name, "Package2")
        self.assertEqual(package1.price, 100)
        self.assertEqual(package2.price, 200)

    def test_package_ordering(self):
        packages = Package.objects.all()
        self.assertEqual(packages[0].name, "Package1")
        self.assertEqual(packages[1].name, "Package2")
        self.assertEqual(packages[0].price, 100)
        self.assertEqual(packages[1].price, 200)

    def test_package_str(self):
        package1 = Package.objects.get(name="Package1")
        package2 = Package.objects.get(name="Package2")
        self.assertEqual(package1.__str__(), "Package1")
        self.assertEqual(package2.__str__(), "Package2")

    def test_package_get_absolute_url(self):
        package1 = Package.objects.get(name="Package1")
        package2 = Package.objects.get(name="Package2")
        self.assertEqual(package1.get_absolute_url(), "/products/package/1/")
        self.assertEqual(package2.get_absolute_url(), "/products/package/2/")


class SubscriptionTestCase(TestCase):
    def setUp(self):
        Package.objects.create(name="Package1", price=100)
        Package.objects.create(name="Package2", price=200)
        Package.objects.create(name="Package3", price=300)
        Package.objects.create(name="Package4", price=400)

        user = User.objects.create(username="testuser", password="testpassword")
        Subscription.objects.create(user=user)

    def test_subscription(self):
        subscription = Subscription.objects.get(user__username="testuser")
        self.assertEqual(subscription.user.username, "testuser")
        self.assertEqual(subscription.packages.count(), 0)
        self.assertEqual(subscription.timestamp, datetime.datetime(2019, 1, 1, 0, 0))

    def test_subscription_ordering(self):
        subscription = Subscription.objects.get(user__username="testuser")
        self.assertEqual(subscription.user.username, "testuser")
        self.assertEqual(subscription.packages.count(), 0)
        self.assertEqual(subscription.timestamp, datetime.datetime(2019, 1, 1, 0, 0))

    def test_subscription_str(self):
        subscription = Subscription.objects.get(user__username="testuser")
        self.assertEqual(subscription.__str__(), "testuser")

    def test_subscription_get_absolute_url(self):
        subscription = Subscription.objects.get(user__username="testuser")
        self.assertEqual(subscription.get_absolute_url(), "/products/subscribe/1/")
