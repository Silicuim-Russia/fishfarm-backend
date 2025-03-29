from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


from .services.arduino_service import *
from .serializers import *
from .processor import update, get_all_pools, get_status, setting


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
            return Response({'is_success': False, 'state': 'ERROR'}, status=status.HTTP_400_BAD_REQUEST)
