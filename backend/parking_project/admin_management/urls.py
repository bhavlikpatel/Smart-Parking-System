from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('fixed_slots', views.AdminFixedSlotListViewSet, basename='admin-fixed-slots')
router.register('dashboard', views.AdminDashboardViewSet, basename='admin-dashboard')
router.register('plots', views.PlotViewSet, basename='plots')
router.register('users', views.AccountAdminView, basename='admin-register')

urlpatterns = [
    path('create_fixed_slots/', views.AdminFixedSlotView.as_view(), name="create_fixed_slots"),
    path('', include(router.urls)),
]
