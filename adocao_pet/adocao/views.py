from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect

from .models import Pet, FotoPet
from .forms import PetForm, DetalhesPetForm


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
    user_pets = Pet.objects.filter(dono=user).prefetch_related("fotos")

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
        form = PetForm(request.POST, request.FILES)
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
        form = PetForm()

    return render(request, "novo_pet.html", {"form": form})


@login_required
def detalhes_pet(request, pet_id):
    if request.method == "POST":
        form = DetalhesPetForm(request.POST)
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

            for file in files:
                FotoPet.objects.create(pet=pet, imagem=file)

            return redirect("lista_pets")

    pet = Pet.objects.get(id=pet_id, dono=request.user)
    fotos = pet.fotos.all()  # type: ignore
    form = DetalhesPetForm(
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
