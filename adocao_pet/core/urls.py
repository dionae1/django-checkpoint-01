from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import FormularioAutenticacao

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html",
            authentication_form=FormularioAutenticacao,
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
        views.cadastrar_usuario,
        name="cadastrar_usuario",
    ),
    path(
        "update/",
        views.atualizar_usuario,
        name="atualizar_usuario",
    ),
]
