from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from users.models import User
from django import forms
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']


class UserForgotPasswordForm(PasswordResetForm):
    class Meta:
        model = User
        fields = ['email',]

    def clean_email(self):
        '''Проверка существующего пользователя.'''
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
        except Exception:
            raise forms.ValidationsError('Пользователь с такой почтой не найден.')
        return email

    def send_mail(
            self,
            subject_template_name,
            email_template_name,
            context,
            from_email,
            to_email,
            html_email_template_name=None,
    ):
        pass
