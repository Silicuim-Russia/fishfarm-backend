from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from .serializers import DeviceSerializer
from rest_framework.permissions import IsAuthenticated

# class DeviceViewSet(viewsets.ModelViewSet):
#     queryset = Device.objects.all()
#     serializer_class = DeviceSerializer
#
#     # Кастомное действие для включения/выключения устройства
#     @action(detail=True, methods=['post'])
#     def toggle(self, request, pk=None):
#         device = self.get_object()
#         device.is_active = not device.is_active
#         device.save()
#         return Response({
#             'status': 'success',
#             'is_active': device.is_active,
#             'last_activity': device.last_activity,
#             'message': f"{device.name} {'активирован' if device.is_active else 'деактивирован'}"
#         })
#
#
# @api_view(['GET'])
# def system_status(request):
#     latest_status = SystemStatus.objects.order_by('-timestamp').first()
#     if not latest_status:
#         return Response({'error': 'Нет информации'}, status=404)
#
#     serializer = SystemStatusSerializer(latest_status)
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def get_status(request):
#     pools = Pool.objects.prefetch_related('parameters').all()
#     serializer = PoolSerializer(pools, many=True)
#     return Response({
#         'pools': serializer.data
#     })
#
#
# @api_view(['POST'])
# def update_parameters(request):
#     sensor_id = request.data.get('sensor_id')
#     new_value = request.data.get('value')
#
#     try:
#         parameter = PoolParameter.objects.get(sensor_id=sensor_id)
#         parameter.current_value = round(float(new_value), 2)  # Округление до 2 знаков
#         parameter.save()
#         return Response({'status': 'updated'})
#     except PoolParameter.DoesNotExist:
#         return Response({'error': 'Sensor not found'}, status=status.HTTP_404_NOT_FOUND)
