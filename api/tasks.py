from background_task import background
from django.utils.timezone import now
from datetime import datetime, timedelta
from .models import *


@background()
def match_arduino_api():
    print('TASK# matched arduino and api tables')
    arduino_statistics = StatisticArduino.objects.all()

    for stat in arduino_statistics:
        pool_id = stat.pool_id
        api_data = PoolStatistic.objects.get(pool_id=pool_id)

        api_data.timestamp = stat.timestamp
        api_data.temperature = stat.temperature
        api_data.oxygen_saturation = stat.oxygen_saturation
        api_data.pH = stat.pH
        api_data.orp = stat.orp
        api_data.salinity = stat.salinity
        api_data.water_level = stat.water_level
        api_data.turbidity = stat.turbidity
        api_data.ammonia_content = stat.ammonia_content
        api_data.nitrite_content = stat.nitrite_content

        api_data.save()


@background()
def check_pools_health():
    stats = PoolStatistic.objects.all()

    for stat in stats:
        pool_id = stat.pool_id

        if (now() - stat.timestamp) > timedelta(minutes=5):
            triggered_func(f'Данные бассейна с ID:{pool_id} не обновлялись больше 5 минут')

        fields_to_check = [
            'temperature',
            'oxygen_saturation',
            'pH',
            'orp',
            'salinity',
            'water_level',
            'turbidity',
            'ammonia_content',
            'nitrite_content'
        ]

        for field in fields_to_check:
            if not getattr(stat, field):
                continue

            current_value = getattr(stat, field)

            optimal_values = PoolOptimalValues.objects.get(pool_id=pool_id, sensor=field)
            min_value = optimal_values.min
            max_value = optimal_values.max

            if not (min_value <= current_value <= max_value):
                triggered_func(
                    f"Бассейн {pool_id}: Значение {field} ({current_value}) вне допустимого диапазона [{min_value}, {max_value}]")


def triggered_func(message):
    print(message)
