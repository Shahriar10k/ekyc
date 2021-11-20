import django_filters
from django_filters import CharFilter
from customer.models import Customer_info

class CustomerFilter(django_filters.FilterSet):

    class Meta:
        model = Customer_info
        fields = ['id']