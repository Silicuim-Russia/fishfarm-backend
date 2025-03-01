from ..models import Pool, PoolOptimalValues, PoolStatistic


def get_pools():
    return Pool.objects.all()