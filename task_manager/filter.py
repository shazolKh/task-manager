import django_filters

from .models import *


class AllFilter(django_filters.FilterSet):
    class Meta:
        module = Task
        fields = '__all__'
