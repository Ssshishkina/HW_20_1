from django.urls import path
from catalog.views import (HomeView, ProductDetailView, contacts, BlogCreateView, BlogUpdateView, BlogDeleteView,
                           BlogListView, BlogDetailView, toggle_published)
from django.conf.urls.static import static
from django.conf import settings
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', contacts, name='w'),
    path('blog/', BlogListView.as_view(), name='blg'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create/', BlogCreateView.as_view(), name='create'),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='update'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='delete'),
    path('blog/<int:pk>/is_published/', toggle_published, name='toggle_published'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

