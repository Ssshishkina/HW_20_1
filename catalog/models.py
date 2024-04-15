from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name', ]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование', help_text='Укажите наименование товара')
    description = models.TextField(verbose_name='Описание', **NULLABLE, help_text='Опишите товар')
    image = models.ImageField(upload_to='prod_images', verbose_name='Изображение (превью)',
                              **NULLABLE, help_text='Фото товара')
    category = models.ForeignKey('Category', related_name='products', verbose_name='Категория',
                                 on_delete=models.SET_NULL, **NULLABLE, help_text='Категория товара')
    price = models.IntegerField(verbose_name='Цена за покупку', help_text='Стоимость товара')
    created_at = models.DateField(verbose_name='Дата создания (записи в БД)', auto_now_add=True, **NULLABLE)
    updated_at = models.DateField(verbose_name='Дата последнего изменения (записи в БД)', auto_now=True, **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Пользователь', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='Опубликован')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name",]
        permissions = [
            ('cancel_publication', 'Can cancel publication'),
            ('change_description', 'Can change description'),
            ('change_category', 'Can change category'),
        ]

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок', help_text='Укажите заголовок')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Человекопонятный URL', **NULLABLE)
    content = models.TextField(verbose_name='Содержимое', **NULLABLE, help_text='Добавьте описание')
    image = models.ImageField(upload_to='blog_images', verbose_name='Изображение (превью)', **NULLABLE,
                              help_text='Приложите фото')
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True, **NULLABLE)
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)
    view_counter = models.PositiveIntegerField(verbose_name='Счетчик просмотров',
                                               help_text='Укажите кол-во просмотров', default=0)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['created_at', 'is_published', 'view_counter',]

    def __str__(self):
        return f'{self.title}'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    number = models.FloatField(verbose_name='Номер версии')
    name = models.CharField(max_length=100, verbose_name='Название версии', **NULLABLE)
    working_ver = models.BooleanField(verbose_name='Признак версии', **NULLABLE)

    def __str__(self):
        return f'Версия {self.product} == {self.number}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
