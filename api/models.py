from django.db import models


class Pool(models.Model):
    pool_id = models.AutoField(primary_key=True, default=0)
    pool_name = models.CharField(max_length=100, default='Крутой бассейн')
    pool_desc = models.CharField(max_length=255, default='0 ряд, 0 секция')
    url = models.URLField(null=True)
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
    pool_id = models.AutoField(primary_key=True, default=0)
    min_temperature = models.FloatField(null=True, default=22.0)
    max_temperature = models.FloatField(null=True, default=24.0)
    min_oxygen_saturation = models.FloatField(null=True, default=7.5)
    max_oxygen_saturation = models.FloatField(null=True, default=9.0)
    min_pH = models.FloatField(null=True, default=6.5)
    max_pH = models.FloatField(null=True, default=8.0)
    min_orp = models.FloatField(null=True, default=100.0)
    max_orp = models.FloatField(null=True, default=250.0)
    min_salinity = models.FloatField(null=True, default=10.0)
    max_salinity = models.FloatField(null=True, default=12.0)
    min_water_level = models.FloatField(null=True, default=50.0)
    max_water_level = models.FloatField(null=True, default=70.0)
    min_turbidity = models.FloatField(null=True, default=5.0)
    max_turbidity = models.FloatField(null=True, default=10.0)
    min_ammonia_content = models.FloatField(null=True, default=0.0)
    max_ammonia_content = models.FloatField(null=True, default=0.07)
    min_nitrite_content = models.FloatField(null=True, default=0.0)
    max_nitrite_content = models.FloatField(null=True, default=0.1)



class PoolStatistic(models.Model):
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

    def __str__(self):
        return f"{self.pool_id})"
