from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


from .services.arduino_service import *
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


@permission_classes([])
class SensorsData(APIView):

    def post(self, request, *args, **kwargs):
        try:
            StatisticArduinoManagement().save_sensors_data(request.data)
            return Response({'is_success': True}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'is_success': False}, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([])
class ThingControl(APIView):

    def post(self, request, *args, **kwargs):
        try:
            return Response({'is_success': True, 'state': ControlThingsArduinoManagement().thing_state(request.data)},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'is_success': False, 'state': 'ERROR'})
