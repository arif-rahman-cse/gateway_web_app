from django.db import models

# Create your models here.
class SensorDataRaw(models.Model):
    id = models.UUIDField(primary_key=True)
    sensor_value = models.JSONField()
    time = models.DateTimeField()
    bachflg = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensor_data_raw'