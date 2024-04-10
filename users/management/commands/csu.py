from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='user@sky.pro',
            first_name='User_11',
            last_name='Ivanov',
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        user.set_password('Qwerty123')
        user.save()

#новый пользователь
#email='user_new@sky.pro',
#user.set_password('@9gkHe56x')