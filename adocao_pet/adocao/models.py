from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    celular = models.CharField(max_length=20, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
        "first_name",
        "last_name",
        "celular",
        "cidade",
        "estado",
    ]

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


class Pet(models.Model):
    ESCOLHAS_STATUS = [
        ("disponível", "Disponível"),
        ("adotado", "Adotado"),
    ]

    ESCOLHAS_PORTE = [
        ("pequeno", "Pequeno"),
        ("médio", "Médio"),
        ("grande", "Grande"),
    ]

    dono = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="pets"
    )

    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    porte = models.CharField(max_length=20, choices=ESCOLHAS_PORTE)
    descricao = models.TextField(blank=True)
    vacinado = models.BooleanField(default=False)
    castrado = models.BooleanField(default=False)

    status = models.CharField(
        max_length=20, choices=ESCOLHAS_STATUS, default="disponível"
    )

    def __str__(self) -> str:
        return self.nome


class FotoPet(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="fotos")
    imagem = models.ImageField(upload_to="pets/")
    data_upload = models.DateTimeField(auto_now_add=True)
    descricao = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["-data_upload"]
        verbose_name = "Foto do Pet"
        verbose_name_plural = "Fotos dos Pets"

    def __str__(self) -> str:
        return f"Foto de {self.pet.nome}"


class PedidoAdocao(models.Model):
    ESCOLHAS_STATUS = [
        ("pendente", "Pendente"),
        ("aprovado", "Aprovado"),
        ("rejeitado", "Rejeitado"),
    ]

    data_pedido = models.DateTimeField(auto_now_add=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="pedidos")
    adotante = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="pedidos"
    )

    status = models.CharField(
        max_length=20, choices=ESCOLHAS_STATUS, default="pendente"
    )

    def clean(self) -> None:
        if self.pet.dono == self.adotante:
            raise ValidationError("O adotante não pode ser o dono do pet.")

        if self.pet.status != "disponível":
            raise ValidationError("O pet não está disponível para adoção.")

    def __str__(self) -> str:
        return f"Pedido de adoção: {self.pet.nome} por {self.adotante.username}"

    class Meta:
        unique_together = ("pet", "adotante")
