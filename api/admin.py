from django.contrib import admin
from .models import *

admin.site.register(Pool)
admin.site.register(PoolOptimalValues)
admin.site.register(PoolStatistic)
admin.site.register(StatisticArduino)
admin.site.register(PoolStream)