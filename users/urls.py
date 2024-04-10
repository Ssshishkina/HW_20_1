from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from users.apps import UsersConfig
from users.views import UserRegisterView, confirm_email, NewPasswordView
from users.views import UserForgotPasswordView


app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', UserRegisterView.as_view(), name='registration'),
    path('reset/', UserForgotPasswordView.as_view(), name='reset'),
    path('confirm_register/<str:token>/', confirm_email, name='confirm_email'),
    path('reset/', UserForgotPasswordView.as_view(), name='reset'),
    path('new_password/', NewPasswordView.as_view(), name='new_password'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

