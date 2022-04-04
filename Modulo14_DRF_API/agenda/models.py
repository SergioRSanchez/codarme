from django.db import models

# Create your models here.


class Agendamento(models.Model):
    data_horario = models.DateTimeField()
    nome_cliente = models.CharField(max_length=255)
    email_cliente = models.EmailField()
    telefone_cliente = models.CharField(max_length=20)
    horario_cancelado = models.BooleanField(default=False)
