from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("pets/", views.lista_pets, name="lista_pets"),
    path("pets/novo/", views.novo_pet, name="novo_pet"),
    path("pets/<int:pet_id>/", views.detalhes_pet, name="detalhes_pet"),
]
