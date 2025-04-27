from ..models import *
from asgiref.sync import sync_to_async
from datetime import datetime


async def async_get_all_pools():
    pools = await sync_to_async(list)(Pool.objects.all())
    result = [
        {
            'pool_id': pool.pool_id,
            'pool_name': pool.pool_name,
            'pool_desc': pool.pool_desc
        }
        for pool in pools
    ]

    return {'data_type': result}


async def async_get_status(pool_id):
    optimal = await sync_to_async(list)(
        PoolOptimalValues.objects.filter(pool_id=pool_id).values('sensor', 'min', 'max'))
    optimal_dict = {item['sensor']: {'min': item['min'], 'max': item['max']} for item in optimal}
    stats = await sync_to_async(PoolStatistic.objects.get)(pool_id=pool_id)
    fields = ['temperature', 'oxygen_saturation', 'pH', 'orp',
              'salinity', 'water_level', 'turbidity', 'ammonia_content',
              'nitrite_content']

    result = {
        'pool_id': pool_id,
        'timestamp': stats.timestamp
    }

    for field in fields:
        current_value = getattr(stats, field)
        min_value = optimal_dict.get(field, {}).get('min')
        max_value = optimal_dict.get(field, {}).get('max')
        result[field] = {
            'value': current_value,
            'min_value': min_value,
            'max_value': max_value
        }

    return result


async def async_update_optimal(data):
    try:
        pool_id = data.get('pool_id')
        sensor = data.get('sensor')
        min_value = data.get('minValue')
        max_value = data.get('maxValue')

        if not all([pool_id, sensor, min_value, max_value]):
            return {'is_updated': False, 'message': 'send all required fields (pool_id, sensor, min_value, max_value)'}

        update_data = await sync_to_async(PoolOptimalValues.objects.get)(pool_id=pool_id, sensor=sensor)

        update_data.min = min_value
        update_data.max = max_value
        await sync_to_async(update_data.save)()

        return {'is_updated': True,
                'message': f'{sensor} successfully updated (pool_id: {pool_id},min:{min_value} , max:{max_value})'}
    except Exception as e:
        return {'is_updated': False, 'message': f'{e}'}


async def async_update_sensor_data(data):
    try:
        pool_id = data.get('pool_id')
        if not pool_id:
            return {'is_updated': False, 'message': 'send all required fields (pool_id)'}

        arduino_data = await sync_to_async(StatisticArduino.objects.get)(pool_id=pool_id)

        arduino_data.timestamp = datetime.now()
        arduino_data.temperature = data.get('temperature')
        arduino_data.oxygen_saturation = data.get('oxygen_saturation')
        arduino_data.pH = data.get('pH')
        arduino_data.orp = data.get('orp')
        arduino_data.salinity = data.get('salinity')
        arduino_data.water_level = data.get('water_level')
        arduino_data.turbidity = data.get('turbidity')
        arduino_data.ammonia_content = data.get('ammonia_content')
        arduino_data.nitrite_content = data.get('nitrite_content')
        await sync_to_async(arduino_data.save)()
        return {'is_success': True, 'message': f'updated stats (pool_id: {pool_id})'}
    except Exception as e:
        return {'is_success': False, 'message': f'{e}'}
