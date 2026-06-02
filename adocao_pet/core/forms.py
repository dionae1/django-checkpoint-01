from adocao.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={"class": "form-control", "autocomplete": "email"}
        ),
    )

    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "autocomplete": "current-password"}
        ),
    )


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "celular", "cidade", "estado")
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "autocomplete": "given-name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "autocomplete": "family-name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "autocomplete": "email"}
            ),
            "celular": forms.TextInput(
                attrs={"class": "form-control", "autocomplete": "tel"}
            ),
            "cidade": forms.TextInput(
                attrs={"class": "form-control", "autocomplete": "address-level2"}
            ),
            "estado": forms.TextInput(
                attrs={"class": "form-control", "autocomplete": "address-level1"}
            ),
        }
