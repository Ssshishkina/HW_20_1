from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from catalog.views import home, product_info, contacts
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('products/<int:pk>/', product_info, name='product_info'),
    path('contacts/', contacts, name='w')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

