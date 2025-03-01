from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .services.helpers import *
from .serializers import *


class AllPools(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        pools = Pool.objects.all()
        serializer = PoolsSerializer(pools, many=True)

        return Response({'all_pools': serializer.data})
