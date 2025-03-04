from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from api import views
from .views import *
from api.consumers import StreamConsumer
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('all-pools/', AllPools.as_view(), name='all-pools'),
    path('status/', StatusPool.as_view(), name='status'),
    path('update/', OptimalValues.as_view(), name='update'),
    path('setting/', AllPools.as_view(), name='setting'),
    path('stream/', views.stream_info),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

websocket_urlpatterns = [
    path('ws/stream/', StreamConsumer.as_asgi()),
]
