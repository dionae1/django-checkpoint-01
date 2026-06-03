from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, UserUpdateForm


@login_required
def register(request):

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

    form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})


@login_required
def atualizar_usuario(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return render(
                request,
                "update.html",
                {"form": form, "message": "Dados atualizados com sucesso!"},
            )

    form = UserUpdateForm(instance=request.user)
    return render(request, "update.html", {"form": form})
