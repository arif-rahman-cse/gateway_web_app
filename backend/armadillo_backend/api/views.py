
from rest_framework import generics
from . import models
from . import serializers

# Create your views here.
class ThermalSensorDataView(generics.ListAPIView):
    # Get first entry in table that has bachflg=99
    queryset = models.SensorDataRaw.objects.filter(bachflg=99, id = "8ec009c9-674a-45ca-b019-f730ef60e8f1")
    serializer_class = serializers.ThermalSensorDataSerializer

    
