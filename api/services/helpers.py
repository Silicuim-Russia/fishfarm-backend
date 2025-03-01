from ..models import Pool, PoolOptimalValues, PoolStatistic


class PoolManagment:
    def __init__(self):
        self.data = Pool.objects
    def take_data(self, pool_id):
        if self.data.filter(pool_id=pool_id).exists():
            to_return = self.data.filter(pool_id=pool_id)
            return to_return
        else:
            print(f'pool {pool_id} does`t exists')
            return []
    def write_data(self, pool_id, pool_name, pool_desc, url,
                   temperature_sensor_id, oxygen_saturation_sensor_id,
                   pH_sensor_id, orp_sensor_id, salinity_sensor_id,
                   water_level_sensor_id, turbidity_sensor_id,
                   ammonia_content_sensor_id, nitrite_content_sensor_id):
        if self.data.filter(pool_id=pool_id).exists():
            now_data = self.data.filter(pool_id=pool_id)
            now_data.pool_name = pool_name
            now_data.pool_desc = pool_desc
            now_data.url = url
            now_data.temperature_sensor_id = temperature_sensor_id
            now_data.oxygen_saturation_sensor_id = oxygen_saturation_sensor_id
            now_data.pH_sensor_id = pH_sensor_id
            now_data.orp_sensor_id = orp_sensor_id
            now_data.salinity_sensor_id = salinity_sensor_id
            now_data.water_level_sensor_id = water_level_sensor_id
            now_data.turbidity_sensor_id = turbidity_sensor_id
            now_data.ammonia_content_sensor_id = ammonia_content_sensor_id
            now_data.nitrite_content_sensor_id = nitrite_content_sensor_id
            now_data.save()
            print(f'pool info {pool_id} successfully rewrite')
            return True
        else:
            new_pool = Pool(
                pool_id=pool_id,
                pool_name=pool_name,
                pool_desc=pool_desc,
                url=url,
                temperature_sensor_id=temperature_sensor_id,
                oxygen_saturation_sensor_id=oxygen_saturation_sensor_id,
                pH_sensor_id=pH_sensor_id,
                orp_sensor_id=orp_sensor_id,
                salinity_sensor_id=salinity_sensor_id,
                water_level_sensor_id=water_level_sensor_id,
                turbidity_sensor_id=turbidity_sensor_id,
                ammonia_content_sensor_id=ammonia_content_sensor_id,
                nitrite_content_sensor_id =nitrite_content_sensor_id
            )
            new_pool.save()
            print(f'pool {pool_id} successful create')
            return True
class Pool_Values_Managment:
    def __init__(self):
        self.data = PoolOptimalValues.objects
    def take_data(self, pool_id ):
        if self.data.filter(pool_id=pool_id).exists():
            to_return = self.data.filter(pool_id=pool_id)
            return to_return
        else:
            print(f'pool {pool_id} does`t exists ')
            return []
    def write_data(self, pool_id, timestamp, temperature,
                   oxygen_saturation, pH, orp, salinity, water_level,
                   turbidity, ammonia_content, nitrite_content):
        if self.data.filter(pool_id=pool_id).exists():
            now_data = self.data.filter(pool_id=pool_id)
            now_data.timestamp = timestamp
            now_data.temperature = temperature
            now_data.oxygen_saturation = oxygen_saturation
            now_data.pH = pH
            now_data.orp = orp
            now_data.salinity = salinity
            now_data.water_level = water_level
            now_data.turbidity = turbidity
            now_data.ammonia_content = ammonia_content
            now_data.nitrite_content = nitrite_content
            now_data.save()
            print(f'pool data {pool_id} successfully rewrite')
            return True
        else:
            new_data = PoolOptimalValues(
                pool_id=pool_id,
                timestamp=timestamp,
                temperature=temperature,
                oxygen_saturation=oxygen_saturation,
                pH=pH,
                orp=orp,
                salinity=salinity,
                water_level=water_level,
                turbidity=turbidity,
                ammonia_content=ammonia_content,
                nitrite_content=nitrite_content
            )
            new_data.save()
            print(f'pool data {pool_id} successfully create')
            return True
class Pool_Statistic_Managment:
    def __init__(self):
        self.data = PoolStatistic.objects
    def take_data(self, pool_id):
        if self.data.filter(pool_id=pool_id).exists():
            to_return = self.data.filter(pool_id=pool_id)
            return to_return
        else:
            print(f'pool {pool_id} does`t exists ')
            return []
    def write_data(self, pool_id, timestamp, temperature,
                   oxygen_saturation, pH, orp, salinity,
                   water_level, turbidity, ammonia_content,
                   nitrite_content):
        new_data = PoolStatistic(
            pool_id=pool_id,
            timestamp=timestamp,
            temperature=temperature,
            oxygen_saturation=oxygen_saturation,
            pH=pH,
            orp=orp,
            salinity=salinity,
            water_level=water_level,
            turbidity=turbidity,
            ammonia_content=ammonia_content,
            nitrite_content=nitrite_content
        )
        new_data.save()
        print(f'pool {pool_id} successful create')
        return 