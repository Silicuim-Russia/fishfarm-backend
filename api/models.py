from django.db import models
from datetime import datetime


class Pool(models.Model):
    pool_id = models.AutoField(primary_key=True, default=0)
    pool_name = models.CharField(max_length=100, default='Новый бассейн')
    pool_desc = models.CharField(max_length=255, default='0 ряд, 0 секция')
    timestamp = models.DateTimeField(auto_now=True, null=True)
    health_percents = models.IntegerField(null=True, default=0)
    health_zone = models.CharField(max_length=10, null=True, default='danger')

    def __str__(self):
        return f"{self.pool_id} ({self.pool_name}, {self.pool_desc})"


class PoolOptimalValues(models.Model):
    pool_id = models.ForeignKey(Pool, on_delete=models.CASCADE)
    sensor = models.CharField(max_length=20, null=True)
    min = models.FloatField(null=True, default=0)
    max = models.FloatField(null=True, default=0)

    def __str__(self):
        return f"({self.sensor} optimal for Бассейна {self.pool_id})"


class PoolStatistic(models.Model):
    pool_id = models.AutoField(primary_key=True, default=0)
    timestamp = models.DateTimeField(auto_now=True, null=True)
    temperature = models.FloatField(null=True, default=0)
    oxygen_saturation = models.FloatField(null=True, default=0)
    pH = models.FloatField(null=True, default=0)
    orp = models.FloatField(null=True, default=0)
    salinity = models.FloatField(null=True, default=0)
    water_level = models.FloatField(null=True, default=0)
    turbidity = models.FloatField(null=True, default=0)
    ammonia_content = models.FloatField(null=True, default=0)
    nitrite_content = models.FloatField(null=True, default=0)

    def __str__(self):
        return f"{self.pool_id})"


class StatisticArduino(models.Model):
    pool_id = models.AutoField(primary_key=True, default=0)
    timestamp = models.DateTimeField(auto_now=True, null=True)
    temperature = models.FloatField(null=True, default=0)
    oxygen_saturation = models.FloatField(null=True, default=0)
    pH = models.FloatField(null=True, default=0)
    orp = models.FloatField(null=True, default=0)
    salinity = models.FloatField(null=True, default=0)
    water_level = models.FloatField(null=True, default=0)
    turbidity = models.FloatField(null=True, default=0)
    ammonia_content = models.FloatField(null=True, default=0)
    nitrite_content = models.FloatField(null=True, default=0)


class PoolStream(models.Model):
    pool_id = models.AutoField(primary_key=True, default=0)
    stream_name = models.CharField(null=True, max_length=50)
    rtsp_url = models.TextField(null=True)
    transcode_pid = models.IntegerField(default=0)
