
from django.contrib import admin
from django.urls import path,include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),\
    path('create/', views.create_log, name='create_log'),
    path('success/', views.log_success, name='log_success'),  # Vista para la redirección
    path('', views.home, name='home'),
    path("__reload__/", include("django_browser_reload.urls")),
]
