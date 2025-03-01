from ..models import Pool, PoolOptimalValues, PoolStatistic


def get_pools():
    return Pool.objects.all()
class Pool_Values_Managment:
    def __init__(self):
        self.data = PoolOptimalValues.objects
    def take_data(self, pool_id ):
        if self.data.filter(pool_id=pool_id).exists():
            to_return = self.data.filter(pool_id=pool_id)
            return to_return
        else:
            print(f'pool {pool_id} don`t exists')
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
            print(f'pool data {pool_id} successfully create')
            return True