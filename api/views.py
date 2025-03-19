from django.db.models import *
from rest_framework.views import APIView
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .processor import update, get_all_pools, get_status, setting

from django.http import StreamingHttpResponse
import subprocess

def stream_video(request):
    command = [
        'ffmpeg',
        '-i', 'rtsp://pool250:_250_pool@45.152.168.61:52037',
        '-c:v', 'libx264',
        '-preset', 'ultrafast',
        '-tune', 'zerolatency',
        '-f', 'hls',
        '-hls_time', '2',
        '-hls_list_size', '5',
        '-hls_flags', 'delete_segments',
        'pipe:1'
    ]

    try:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        def stream():
            while True:
                chunk = process.stdout.read(1024)
                if not chunk:
                    break
                yield chunk

        return StreamingHttpResponse(stream(), content_type='application/x-mpegURL')

    except Exception as e:
        print(f"Error streaming video: {e}")
        return StreamingHttpResponse(status=500, content_type='text/plain', content="Error streaming video")

class AllPools(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # pools = Pool.objects.all()
        # serializer = PoolsSerializer(pools, many=True)
        # return Response({'all_pools': serializer.data})

        return Response(get_all_pools())
    def post(self, request, *args, **kwargs):
        return Response(setting(request.data))
class OptimalValues(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        return Response(update(request.data))
class StatusPool(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        return Response(get_status(request.query_params.get('pool_id')))
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_status(request):
#     # pool_id = request.query_params.get('pool_id')
#     # print(pool_id)
#     # stats_mgr = Pool_Statistic_Managment()
#     # print(stats_mgr)
#     # all_stats = stats_mgr.take_data(pool_id)
#     # print(all_stats)
#     #
#     # serializer = PoolStatusSerializer(all_stats, many=True)
#     # return Response({'status': serializer.data})
#     return Response(request.data)

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