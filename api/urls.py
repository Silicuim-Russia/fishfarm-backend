from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import *

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('all-pools/', AllPools.as_view(), name='all-pools'),
    path('status/', get_status, name='status'),
    path('update/', update_parameters, name='update'),
]
