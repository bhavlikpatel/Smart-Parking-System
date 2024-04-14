import django_filters
from django.db.models import Q
from django_filters.filters import OrderingFilter
from functools import reduce

from parking_app.models import FixedSlot
from . import models


class FixedSlotFilter(django_filters.FilterSet):
    plot = django_filters.CharFilter(field_name='plot',method="filter_plot_wise_slots", label='Plot')

    class Meta:
        model = FixedSlot
        fields = ('plot',)

    def filter_plot_wise_slots(self, queryset, value, *args, **kwargs):
        if args:
            plot_id = args[0]
            project = self.Meta.model.objects.get(plot=plot_id)
            return queryset.filter(branch=project.branch)
        return queryset



