#  Modelo é qualquer entidade que represente algum objeto
from django.db import models

# Create your models here
class Categoria(models.Model):
    nome = models.CharField(max_length=256, blank=False,unique=True)

    def __str__(self):
        return f"{self.nome} <{self.id}>"
    
    @classmethod
    def cria_categoria(cls,nome):
        if not nome:
            raise ValueError("Categoria precisa de um nome.")
        if nome:
            categoria = Categoria(nome=nome)
        categoria.save()
        return categoria

class Evento(models.Model):
    nome = models.CharField(max_length=256)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    local = models.CharField(max_length=256, blank=True)
    link = models.CharField(max_length=256, blank=True)
    data = models.DateField(blank=True)
    participantes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nome} <{self.id}>"

    @classmethod
    def cria_evento(cls, nome, categoria, local=None, link=None, data=None):
        if not nome:
            raise ValueError("Evento precisa de um nome.")
        if not categoria:
            raise ValueError("Evento precisa de uma categoria.")
        if local and link:
            raise ValueError("Evento não pode possuir local E link.")
        if local:
            evento = Evento(nome=nome, categoria=categoria, local=local, data=data)
        if link:
            evento = Evento(nome=nome, categoria=categoria, link=link, data=data)
        evento.save()
        return evento