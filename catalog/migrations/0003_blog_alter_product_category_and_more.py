# Generated by Django 5.0.2 on 2024-03-09 19:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_remove_product_manufactured_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Укажите заголовок', max_length=100, verbose_name='Заголовок')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True, verbose_name='Человекопонятный URL')),
                ('content', models.TextField(blank=True, help_text='Добавьте описание', null=True, verbose_name='Содержимое')),
                ('image', models.ImageField(blank=True, help_text='Приложите фото', null=True, upload_to='blog_images', verbose_name='Изображение (превью)')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('view_counter', models.PositiveIntegerField(default=0, help_text='Укажите кол-во просмотров', verbose_name='Счетчик просмотров')),
            ],
            options={
                'verbose_name': 'Публикация',
                'verbose_name_plural': 'Публикации',
                'ordering': ['created_at', 'is_published', 'view_counter'],
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, help_text='Категория товара', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='catalog.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, help_text='Опишите товар', null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, help_text='Фото товара', null=True, upload_to='prod_images', verbose_name='Изображение (превью)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(help_text='Укажите наименование товара', max_length=50, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(help_text='Стоимость товара', verbose_name='Цена за покупку'),
        ),
    ]
