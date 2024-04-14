from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from core import views as core_views
from admin_management import views as admin_views

router = DefaultRouter()

router.register('fixed_slots', views.FixedSlotListViewSet, basename='fixed_slots')
router.register('plot_slots', views.PlotSlotListViewSet, basename='plot-slots')
router.register('slots', views.SlotViewSet, basename='slots')
router.register('users', core_views.UserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls)),
]
