from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect

from .models import Pet, FotoPet, PedidoAdocao
from .forms import FormularioCadastroPet, FormularioDetalhesPet


@login_required
def home(request):
    user = request.user
    template = loader.get_template("home.html")

    context = {
        "user": user,
    }

    return HttpResponse(template.render(context, request))


@login_required
def lista_pets(request):
    user = request.user
    user_pets = (
        Pet.objects.filter(dono=user)
        .prefetch_related("fotos")
        .order_by("status", "nome")
        .reverse()
    )

    for pet in user_pets:
        pet.foto_principal = pet.fotos.first()  # type: ignore

    template = loader.get_template("lista_pets.html")

    context = {
        "user": user,
        "pets": user_pets,
    }

    return HttpResponse(template.render(context, request))


@login_required
def novo_pet(request):

    if request.method == "POST":
        form = FormularioCadastroPet(request.POST, request.FILES)
        files = request.FILES.getlist("fotos")
        if form.is_valid():
            pet = Pet(
                nome=form.cleaned_data["nome"],
                especie=form.cleaned_data["especie"],
                raca=form.cleaned_data["raca"],
                idade=form.cleaned_data["idade"],
                porte=form.cleaned_data["porte"],
                descricao=form.cleaned_data["descricao"],
                vacinado=form.cleaned_data["vacinado"],
                castrado=form.cleaned_data["castrado"],
            )

            pet.dono = request.user
            pet.save()
            for file in files:
                FotoPet.objects.create(pet=pet, imagem=file)
            return redirect("lista_pets")
    else:
        form = FormularioCadastroPet()

    return render(request, "novo_pet.html", {"form": form})


@login_required
def detalhes_pet(request, pet_id):
    if request.method == "POST":
        form = FormularioDetalhesPet(request.POST)
        files = request.FILES.getlist("fotos")

        if form.is_valid():
            pet = Pet.objects.get(id=pet_id, dono=request.user)
            pet.nome = form.cleaned_data["nome"]
            pet.especie = form.cleaned_data["especie"]
            pet.raca = form.cleaned_data["raca"]
            pet.idade = form.cleaned_data["idade"]
            pet.porte = form.cleaned_data["porte"]
            pet.descricao = form.cleaned_data["descricao"]
            pet.vacinado = form.cleaned_data["vacinado"]
            pet.castrado = form.cleaned_data["castrado"]
            pet.save()

            if files:
                pet.fotos.all().delete()  # type: ignore

            for file in files:
                FotoPet.objects.create(pet=pet, imagem=file)

            return redirect("lista_pets")

    pet = Pet.objects.get(id=pet_id, dono=request.user)
    fotos = pet.fotos_carrossel()
    form = FormularioDetalhesPet(
        initial={
            "nome": pet.nome,
            "especie": pet.especie,
            "raca": pet.raca,
            "idade": pet.idade,
            "porte": pet.porte,
            "descricao": pet.descricao,
            "vacinado": pet.vacinado,
            "castrado": pet.castrado,
        }
    )

    return render(
        request, "detalhes_pet.html", {"form": form, "pet": pet, "fotos": fotos}
    )


@login_required
def deletar_pet(request, pet_id):
    pet = Pet.objects.get(id=pet_id, dono=request.user)
    pet.delete()
    return redirect("lista_pets")


@login_required
def lista_adocao(request):
    user = request.user
    pets_disponiveis = (
        Pet.objects.filter(status="disponível")
        .exclude(dono=user)
        .prefetch_related("fotos")
    )

    for pet in pets_disponiveis:
        pet.foto_principal = pet.fotos.first()  # type: ignore

    template = loader.get_template("lista_adocao.html")

    context = {
        "user": user,
        "pets": pets_disponiveis,
    }

    return HttpResponse(template.render(context, request))


@login_required
def detalhes_adocao(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    fotos = pet.fotos_carrossel()  # type: ignore

    solicitacao_existente = PedidoAdocao.objects.filter(
        pet=pet, adotante=request.user
    ).exists()

    return render(
        request,
        "detalhes_adocao.html",
        {"pet": pet, "fotos": fotos, "solicitacao_existente": solicitacao_existente},
    )


@login_required
def solicitar_adocao(request, pet_id):
    if request.method == "POST":
        pet = Pet.objects.get(id=pet_id)
        fotos = pet.fotos_carrossel()

        PedidoAdocao.objects.create(pet=pet, adotante=request.user)

        return render(
            request,
            "detalhes_adocao.html",
            {
                "pet": pet,
                "fotos": fotos,
                "message": "Pedido de adoção enviado com sucesso!",
                "solicitacao_existente": True,
            },
        )

    return redirect("detalhes_adocao", pet_id=pet_id)


@login_required
def lista_solicitacoes(request):
    user = request.user

    solicitacoes_recebidas = PedidoAdocao.objects.filter(pet__dono=user).select_related(
        "pet", "adotante"
    )

    solicitacoes_recebidas_aprovadas = solicitacoes_recebidas.filter(status="aprovado")
    solicitacoes_recebidas_rejeitadas = solicitacoes_recebidas.filter(
        status="rejeitado"
    )
    solicitacoes_recebidas_pendentes = solicitacoes_recebidas.filter(status="pendente")

    solicitacoes_enviadas = PedidoAdocao.objects.filter(adotante=user).select_related(
        "pet", "pet__dono"
    )

    solicitacoes_enviadas_pendentes = solicitacoes_enviadas.filter(status="pendente")
    solicitacoes_enviadas_aprovadas = solicitacoes_enviadas.filter(status="aprovado")
    solicitacoes_enviadas_rejeitadas = solicitacoes_enviadas.filter(status="rejeitado")

    return render(
        request,
        "lista_solicitacoes.html",
        {
            "solicitacoes_recebidas_pendentes": solicitacoes_recebidas_pendentes,
            "solicitacoes_recebidas_aprovadas": solicitacoes_recebidas_aprovadas,
            "solicitacoes_recebidas_rejeitadas": solicitacoes_recebidas_rejeitadas,
            "solicitacoes_enviadas_pendentes": solicitacoes_enviadas_pendentes,
            "solicitacoes_enviadas_aprovadas": solicitacoes_enviadas_aprovadas,
            "solicitacoes_enviadas_rejeitadas": solicitacoes_enviadas_rejeitadas,
        },
    )


@login_required
def aceitar_solicitacao(request, solicitacao_id):
    solicitacao = PedidoAdocao.objects.get(id=solicitacao_id, pet__dono=request.user)
    solicitacao.status = "aprovado"
    solicitacao.save()
    return redirect("lista_solicitacoes")


@login_required
def rejeitar_solicitacao(request, solicitacao_id):
    solicitacao = PedidoAdocao.objects.get(id=solicitacao_id, pet__dono=request.user)
    solicitacao.status = "rejeitado"
    solicitacao.save()
    return redirect("lista_solicitacoes")
