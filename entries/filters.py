import django_filters
from django_filters import CharFilter
from entries.models import Student_info

class StudentFilter(django_filters.FilterSet):

    class Meta:
        model = Student_info
        fields = ['nsu_id']
        