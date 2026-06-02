from django.contrib.auth import login, logout
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm


def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = CustomUserCreationForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")

    return render(request, "register.html", {"form": form})
