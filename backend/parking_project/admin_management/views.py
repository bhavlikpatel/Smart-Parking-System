import logging
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from core.views import BaseViewSet, BaseGenericViewSet
from lib.constants import Actions, Method
from django.contrib.auth.models import User
from .serializers import UserAdminSerializer
from lib.constants import Method
from rest_framework import generics
from django.db.models.functions import Coalesce
from django.db.models import Sum, F, Avg, Value, Q, Count, ExpressionWrapper, Case, When
from parking_app.serializers import FixedSlotSerializer
from . import serializers
from . import models
from parking_app import models as parking_app_models
from rest_framework.decorators import action
from rest_framework.response import Response
from lib.paginators import CustomPagination
from rest_framework import status
from rest_framework import mixins
from rest_framework import views
from . import helpers
from datetime import timedelta, datetime
from parking_app import constants
from . import filters

logger = logging.getLogger(__name__)


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days + 1)):
        yield start_date + timedelta(n)


class AdminDashboardViewSet(BaseGenericViewSet):
    serializer_class = parking_app_models.FixedSlot

    @action(methods=['get'], detail=False)
    def scoreboard(self, request, *args, **kwargs):
        s_d = request.query_params.get('start_date', None)
        e_d = request.query_params.get('end_date', None)
        start_date, end_date = helpers.manage_start_end_date(s_d, e_d, duration=7)
        duration_days = (end_date - start_date).days
        total_fixed_slots = parking_app_models.FixedSlot.objects.all()
        fixed_slots_count = total_fixed_slots.count()
        plots = models.Plot.objects.all()
        plot_count = plots.count()
        user_slots = parking_app_models.Slot.objects.filter(slot_date__range=(start_date, end_date)).distinct()
        data = user_slots.aggregate(
            total_payment=Coalesce(
                Sum('amount'),
                Value(0)
            ), )

        user_slot_count = user_slots.count()
        avg_slot_utilization = round((int(user_slot_count) * 100) / (int(fixed_slots_count) * int(duration_days)))
        scoreboard = {
            "total_fixed_slots": fixed_slots_count * duration_days,
            "total_plot": plot_count * duration_days,
            "avg_slot_utilization": avg_slot_utilization,
            "user_slot_count": user_slot_count,
            "total_payment": data['total_payment']
        }
        return Response(data={"scoreboard": scoreboard}, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False)
    def slots_booking_chart(self, request, *args, **kwargs):
        s_d = request.query_params.get('start_date', None)
        e_d = request.query_params.get('end_date', None)

        start_date, end_date = helpers.manage_start_end_date(s_d, e_d, duration=7)
        utilized_slots = []
        for date in daterange(start_date, end_date):
            slots = parking_app_models.Slot.objects.filter(created__date=date)
            if slots:
                utilized_slots.append({
                    f"{date}": slots.count()
                })
            else:
                utilized_slots.append({
                    f"{date}": 0
                })
        return Response(data={"utilized_slots": utilized_slots}, status=status.HTTP_200_OK)


# Create your views here.
class AccountAdminView(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, BaseGenericViewSet):
    queryset = User.objects.filter(is_superuser=True)
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    search_fields = ("first_name", "last_name", "username", "email")
    serializer_class = UserAdminSerializer
    pagination_class = CustomPagination


class PlotViewSet(BaseViewSet):
    pagination_class = CustomPagination
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    search_fields = ('plot_name', 'plot_id', 'city')

    dynamic_serializers = {
        Actions.LIST: serializers.PlotSerializer,
        Actions.Retrieve: serializers.PlotSerializer,
        Actions.VIEW: serializers.PlotSerializer
    }

    def get_queryset(self):
        queryset = models.Plot.objects.all()
        return queryset

    @action(methods=[Method.DELETE], detail=True)
    def delete_plot(self, request, pk, *args, **kwargs):
        try:
            plot_name = None
            plot = self.get_object()
            if plot:
                plot_name = plot.plot_name
                plot.delete()
        except Exception as e:
            return Response(data={"errors": "Plot Does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"message": f"Plot {plot_name} delete successfully"}, status=status.HTTP_200_OK)


class AdminFixedSlotView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        plot_id = self.request.data.get('plot_id')
        slot_size = self.request.data.get('slot_size')
        try:
            plot = models.Plot.objects.get(id=plot_id)
        except Exception as e:
            return Response({"errors": "Plot ID Does Not Exist"}, status=status.HTTP_400_BAD_REQUEST)
        fixed_slot_list = []
        created_slot_count = 0
        last_slot = parking_app_models.FixedSlot.objects.last()

        slot_id = int(last_slot.id) + 1 if last_slot else 1
        start = slot_id
        end = int(slot_id) + int(slot_size)
        for i in range(start, end):
            fixed_slot_list.append(parking_app_models.FixedSlot(
                plot=plot, slot_id=i
            ))
            created_slot_count += 1
        if fixed_slot_list:
            parking_app_models.FixedSlot.objects.bulk_create(fixed_slot_list)
        return Response(data={"message": f"{created_slot_count} slots created"}, status=status.HTTP_200_OK)


class AdminFixedSlotListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                                BaseGenericViewSet):
    serializer_class = FixedSlotSerializer
    queryset = parking_app_models.FixedSlot.objects.all()
    pagination_class = CustomPagination
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    search_fields = ('plot__plot_name', 'plot__plot_id', 'slot_id', 'plot__id', 'id')

