from django.contrib import admin
from catalog.models import Category, Product, Blog


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_filter = ("name",)
    search_fields = ("name", "description",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category",)
    list_filter = ("category",)
    search_fields = ("name", "description",)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    '''Класс для регистрации публикации в админке.'''
    list_display = ("id", "title", "is_published", "slug",)
    list_filter = ("title",)
    search_fields = ("title", "is_published",)
