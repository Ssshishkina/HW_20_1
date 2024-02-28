from django.db import models

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
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='prod_images', verbose_name='Изображение (превью)', **NULLABLE)
    category = models.ForeignKey('Category', related_name='products', verbose_name='Категория',
                                 on_delete=models.SET_NULL, **NULLABLE)
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateField(verbose_name='Дата создания (записи в БД)', auto_now_add=True, **NULLABLE)
    updated_at = models.DateField(verbose_name='Дата последнего изменения (записи в БД)', auto_now=True, **NULLABLE)

    #manufactured_at = models.DateField(verbose_name='Дата производства продукта', auto_now=True, **NULLABLE)
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", ]

    def __str__(self):
        return self.name
