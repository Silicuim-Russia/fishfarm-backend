from rest_framework import serializers
from .models import *


class PoolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pool
        fields = '__all__'

class PoolStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoolStatistic
        fields = '__all__'
        extra_kwargs = {
            'pool_id': {'read_only': True},
            'timestamp': {'read_only': True}
        }

class UpdateSerializer(serializers.Serializer):
    sensor_id = serializers.IntegerField(required=True)
    value = serializers.FloatField(required=True)