from django import forms
from eletronicos.models import UsuariosModel


class CadastroForm(forms.ModelForm):
    class Meta:
        model = UsuariosModel
        exclude = ["status", "imagem", "email"]
