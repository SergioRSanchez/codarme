#  Modelo é qualquer entidade que represente algum objeto
from django.db import models

# Create your models here.9
class Categoria(models.Model):
    nome = models.CharField(max_length=256, unique=True)  #  CharField é texto

    def __str__(self):
        return f"{self.nome} <{self.id}>"

class Evento(models.Model):
    nome = models.CharField(max_length=256)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    local = models.CharField(max_length=256, blank=True)
    link = models.CharField(max_length=256, blank=True)
    data = models.DateField(null=True)
    participantes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nome} <{self.id}>"

    @classmethod
    def cria_evento(cls, nome, local, link, data, participantes):
        evento = cls(nome, local="Rio Preto", link=f"https://tamarcado.com/eventos?id={cls.id}", data=data, participantes=participantes)
        evento = Evento(nome, local, link, data, participantes)
        return evento