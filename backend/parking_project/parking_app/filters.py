import django_filters
from django.db.models import Q
from django_filters.filters import OrderingFilter
from functools import reduce

from .models import FixedSlot


class FixedSlotFilter(django_filters.FilterSet):
    class Meta:
        model = FixedSlot
        fields = ('plot',)




