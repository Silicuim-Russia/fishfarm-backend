from django.db import models


class Pool(models.Model):
    pool_id = models.AutoField(primary_key=True)
    pool_name = models.CharField(max_length=100)
    pool_desc = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.pool_id} (№{self.pool_name}, {self.pool_desc})"


class PoolOptimalValues(models.Model):
    min_temperature = models.FloatField()
    max_temperature = models.FloatField()
    min_oxygen_saturation = models.FloatField()
    max_oxygen_saturation = models.FloatField()
    min_pH = models.FloatField()
    max_pH = models.FloatField()
    min_orp = models.FloatField()
    max_orp = models.FloatField()
    min_salinity = models.FloatField()
    max_salinity = models.FloatField()
    min_water_level = models.FloatField()
    max_water_level = models.FloatField()
    min_turbidity = models.FloatField()
    max_turbidity = models.FloatField()
    min_ammonia_content = models.FloatField()
    max_ammonia_content = models.FloatField()
    min_nitrite_content = models.FloatField()
    max_nitrite_content = models.FloatField()
    temperature_sensor_id = models.IntegerField()
    oxygen_saturation_sensor_id = models.IntegerField()
    pH_sensor_id = models.IntegerField()
    orp_sensor_id = models.IntegerField()
    salinity_sensor_id = models.IntegerField()
    water_level_sensor_id = models.IntegerField()
    turbidity_sensor_id = models.IntegerField()
    ammonia_content_sensor_id = models.IntegerField()
    nitrite_content_sensor_id = models.IntegerField()


class PoolStatistic(models.Model):
    pool_id = models.ForeignKey(Pool, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    temperature = models.FloatField()
    oxygen_saturation = models.FloatField()
    pH = models.FloatField()
    salinity = models.FloatField()
    water_lavel = models.FloatField()
    turbidity = models.FloatField()
    ammonia_content = models.FloatField()
    nitrite_content = models.FloatField()

    def __str__(self):
        return f"{self.pool_id})"
