from django.urls import path
from django.views.decorators.cache import cache_page, never_cache
from catalog.views import (HomeView, ProductDetailView, contacts, BlogCreateView, BlogUpdateView, BlogDeleteView,
                           BlogListView, BlogDetailView, toggle_published, ProductCreateView, ProductUpdateView,
                           ProductDeleteView)
from django.conf.urls.static import static
from django.conf import settings
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('products/create/', never_cache(ProductCreateView.as_view()), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('contacts/', contacts, name='w'),
    path('blog/', BlogListView.as_view(), name='blg'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create/', BlogCreateView.as_view(), name='create'),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='update'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='delete'),
    path('blog/<int:pk>/is_published/', toggle_published, name='toggle_published'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
