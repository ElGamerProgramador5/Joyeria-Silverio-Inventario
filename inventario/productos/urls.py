from django.urls import path
from . import views

urlpatterns = [
    path('', views.panel_inventario, name='panel_control'),
]
