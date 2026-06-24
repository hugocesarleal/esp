from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # Interface Web
    path('api/numero/', views.api_get_numero, name='api_get_numero'), # Rota do ESP32
]