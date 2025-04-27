from django.db import models


class Pool(models.Model):
    pool_id = models.AutoField(primary_key=True, default=0)
    pool_name = models.CharField(max_length=100, default='Крутой бассейн')
    pool_desc = models.CharField(max_length=255, default='0 ряд, 0 секция')
    rtsp_url = models.URLField(null=True)
    hls_url = models.URLField(null=True)
    temperature_sensor_id = models.IntegerField(null=True)
    oxygen_saturation_sensor_id = models.IntegerField(null=True)
    pH_sensor_id = models.IntegerField(null=True)
    orp_sensor_id = models.IntegerField(null=True)
    salinity_sensor_id = models.IntegerField(null=True)
    water_level_sensor_id = models.IntegerField(null=True)
    turbidity_sensor_id = models.IntegerField(null=True)
    ammonia_content_sensor_id = models.IntegerField(null=True)
    nitrite_content_sensor_id = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.pool_id} (№{self.pool_name}, {self.pool_desc})"


class PoolOptimalValues(models.Model):
    id = models.IntegerField(primary_key=True)
    pool_id = models.ForeignKey(Pool, on_delete=models.CASCADE)
    sensor = models.CharField(max_length=20, null=True)
    min = models.FloatField(null=True)
    max = models.FloatField(null=True)

    def __str__(self):
        return f"(updated optimal for {self.pool_id})"


class PoolStatistic(models.Model):
    pool_id = models.AutoField(primary_key=True, default=0)
    timestamp = models.DateTimeField(null=True)
    temperature = models.FloatField(null=True)
    oxygen_saturation = models.FloatField(null=True)
    pH = models.FloatField(null=True)
    orp = models.FloatField(null=True)
    salinity = models.FloatField(null=True)
    water_level = models.FloatField(null=True)
    turbidity = models.FloatField(null=True)
    ammonia_content = models.FloatField(null=True)
    nitrite_content = models.FloatField(null=True)

    def __str__(self):
        return f"{self.pool_id})"


class StatisticArduino(models.Model):
    pool_id = models.AutoField(primary_key=True, default=0)
    timestamp = models.DateTimeField(auto_now=True)
    temperature = models.FloatField(null=True)
    oxygen_saturation = models.FloatField(null=True)
    pH = models.FloatField(null=True)
    orp = models.FloatField(null=True)
    salinity = models.FloatField(null=True)
    water_level = models.FloatField(null=True)
    turbidity = models.FloatField(null=True)
    ammonia_content = models.FloatField(null=True)
    nitrite_content = models.FloatField(null=True)


class ControlThingsArduino(models.Model):
    pool_id = models.AutoField(primary_key=True, default=0)
    freezer = models.BooleanField(default=False)
    feeder = models.BooleanField(default=False)