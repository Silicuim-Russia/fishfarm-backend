from rest_framework import serializers
from .services.helpers import Pool_Managment, Pool_Values_Managment, Pool_Statistic_Managment


class ParameterSerializer(serializers.Serializer):
    sensor = serializers.IntegerField()
    optimalStartValue = serializers.FloatField()
    optimalEndValue = serializers.FloatField()
    value = serializers.FloatField()


class PoolStatusSerializer(serializers.Serializer):
    temperature = ParameterSerializer()
    oxygen_saturation = ParameterSerializer()
    pH = ParameterSerializer()
    orp = ParameterSerializer()
    salinity = ParameterSerializer()
    water_level = ParameterSerializer()
    turbidity = ParameterSerializer()
    ammonia_content = ParameterSerializer()
    nitrite_content = ParameterSerializer()

    def get_parameter_data(self, pool_id, param_name):
        pool_mgr = Pool_Managment()
        values_mgr = Pool_Values_Managment()
        stats_mgr = Pool_Statistic_Managment()

        pool_data = pool_mgr.take_data(pool_id).first()
        if not pool_data:
            return None

        optimal_values = values_mgr.take_data(pool_id).first()

        last_stat = stats_mgr.take_data(pool_id).order_by('-timestamp').first()

        param_map = {
            'temperature': {
                'sensor_field': 'temperature_sensor_id',
                'min_field': 'min_temperature',
                'max_field': 'max_temperature',
                'value_field': 'temperature'
            },
            'oxygen_saturation': {
                'sensor_field': 'oxygen_saturation_sensor_id',
                'min_field': 'min_oxygen_saturation',
                'max_field': 'max_oxygen_saturation',
                'value_field': 'oxygen_saturation'
            },
            "pH": {
                'sensor_field': 'ph_sensor_id',
                'min_field': 'min_ph',
                'max_field': 'max_ph',
                'value_field': 'ph'
            },
            "orp": {
                'sensor_field': 'orp_sensor_id',
                'min_field': 'min_orp',
                'max_field': 'max_orp',
                'value_field': 'orp'
            },
            "salinity": {
                'sensor_field': 'salinity_sensor_id',
                'min_field': 'min_salinity',
                'max_field': 'max_salinity',
                'value_field': 'salinity'
            },
            "water_level": {
                'sensor_field': 'water_level_sensor_id',
                'min_field': 'min_water_level',
                'max_field': 'max_water_level',
                'value_field': 'water_level'
            },
            "turbidity": {
                'sensor_field': 'turbidity_sensor_id',
                'min_field': 'min_turbidity',
                'max_field': 'max_turbidity',
                'value_field': 'turbidity'
            },
            "ammonia_content": {
                'sensor_field': 'ammonia_content_sensor_id',
                'min_field': 'min_ammonia_content',
                'max_field': 'max_ammonia_content',
                'value_field': 'ammonia_content'
            },
            "nitrite_content": {
                'sensor_field': 'nitrite_content_sensor_id',
                'min_field': 'min_nitrite_content',
                'max_field': 'max_nitrite_content',
                'value_field': 'nitrite_content'
            }
        }

        return {
            "sensor": getattr(pool_data, param_map[param_name]['sensor_field']),
            "optimalStartValue": getattr(optimal_values, param_map[param_name]['min_field']),
            "optimalEndValue": getattr(optimal_values, param_map[param_name]['max_field']),
            "value": getattr(last_stat, param_map[param_name]['value_field'])
        }

    def to_representation(self, instance):
        pool_id = instance.pool_id.pool_id
        return {
            "temperature": self.get_parameter_data(pool_id, 'temperature'),
            "oxygen_saturation": self.get_parameter_data(pool_id, 'oxygen_saturation'),
            "pH": self.get_parameter_data(pool_id, 'pH'),
            "orp": self.get_parameter_data(pool_id, 'orp'),
            "salinity": self.get_parameter_data(pool_id, 'salinity'),
            "water_level": self.get_parameter_data(pool_id, 'water_level'),
            "turbidity": self.get_parameter_data(pool_id, 'turbidity'),
            "ammonia_content": self.get_parameter_data(pool_id, 'ammonia_content'),
            "nitrite_content": self.get_parameter_data(pool_id, 'nitrite_content')
        }