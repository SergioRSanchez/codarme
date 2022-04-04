from rest_framework import serializers
from django.utils import timezone
import re

from agenda.models import Agendamento


class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = (
            "id",
            "data_horario",
            "nome_cliente",
            "email_cliente",
            "telefone_cliente",
        )

    """ data_horario = serializers.DateTimeField()
    nome_cliente = serializers.CharField(max_length=255)
    email_cliente = serializers.EmailField()
    telefone_cliente = serializers.CharField(max_length=20) """

    def validate_data_horario(self, data_horario):
        if data_horario < timezone.now():
            raise serializers.ValidationError("A data e hora devem ser futuras")
        if (
            data_horario.hour < 9
            or data_horario.hour > 11
            and data_horario.hour < 13
            or data_horario.hour > 17
        ):
            raise serializers.ValidationError(
                "O horário deve estar entre 9 e 18 horas. Horário de almoço entre 12 e 13 horas"
            )

        return data_horario

    def validate(self, attrs):
        telefone_cliente = attrs.get("telefone_cliente", "")
        email_cliente = attrs.get("email_cliente", "")

        if (
            email_cliente.endswith(".br")
            and telefone_cliente.startswith("+")
            and not telefone_cliente.startswith("+55")
        ):
            raise serializers.ValidationError(
                "O telefone deve ser no formato +55XX-XXXX-XXXX"
            )
        if len(telefone_cliente) < 8:
            raise serializers.ValidationError(
                "O telefone deve ter pelo menos 8 dígitos"
            )
        for i in telefone_cliente:
            if i == "+" and not telefone_cliente.startswith("+"):
                raise serializers.ValidationError(
                    "Se o número conter o caractere +, ele deve estar no início do telefone"
                )
        validate = r"[0-9+()-]{7}$"
        if not re.search(validate, telefone_cliente):
            raise serializers.ValidationError(
                "O telefone deve conter apenas números ou caracteres especiais"
            )
        if Agendamento.objects.filter(
            email_cliente=email_cliente, data_horario__day=attrs["data_horario"].day
        ).exists():  # está errado, pois ele como mesmo dia de meses diferentes
            raise serializers.ValidationError(
                "O cliente já está cadastrado para um agendamento no dia selecionado"
            )
        # O horário de um agendamento deve ter um espaço de 30 minutos entre outro agendamento
        if Agendamento.objects.filter(
            data_horario__day=attrs["data_horario"].day,
            data_horario__hour=attrs["data_horario"].hour,
        ).exists():
            raise serializers.ValidationError("O horário selecionado já está ocupado")

        return attrs


#  Como estou usando o ModelSerializer, eu não preciso utilizar esses métodos abaixo:
"""     def create(self, validated_data):
        agendamento = Agendamento.objects.create(
            data_horario=validated_data["data_horario"],
            nome_cliente=validated_data["nome_cliente"],
            email_cliente=validated_data["email_cliente"],
            telefone_cliente=validated_data["telefone_cliente"],
        )  # TODO: criar instância de Agendamento com valores validados.
        return agendamento

    def update(self, instance, validated_data):
        instance.data_horario = validated_data.get("data_horario", instance.data_horario)  # Caso o novo valor passado dessa chave seja nulo, ele usa o valor antigo
        instance.nome_cliente = validated_data.get("nome_cliente", instance.nome_cliente)
        instance.email_cliente = validated_data.get("email_cliente", instance.email_cliente)
        instance.telefone_cliente = validated_data.get("telefone_cliente", instance.telefone_cliente)
        instance.save()
        return instance """
