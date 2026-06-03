from django.contrib import admin
from django.utils.html import format_html

from .models import FotoPet, PedidoAdocao, Pet, User


class AdoptionRequestInline(admin.TabularInline):
    model = PedidoAdocao
    extra = 0


class FotoPetInline(admin.TabularInline):
    model = FotoPet
    extra = 1
    fields = ("preview_imagem", "imagem", "descricao", "data_upload")
    readonly_fields = ("preview_imagem", "data_upload")

    def preview_imagem(self, obj):
        if not obj or not getattr(obj, "imagem", None):
            return "Sem imagem"

        if not obj.imagem:
            return "Sem imagem"

        return format_html(
            '<a href="{}" target="_blank">'
            '<img src="{}" style="max-height: 90px; max-width: 90px; object-fit: cover; border-radius: 6px;" />'
            "</a>",
            obj.imagem.url,
            obj.imagem.url,
        )

    preview_imagem.short_description = "Preview"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
        "celular_formatado_admin",
        "cidade",
        "estado",
    )
    search_fields = ("username", "email", "celular", "cidade", "estado", "first_name", "last_name")
    list_filter = ("cidade", "estado")
    ordering = ("id",)

    @admin.display(description="Celular", ordering="celular")
    def celular_formatado_admin(self, obj):
        return obj.celular_formatado


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("nome", "especie", "raca", "idade", "porte", "status", "dono")
    search_fields = ("nome", "especie", "raca", "dono__first_name", "dono__last_name")
    list_filter = ("status", "porte")
    ordering = ("nome",)
    inlines = [FotoPetInline, AdoptionRequestInline]
    fieldsets = (
        (
            "Informações Básicas",
            {"fields": ("nome", "especie", "raca", "idade", "porte", "descricao")},
        ),
        ("Saúde", {"fields": ("vacinado", "castrado")}),
        ("Adoção", {"fields": ("dono", "status")}),
    )


@admin.register(PedidoAdocao)
class PedidoAdocaoAdmin(admin.ModelAdmin):
    list_display = ("data_pedido", "pet", "adotante", "status")
    search_fields = ("pet__nome", "adotante__first_name", "adotante__last_name")
    list_filter = ("status",)
    ordering = ("-data_pedido",)
    autocomplete_fields = ("pet", "adotante")

    fieldsets = (
        ("Informações", {"fields": ("pet", "adotante")}),
        ("Status do Pedido", {"fields": ("status",)}),
    )
