import logging
from django.db.models.functions import Lower
from django.http import JsonResponse
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets, mixins
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.generics import UpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.renderers import JSONRenderer

from . import models
from lib.constants import Actions, Method
from lib.paginators import CustomPagination
from django.contrib.auth.models import User
from core.serializers import RegisterSerializer, UserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

logger = logging.getLogger(__name__)


class BaseGenericViewSet(viewsets.GenericViewSet):
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)


class BaseViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    dynamic_serializers = {}
    http_method_names = [
        Method.GET, Method.HEAD, Method.OPTIONS, Method.POST, Method.PATCH, Method.PUT,
        Method.DELETE
    ]

    def get_serializer_class(self):
        serializer_dict = self.dynamic_serializers

        if not serializer_dict:
            return self.serializer_class

        request_action = self.action
        if request_action == Actions.LIST:
            return serializer_dict[request_action]
        return serializer_dict[Actions.Retrieve]

    @action(methods=[Method.GET], detail=True)
    def view(self, queryset, pk, *args, **kwargs):
        obj = self.get_object()
        serializer = self.dynamic_serializers[self.action](obj, context={'request': self.request})
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()


class RegisterView(generics.CreateAPIView, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserViewSet(BaseGenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    pagination_class = CustomPagination


