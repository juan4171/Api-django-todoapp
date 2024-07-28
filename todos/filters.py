import django_filters
from .models import Todo

class TodoFilter(django_filters.FilterSet):
    datecompleted_null = django_filters.BooleanFilter(field_name='datecompleted', lookup_expr='isnull')

    class Meta:
        model = Todo
        fields = ['datecompleted_null']