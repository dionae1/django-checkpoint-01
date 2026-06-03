from adocao.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from adocao.utils import formatar_celular_brasileiro, somente_digitos


class CelularBRField(forms.CharField):
    def prepare_value(self, value):
        return formatar_celular_brasileiro(value)

    def to_python(self, value):
        value = super().to_python(value)
        return somente_digitos(value)

    def validate(self, value):
        super().validate(value)

        if value and len(value) not in (10, 11):
            raise forms.ValidationError(
                "Informe um número de celular válido com DDD."
            )


class FormularioAutenticacao(AuthenticationForm):
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


class FormularioCadastro(UserCreationForm):
    celular = CelularBRField(
        label="Número de celular",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "autocomplete": "tel",
                "inputmode": "tel",
                "placeholder": "(11) 99999-9999",
            }
        ),
    )

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
            "cidade": forms.TextInput(
                attrs={"class": "form-control", "autocomplete": "address-level2"}
            ),
            "estado": forms.TextInput(
                attrs={"class": "form-control", "autocomplete": "address-level1"}
            ),
        }


class FormularioAtualizacao(forms.ModelForm):
    celular = CelularBRField(
        label="Número de celular",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "autocomplete": "tel",
                "inputmode": "tel",
                "placeholder": "(11) 99999-9999",
            }
        ),
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "celular", "cidade", "estado")
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "autocomplete": "given-name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "autocomplete": "family-name"}
            ),
            "cidade": forms.TextInput(
                attrs={"class": "form-control", "autocomplete": "address-level2"}
            ),
            "estado": forms.TextInput(
                attrs={"class": "form-control", "autocomplete": "address-level1"}
            ),
        }
