from django.shortcuts import render, redirect
from eletronicos.forms import CadastroForm
from eletronicos.models import UsuariosModel
from django.shortcuts import get_object_or_404


def home(request):
    if request.method == "POST":
        form = CadastroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("Usuarios")
    else:
        form = CadastroForm()
    return render(request, "eletronicos/index.html", {"form": form})


def mostrar_usuarios(request):
    usuarios = UsuariosModel.objects.all()
    return render(request, "eletronicos/usuarios.html", {"usuarios": usuarios})


def remover_usuarios(request, id):
    usuarios = get_object_or_404(UsuariosModel, id=id)
    usuarios.delete()
    return redirect("Usuarios")
