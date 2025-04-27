from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .services.async_getters import async_get_all_pools, async_get_status, async_update_optimal, async_update_sensor_data
from drfasyncview import AsyncRequest, AsyncAPIView


@permission_classes([])
class AllPools(AsyncAPIView):
    async def get(self, request: AsyncRequest):
        all_pools = await async_get_all_pools()
        return Response(all_pools)


@permission_classes([])
class StatusPool(AsyncAPIView):
    async def get(self, request: AsyncRequest):
        pool_status = await async_get_status(request.query_params.get('pool_id'))
        return Response(pool_status)


@permission_classes([])
class OptimalValues(AsyncAPIView):
    async def post(self, request: AsyncRequest):
        update_optimal = await async_update_optimal(request.data)
        return Response(update_optimal)


@permission_classes([])
class SensorsData(AsyncAPIView):
    async def post(self, request: AsyncRequest):
        sensors_data = await async_update_sensor_data(request.data)
        return Response(sensors_data)


# @permission_classes([])
# class ThingControl(APIView):
#
#     def post(self, request, *args, **kwargs):
#         try:
#             return Response({'is_success': True, 'state': ControlThingsArduinoManagement().thing_state(request.data)},
#                             status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'is_success': False, 'state': 'ERROR'}, status=status.HTTP_400_BAD_REQUEST)
