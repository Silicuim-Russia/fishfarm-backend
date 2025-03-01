from .services.helpers import Pool_Values_Managment, Pool_Managment
value_helper = Pool_Values_Managment()
pools_helper = Pool_Managment()
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
        return {'is_updated':False, 'message':'Look at console\nCheck data!!!'}
    return {'is_updated':True, 'message':f'pool_data {data['pool_id']} changed category:{data['sensor']}'}
def get_all_pools():
    to_return = list()
    data = pools_helper.all_data()
    for i in range(len(data[0])):
        to_return.append({
            'pool_id':data[0][i]['pool_id'],
            'pool_name':data[1][i]['pool_name'],
            'pool_desc':data[-1][i]['pool_desc']
        })
    return {'data_type':f'{to_return}'}