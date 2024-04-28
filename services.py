from django.core.cache import cache
from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_products_from_cache():
    '''Получаем список продуктов из кеша.'''
    if not CACHE_ENABLED:
        return Product.objects.all()
        key = 'products_list'
        products = cache.get(key)
        if products is None:
            products = Product.objects.all()
            cache.set(key, products)
        return products
