from django import forms


class MultipleImageInput(forms.ClearableFileInput):
    allow_multiple_selected = True

    def __init__(self, attrs=None):
        default_attrs = {"class": "form-control", "multiple": True}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)


class MultipleImageField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs["widget"] = MultipleImageInput()
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class PetForm(forms.Form):
    nome = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Nome do pet"}
        ),
    )
    especie = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ex: Cão, gato"}
        ),
    )
    raca = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Raça"}),
    )
    idade = forms.IntegerField(
        min_value=0,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Idade em anos"}
        ),
    )
    porte = forms.ChoiceField(
        choices=[
            ("", "Selecione o porte"),
            ("pequeno", "Pequeno"),
            ("médio", "Médio"),
            ("grande", "Grande"),
        ],
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    descricao = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "rows": 4, "placeholder": "Descreva o pet"}
        )
    )
    vacinado = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )
    castrado = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )
    fotos = MultipleImageField(required=False)


class DetalhesPetForm(forms.Form):
    nome = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    especie = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    raca = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={"class": "form-control"})
    )
    idade = forms.IntegerField(
        min_value=0, widget=forms.NumberInput(attrs={"class": "form-control"})
    )
    porte = forms.ChoiceField(
        choices=[
            ("", "Selecione o porte"),
            ("pequeno", "Pequeno"),
            ("médio", "Médio"),
            ("grande", "Grande"),
        ],
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    descricao = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 4})
    )
    vacinado = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )
    castrado = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )
    fotos = MultipleImageField(required=False)