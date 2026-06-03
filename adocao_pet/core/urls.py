from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import EmailAuthenticationForm

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html",
            authentication_form=EmailAuthenticationForm,
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(
            next_page="login",
        ),
        name="logout",
    ),
    path(
        "register/",
        views.register,
        name="register",
    ),
    path(
        "update/",
        views.atualizar_usuario,
        name="atualizar_usuario",
    ),
]
