from django.contrib import admin
from django.urls import path,  include
from djoser.views import TokenCreateView, TokenDestroyView
from core.views import RegisterView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('parking_app.urls')),
    path('api/v1/admin/', include('admin_management.urls')),
    path('login/', TokenCreateView.as_view(), name='login'),
    path('logout/', TokenDestroyView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),

]
