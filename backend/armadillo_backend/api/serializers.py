from rest_framework import serializers

from .models import SensorDataRaw


class ThermalSensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorDataRaw
        fields = '__all__'