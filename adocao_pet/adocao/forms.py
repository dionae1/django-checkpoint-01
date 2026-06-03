from django import forms


class MultipleImageInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleImageField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs["widget"] = MultipleImageInput
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class PetForm(forms.Form):
    nome = forms.CharField(max_length=100)
    especie = forms.CharField(max_length=100)
    raca = forms.CharField(max_length=100)
    idade = forms.IntegerField()
    porte = forms.ChoiceField(
        choices=[
            ("pequeno", "Pequeno"),
            ("médio", "Médio"),
            ("grande", "Grande"),
        ]
    )
    descricao = forms.CharField(widget=forms.Textarea)
    vacinado = forms.BooleanField(required=False)
    castrado = forms.BooleanField(required=False)
    fotos = MultipleImageField(required=False)
