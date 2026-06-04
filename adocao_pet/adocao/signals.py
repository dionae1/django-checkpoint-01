from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import PedidoAdocao


@receiver(post_save, sender=PedidoAdocao)
def apply_adoption(sender, instance: PedidoAdocao, created, **kwargs):
    """When a PedidoAdocao is approved, mark the pet as adopted and transfer owner.

    This runs after the PedidoAdocao is saved; it does nothing if the pet is
    already adopted.
    """
    if instance.status != "aprovado":
        return

    pet = instance.pet
    # if already adopted, no action
    if pet.status == "adotado":
        return

    with transaction.atomic():
        pet.status = "adotado"
        # Manter o dono original do pet para salvar o histórico.
        # Rastrear o dono novo pelo pedido aprovado.
        # pet.dono = instance.adotante
        pet.save()
