from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import FormularioCadastro, FormularioAtualizacao


def cadastrar_usuario(request):

    if request.method == "POST":
        form = FormularioCadastro(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

    form = FormularioCadastro()
    return render(request, "cadastro.html", {"form": form})


@login_required
def atualizar_usuario(request):
    if request.method == "POST":
        form = FormularioAtualizacao(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return render(
                request,
                "perfil.html",
                {"form": form, "message": "Dados atualizados com sucesso!"},
            )

    form = FormularioAtualizacao(instance=request.user)
    return render(request, "perfil.html", {"form": form})
