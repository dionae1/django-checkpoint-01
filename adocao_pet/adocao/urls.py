from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("pets/", views.lista_pets, name="lista_pets"),
    path("pets/novo/", views.novo_pet, name="novo_pet"),
]
