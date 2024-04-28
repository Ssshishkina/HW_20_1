from django.conf import settings
from django.core.cache import cache
from catalog.models import Product


def get_cached_products(product_id):
    if settings.CACHE_ENABLED:
        key = f'product_list_{product_id}'
        product_list = cache.get(key)
        if product_list is None:
            product_list = Product.objects.filter(product_id=product_id)
            cache.set(key, product_list)
    else:
        product_list = Product.objects.filter(product_id=product_id)
    return product_list
