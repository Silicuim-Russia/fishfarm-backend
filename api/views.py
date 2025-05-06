from django.http import Http404, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from rest_framework.decorators import permission_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .services.async_getters import *
from drfasyncview import AsyncRequest, AsyncAPIView

from .models import *
from .services.stream_service import HlsStreamService
import time
import os
from . import settings as app_settings

from asgiref.sync import sync_to_async


class AllPools(AsyncAPIView):
    permission_classes = [IsAuthenticated]

    async def initial(self, request, *args, **kwargs):
        await sync_to_async(request._authenticate)()
        await self.check_permissions(request)
        await self.check_throttles(request)

    async def get(self, request):
        all_pools = await async_get_all_pools()
        return Response(all_pools)


class StatusPool(AsyncAPIView):
    permission_classes = [IsAuthenticated]

    async def initial(self, request, *args, **kwargs):
        await sync_to_async(request._authenticate)()
        await self.check_permissions(request)
        await self.check_throttles(request)

    async def get(self, request: AsyncRequest):
        pool_status = await async_get_status(request.query_params.get('pool_id'))
        return Response(pool_status)


class OptimalValues(AsyncAPIView):
    permission_classes = [IsAuthenticated]

    async def initial(self, request, *args, **kwargs):
        await sync_to_async(request._authenticate)()
        await self.check_permissions(request)
        await self.check_throttles(request)

    async def post(self, request: AsyncRequest):
        update_optimal = await async_update_optimal(request.data)
        return Response(update_optimal)


class CreatePool(AsyncAPIView):
    permission_classes = [IsAuthenticated]

    async def initial(self, request, *args, **kwargs):
        await sync_to_async(request._authenticate)()
        await self.check_permissions(request)
        await self.check_throttles(request)

    async def post(self, request: AsyncRequest):
        create_pool = await async_create_pool(request.data)
        return Response(create_pool)


class DeletePool(AsyncAPIView):
    permission_classes = [IsAuthenticated]

    async def initial(self, request, *args, **kwargs):
        await sync_to_async(request._authenticate)()
        await self.check_permissions(request)
        await self.check_throttles(request)

    async def get(self, request: AsyncRequest):
        delete_pool = await async_delete_pool(request.query_params.get('pool_id'))
        return Response(delete_pool)


class SensorsData(AsyncAPIView):
    permission_classes = [IsAuthenticated]

    async def initial(self, request, *args, **kwargs):
        await sync_to_async(request._authenticate)()
        await self.check_permissions(request)
        await self.check_throttles(request)

    async def post(self, request: AsyncRequest):
        sensors_data = await async_update_sensor_data(request.data)
        return Response(sensors_data)


@permission_classes([AllowAny])
class ChannelOpenView(View):
    def get(self, request, stream_name):
        channel = PoolStream.objects.get(stream_name=stream_name)

        if channel.transcode_pid < 1:
            try:
                hls_service = HlsStreamService()
                process_id = hls_service.deploy_transcode_daemon(channel)

                channel.transcode_pid = process_id
                channel.save()

                for _ in range(10):
                    if hls_service.channel_ready(stream_name):
                        break
                    time.sleep(1)
                else:
                    raise Http404("Channel is not ready")
            except Exception as e:
                raise Http404("Failed to start channel")

        return redirect(reverse('channel_read', args=[stream_name, 'index.m3u8']))


@permission_classes([AllowAny])
class ChannelReadView(View):
    def get(self, request, channel, filename):
        try:
            file_path = os.path.join(app_settings.HLS_STREAM_ROOT, channel, filename)
            with open(file_path, 'rb') as file_stream:
                extension = filename.split('.')[1]
                if extension == 'm3u8':
                    content_type = 'application/vnd.apple.mpegurl'
                elif extension == 'ts':
                    content_type = 'video/mp2t'
                else:
                    content_type = 'application/octet-stream'

                response = HttpResponse(file_stream, content_type=content_type)
                return response
        except FileNotFoundError:
            raise Http404("File does not exist")
