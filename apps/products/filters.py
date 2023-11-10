from django_filters import rest_framework as filters

from apps.products.models import Package


class PackageFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Package
        fields = ["name"]
