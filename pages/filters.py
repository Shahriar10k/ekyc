import django_filters
from django_filters import CharFilter
from entries.models import Course

class courseFilter(django_filters.FilterSet):

    class Meta:
        model = Course
        fields = ['couse_code']