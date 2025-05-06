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
        api_stat = PoolStatistic.objects.get(pool_id=pool_id)
        api_pool = Pool.objects.get(pool_id=pool_id)

        api_stat.timestamp = stat.timestamp
        api_stat.temperature = stat.temperature
        api_stat.oxygen_saturation = stat.oxygen_saturation
        api_stat.pH = stat.pH
        api_stat.orp = stat.orp
        api_stat.salinity = stat.salinity
        api_stat.water_level = stat.water_level
        api_stat.turbidity = stat.turbidity
        api_stat.ammonia_content = stat.ammonia_content
        api_stat.nitrite_content = stat.nitrite_content

        api_pool.timestamp = stat.timestamp

        api_stat.save()
        api_pool.save()


@background()
def check_pools_health():
    stats = PoolStatistic.objects.all()

    for stat in stats:
        pool_id = stat.pool_id
        api_pool = Pool.objects.get(pool_id=pool_id)
        bad_sensors_counter = 0

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

        if (now() - stat.timestamp) > timedelta(minutes=5):
            triggered_func(f'Данные бассейна с ID:{pool_id} не обновлялись больше 5 минут')

        for field in fields_to_check:
            if not getattr(stat, field):
                continue

            current_value = getattr(stat, field)

            optimal_values = PoolOptimalValues.objects.get(pool_id=pool_id, sensor=field)
            min_value = optimal_values.min
            max_value = optimal_values.max

            if not (min_value < current_value < max_value):
                triggered_func(
                    f"Бассейн {pool_id}: Значение {field} ({current_value}) вне допустимого диапазона [{min_value}, {max_value}]")
                bad_sensors_counter += 1

        health_percentage = 100 - int(bad_sensors_counter * 100 / len(fields_to_check))
        if bad_sensors_counter == 0:
            health_zone = 'good'
        elif bad_sensors_counter < 3:
            health_zone = 'warning'
        else:
            health_zone = 'danger'

        api_pool.state_percents = health_percentage
        api_pool.state_zone = health_zone
        api_pool.save()


def triggered_func(message):
    print(message)
