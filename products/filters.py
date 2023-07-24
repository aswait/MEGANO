from django_filters import rest_framework as filters


from .models import Product


class ProductFilter(filters.FilterSet):
    filter = filters.D