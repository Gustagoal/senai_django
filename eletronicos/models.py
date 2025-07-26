from django.db import models

# Create your models here.
categorias = (
    ("Celular", "Celular"),
    ("Notebook", "Notebook"),
    ("Fones", "Fones"),
    ("Computadores", "Computadores"),
)
status_opcoes = (
    (False, "pendente"),
    (True, "Concluido"),
)


class UsuariosModel(models.Model):
    categorias = models.CharField(choices=categorias)
    email = models.EmailField()
    produto = models.CharField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True, choices=status_opcoes)
