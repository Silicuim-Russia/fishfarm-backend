from .services.helpers import Pool_Values_Managment, Pool_Managment, Pool_Statistic_Managment
pools_helper = Pool_Managment()
value_helper = Pool_Values_Managment()
statistics_helper = Pool_Statistic_Managment()

def setting(data:dict):
    status = pools_helper.setting_data(data['pool_id'], data['pool_name'], data['pool_desc'])
    if status:
        return {'is_updated' : status, 'message' : f'pool {data['pool_id']} changed'}
    else:
        return {'is_updated': status, 'message': f'pool {data['pool_id']} does`t exist'}
def update(data: dict):
    if data['sensor'] == 'temperature':
        status = value_helper.write_data(pool_id=data['pool_id'], flag=data['sensor'], min_temperature=data['minValue'],max_temperature=data['maxValue'], min_oxygen_saturation=None,
                   max_oxygen_saturation=None, min_pH=None, max_pH=None, min_orp=None, max_orp=None, min_salinity=None,
                   max_salinity=None, min_water_level=None, max_water_level=None, min_turbidity=None,
                   max_turbidity=None, min_ammonia_content=None, max_ammonia_content=None,
                   min_nitrite_content=None, max_nitrite_content=None)
    elif data['sensor'] == 'oxygen_saturation':
        status = value_helper.write_data(pool_id=data['pool_id'], flag=data['sensor'], min_temperature=None,
                                max_temperature=None, min_oxygen_saturation=data['minValue'],
                                max_oxygen_saturation=data['maxValue'], min_pH=None, max_pH=None, min_orp=None, max_orp=None,
                                min_salinity=None,
                                max_salinity=None, min_water_level=None, max_water_level=None, min_turbidity=None,
                                max_turbidity=None, min_ammonia_content=None, max_ammonia_content=None,
                                min_nitrite_content=None, max_nitrite_content=None)
    elif data['sensor'] == 'pH':
        status = value_helper.write_data(pool_id=data['pool_id'], flag=data['sensor'], min_temperature=None,
                                max_temperature=None, min_oxygen_saturation=None,
                                max_oxygen_saturation=None, min_pH=data['minValue'], max_pH=data['maxValue'], min_orp=None, max_orp=None,
                                min_salinity=None,
                                max_salinity=None, min_water_level=None, max_water_level=None, min_turbidity=None,
                                max_turbidity=None, min_ammonia_content=None, max_ammonia_content=None,
                                min_nitrite_content=None, max_nitrite_content=None)
    elif data['sensor'] == 'orp':
        status = value_helper.write_data(pool_id=data['pool_id'], flag=data['sensor'], min_temperature=None,
                                max_temperature=None, min_oxygen_saturation=None,
                                max_oxygen_saturation=None, min_pH=None, max_pH=None,
                                min_orp=data['minValue'], max_orp=data['maxValue'],
                                min_salinity=None,
                                max_salinity=None, min_water_level=None, max_water_level=None, min_turbidity=None,
                                max_turbidity=None, min_ammonia_content=None, max_ammonia_content=None,
                                min_nitrite_content=None, max_nitrite_content=None)
    elif data['sensor'] == 'salinity':
        status = value_helper.write_data(pool_id=data['pool_id'], flag=data['sensor'], min_temperature=None,
                                         max_temperature=None, min_oxygen_saturation=None,
                                         max_oxygen_saturation=None, min_pH=None, max_pH=None,
                                         min_orp=None, max_orp=None,
                                         min_salinity=data['minValue'],
                                         max_salinity=data['maxValue'], min_water_level=None, max_water_level=None,
                                         min_turbidity=None,
                                         max_turbidity=None, min_ammonia_content=None, max_ammonia_content=None,
                                         min_nitrite_content=None, max_nitrite_content=None)
    elif data['sensor'] == 'water_level':
        status = value_helper.write_data(pool_id=data['pool_id'], flag=data['sensor'], min_temperature=None,
                                max_temperature=None, min_oxygen_saturation=None,
                                max_oxygen_saturation=None, min_pH=None, max_pH=None,
                                min_orp=None, max_orp=None,
                                min_salinity=None,
                                max_salinity=None, min_water_level=data['minValue'], max_water_level=data['maxValue'], min_turbidity=None,
                                max_turbidity=None, min_ammonia_content=None, max_ammonia_content=None,
                                min_nitrite_content=None, max_nitrite_content=None)
    elif data['sensor'] == 'turbidity':
        status = value_helper.write_data(pool_id=data['pool_id'], flag=data['sensor'], min_temperature=None,
                                         max_temperature=None, min_oxygen_saturation=None,
                                         max_oxygen_saturation=None, min_pH=None, max_pH=None,
                                         min_orp=None, max_orp=None,
                                         min_salinity=None,
                                         max_salinity=None, min_water_level=None, max_water_level=None,
                                         min_turbidity=data['minValue'],
                                         max_turbidity=data['maxValue'], min_ammonia_content=None, max_ammonia_content=None,
                                         min_nitrite_content=None, max_nitrite_content=None)
    elif data['sensor'] == 'ammonia_content':
        status = value_helper.write_data(pool_id=data['pool_id'], flag=data['sensor'], min_temperature=None,
                                         max_temperature=None, min_oxygen_saturation=None,
                                         max_oxygen_saturation=None, min_pH=None, max_pH=None,
                                         min_orp=None, max_orp=None,
                                         min_salinity=None,
                                         max_salinity=None, min_water_level=None, max_water_level=None,
                                         min_turbidity=None,
                                         max_turbidity=None, min_ammonia_content=data['minValue'], max_ammonia_content=data['maxValue'],
                                         min_nitrite_content=None, max_nitrite_content=None)
    elif data['sensor'] == 'nitrite_content':
        status = value_helper.write_data(pool_id=data['pool_id'], flag=data['sensor'], min_temperature=None,
                                         max_temperature=None, min_oxygen_saturation=None,
                                         max_oxygen_saturation=None, min_pH=None, max_pH=None,
                                         min_orp=None, max_orp=None,
                                         min_salinity=None,
                                         max_salinity=None, min_water_level=None, max_water_level=None,
                                         min_turbidity=None,
                                         max_turbidity=None, min_ammonia_content=None, max_ammonia_content=None,
                                         min_nitrite_content=data['minValue'], max_nitrite_content=data['maxValue'])
    else:
        print("Check data!!!")
        status = False
        return {'is_updated':status, 'message':'Look at console\nCheck data!!!'}
    return {'is_updated':status, 'message':f'pool_data {data['pool_id']} changed category:{data['sensor']}'}
def get_all_pools():
    to_return = list()
    data = pools_helper.get_data()
    for i in range(len(data[0])):
        to_return.append({
            'pool_id':data[0][i]['pool_id'],
            'pool_name':data[1][i]['pool_name'],
            'pool_desc':data[-1][i]['pool_desc']
        })
    return {'data_type':f'{to_return}'}
def get_status(pool_id):
    id_list = pools_helper.take_data(pool_id=pool_id)
    optimal_values = value_helper.take_data(pool_id=pool_id)
    statistics_data = statistics_helper.take_data(pool_id=pool_id)
    fields = ['temperature', 'oxygen_saturation', 'pH', 'orp',
              'salinity', 'water_level', 'turbidity', 'ammonia_content',
              'nitrite_content']
    to_return = {
        'pool_id' : id_list[0][0]['pool_id'],
        'timestamp':statistics_data[1][0]['timestamp']
    }
    for i, field in enumerate(fields):
        to_return[field] = {
            'sensor_id' : id_list[4+i][0][field + '_sensor_id'],
            'min_value': optimal_values[1 + 2*i][int(pool_id) - 1]['min_' + field],
            'max_value': optimal_values[1 + 2 * i + 1][int(pool_id) - 1]['max_' + field],
            'value' : statistics_data[2 + i][int(pool_id) - 1][field],
            'zone' : check_zone(statistics_data[2 + i][int(pool_id) - 1][field],
                                optimal_values[1 + 2*i][int(pool_id) - 1]['min_' + field],
                                optimal_values[1 + 2 * i + 1][int(pool_id) - 1]['max_' + field])
        }
    return to_return
def check_zone(value, min_value, max_value):
    if value < min_value:
        return 'red'
    elif value > max_value:
        return 'red'
    else:
        return 'green'
