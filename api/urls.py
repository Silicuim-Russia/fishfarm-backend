from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import *
from .tasks import *

from background_task.models import Task, CompletedTask

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('all-pools/', AllPools.as_view(), name='all-pools'),
    path('status/', StatusPool.as_view(), name='status'),
    path('update/', OptimalValues.as_view(), name='update'),
    # path('setting/', AllPools.as_view(), name='setting'),
    path('sensors-data/', SensorsData.as_view(), name='sensors-data'),
    # path('thing-state/', ThingControl.as_view(), name='thing-state')
    path('watch/<str:stream_name>', ChannelOpenView.as_view(), name='channel_open'),
    path('read/<str:channel>/<str:filename>', ChannelReadView.as_view(), name='channel_read'),
]


Task.objects.all().delete()
CompletedTask.objects.all().delete()

match_arduino_api(repeat=30)
check_pools_health(repeat=60)
