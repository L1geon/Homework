from django.db import models


class Sensor(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(null=True, max_length=100)


class Measurement(models.Model):
    sensorID = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    measurement = models.IntegerField()
    date_create = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)
