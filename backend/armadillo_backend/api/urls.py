from django.urls import path

from . import views

urlpatterns = [
    path('thermal-sensor-data/', views.ThermalSensorDataView.as_view(), name='thermal-sensor-data'),
]