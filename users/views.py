from django.contrib.auth.views import PasswordResetView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, TemplateView
from users.forms import UserRegisterForm
from users.forms import UserForgotPasswordForm
from users.models import User
import secrets
from django.conf import settings
from django.core.mail import send_mail
import random


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm

    def get_success_url(self):
        return reverse('users:login')

    def form_valid(self, form):
        token = secrets.token_hex(8)
        user = form.save()
        user.token = token
        user.is_active = False
        user.save()
        host = self.request.get_host()
        link = f'http://{host}/users/confirm_register/{token}/'
        message = f'Вы зарегистрировались. Подтвердите почту {link})'
        send_mail('Подтверждение почты', message, settings.EMAIL_HOST_USER,
                  [user.email])
        return super().form_valid(form)


def confirm_email(request, token):
    user = get_object_or_404(User, token=token)
    print(user)
    user.is_active = True
    user.save()

    return redirect('users:login')


class UserForgotPasswordView(PasswordResetView):
    form_class = UserForgotPasswordForm
    template_name = 'users/reset_password.html'
    email_template_name = 'users/new_password.html'

    def get_success_url(self):
        return reverse('users:new_password')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        user = User.objects.get(email=email)
        new_password = ''.join([str(random.randint(0, 9)) for num in range(8)])
        user.set_password(new_password)
        user.save()
        send_mail('Смена пароля', f'Ваш новый пароль {new_password}', settings.EMAIL_HOST_USER,
                  [user.email])
        return super().form_valid(form)


class NewPasswordView(TemplateView):
    template_name = 'users/new_password.html'
