from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .services.helpers import Pool_Statistic_Managment
from .serializers import *
<<<<<<< HEAD
from .pidor import update, get_all_pools
=======
>>>>>>> 2b7ef3cc31d3851570c211ab544276e0195902a1


<<<<<<< HEAD
    def get(self, request, *args, **kwargs):
        # pools = Pool.objects.all()
        # serializer = PoolsSerializer(pools, many=True)
        # return Response({'all_pools': serializer.data})

        return Response(get_all_pools())
    def post(self, request, *args, **kwargs):
        return Response(update(request.data))
=======
# class AllPools(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, *args, **kwargs):
#         pools = Pool.objects.all()
#         serializer = PoolsSerializer(pools, many=True)
#
#         return Response({'all-pools': serializer.data})
>>>>>>> 2b7ef3cc31d3851570c211ab544276e0195902a1

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_status(request):
    pool_id = request.query_params.get('pool_id')
    print(pool_id)
    stats_mgr = Pool_Statistic_Managment()
    print(stats_mgr)
    all_stats = stats_mgr.take_data(pool_id)
    print(all_stats)

    serializer = PoolStatusSerializer(all_stats, many=True)
    return Response({'status': serializer.data})


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def update_parameters(request):
#     serializer = UpdateSerializer(data=request.data)
#     if not serializer.is_valid():
#         return Response(serializer.errors, status=400)
#
#     sensor_id = serializer.validated_data['sensor_id']
#     value = serializer.validated_data['value']
#
#     try:
#         pool = Pool.objects.get(
#             models.Q(temperature_sensor_id=sensor_id) |
#             models.Q(oxygen_saturation_sensor_id=sensor_id) |
#             models.Q(pH_sensor_id=sensor_id) |
#             models.Q(orp_sensor_id=sensor_id) |
#             models.Q(salinity_sensor_id=sensor_id) |
#             models.Q(water_level_sensor_id=sensor_id) |
#             models.Q(turbidity_sensor_id=sensor_id) |
#             models.Q(ammonia_content_sensor_id=sensor_id) |
#             models.Q(nitrite_content_sensor_id=sensor_id)
#         )
#     except Pool.DoesNotExist:
#         return Response({'error': 'Sensor not found'}, status=404)
#
#     param_mapping = {
#         pool.temperature_sensor_id: 'temperature',
#         pool.oxygen_saturation_sensor_id: 'oxygen_saturation',
#         pool.pH_sensor_id: 'pH',
#         pool.orp_sensor_id: 'orp',
#         pool.salinity_sensor_id: 'salinity',
#         pool.water_level_sensor_id: 'water_level',
#         pool.turbidity_sensor_id: 'turbidity',
#         pool.ammonia_content_sensor_id: 'ammonia_content',
#         pool.nitrite_content_sensor_id: 'nitrite_content'
#     }
#
#     field_name = param_mapping.get(sensor_id)
#     if not field_name:
#         return Response({'error': 'Invalid sensor type'}, status=400)
#
#     stat, created = PoolStatistic.objects.update_or_create(
#         pool_id=pool,
#         defaults={
#             field_name: value,
#             **{f: None for f in ['temperature', 'oxygen_saturation', 'pH', 'orp',
#                                  'salinity', 'water_level', 'turbidity',
#                                  'ammonia_content', 'nitrite_content']
#                if f != field_name}
#         }
#     )
#
#     return Response({'status': 'updated', 'pool_id': pool.pool_id})