from ..models import StatisticArduino


class StatisticArduinoManagement:
    def save_sensors_data(self, data):
        new_data = StatisticArduino(
            pool_id=data.get('pool_id'),
            temperature=data.get('temperature'),
            oxygen_saturation=data.get('oxygen_saturation'),
            pH=data.get('pH'),
            orp=data.get('orp'),
            salinity=data.get('salinity'),
            water_level=data.get('water_level'),
            turbidity=data.get('turbidity'),
            ammonia_content=data.get('ammonia_content'),
            nitrite_content=data.get('nitrite_content')
        )
        new_data.save()
        return True