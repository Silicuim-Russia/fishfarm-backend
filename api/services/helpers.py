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
            new_pool_values = PoolOptimalValues(pool_id=pool_id)
            new_pool_values.save()
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
    def write_data(self, pool_id, flag, min_temperature, max_temperature, min_oxygen_saturation,
                   max_oxygen_saturation, min_pH, max_pH, min_orp, max_orp, min_salinity,
                   max_salinity, min_water_level, max_water_level, min_turbidity,
                   max_turbidity, min_ammonia_content, max_ammonia_content,
                   min_nitrite_content, max_nitrite_content):
        if self.data.filter(pool_id=pool_id).exists() == False:
            print(f'pool {pool_id} does`t exist')
            return False
        else:
            now_data = self.data.filter(pool_id=pool_id)
            if flag == 'temperature':
                now_data.min_temperature = min_temperature
                now_data.max_temperature = max_temperature
            elif flag == 'oxygen_saturation':
                now_data.min_oxygen_saturation = min_oxygen_saturation
                now_data.max_oxygen_saturation = max_oxygen_saturation
            elif flag == 'pH':
                now_data.min_pH = min_pH
                now_data.max_pH = max_pH
            elif flag == 'orp':
                now_data.min_orp = min_orp
                now_data.max_orp = max_orp
            elif flag == 'salinity':
                now_data.min_salinity = min_salinity
                now_data.max_salinity = max_salinity
            elif flag == 'water_level':
                now_data.min_water_level = min_water_level
                now_data.max_water_level = max_water_level
            elif flag == 'turbidity':
                now_data.min_turbidity = min_turbidity
                now_data.max_turbidity = max_turbidity
            elif flag == 'ammonia_content':
                now_data.min_ammonia_content = min_ammonia_content
                now_data.max_ammonia_content = max_ammonia_content
            elif flag == 'nitrite_content':
                now_data.min_nitrite_content = min_nitrite_content
                now_data.max_nitrite_content = max_nitrite_content
            else:
                print('Wrong flag')
                return False
            now_data.save()
            print(f'pool optimal values {pool_id} updated successfully')
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
        return True