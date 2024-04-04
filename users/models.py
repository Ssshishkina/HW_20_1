from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    avatar = models.ImageField(upload_to='users/avatar', verbose_name="Аватар", **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='email')
    token = models.CharField(max_length=50, verbose_name='Токен', **NULLABLE)


USERNAME_FIELD = 'email'
REQUIRED_FIELDS = []


class Meta:
    verbose_name = 'Пользователь'
    verbose_name_plural = 'Пользователи'


def __str__(self):
    return self.email


