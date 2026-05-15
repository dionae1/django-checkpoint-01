from django.contrib import admin

from .models import User, Pet, PedidoAdocao, FotoPet


class AdoptionRequestInline(admin.TabularInline):
    model = PedidoAdocao
    extra = 0


class FotoPetInline(admin.TabularInline):
    model = FotoPet
    extra = 1
    fields = ("imagem", "descricao", "data_upload")
    readonly_fields = ("data_upload",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "celular", "cidade", "estado")
    search_fields = ("username", "email", "celular", "cidade", "estado")
    list_filter = ("cidade", "estado")
    ordering = ("id",)


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("nome", "especie", "raca", "idade", "porte", "status", "dono")
    search_fields = ("nome", "especie", "raca", "dono__username")
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
    search_fields = ("pet__nome", "adotante__username")
    list_filter = ("status",)
    ordering = ("-data_pedido",)
    autocomplete_fields = ("pet", "adotante")

    fieldsets = (
        ("Informações", {"fields": ("pet", "adotante")}),
        ("Status do Pedido", {"fields": ("status",)}),
    )
