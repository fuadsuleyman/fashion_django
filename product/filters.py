import django_filters
from django_filters import CharFilter
from .models import *

class ProductFilter(django_filters.FilterSet):
    title = CharFilter(lookup_expr='iexact', label='')

    class Meta:
        model = Product  
        fields = ['title']
