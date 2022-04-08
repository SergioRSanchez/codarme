import pytz
from rest_framework import serializers
from django.utils import timezone
from datetime import timedelta, date, datetime, time, tzinfo
import re
from django.forms import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from rest_framework.validators import UniqueValidator

from agenda.models import Agendamento
from agenda import utils


class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = (
            "id",
            "data_horario",
            "nome_cliente",
            "email_cliente",
            "telefone_cliente",
            "prestador",
        )

    """ ao invés de ficar declarando todos os campos, podemos usar o " fields = '__all__' ", porém ele expõem todos os dados
do nosso modelo, e não é o que queremos no caso, pois não queremos mostrar o campo de 'horario_cancelado'. """

    """ data_horario = serializers.DateTimeField()
    nome_cliente = serializers.CharField(max_length=255)
    email_cliente = serializers.EmailField()
    telefone_cliente = serializers.CharField(max_length=20) """

    """ Tem uma ordem em que as coisas são executadas no serializer:
    1) Tipos passados => vai verificar se o tipo é int e está passando str por exemplo
    2) Depois ele procura as validações específicas, como validate_prestador
    3) Por último ele verifica a validação geral (object-level) => que é o método validate """

    # No caso iria parar na primeira validação, pois ele entende que é um int e estamos passando uma str
    # Portanto devemos converter ele em charfield
    prestador = serializers.CharField()

    def validate_prestador(self, value):  # value = usuario1
        # é obrigatório passar o prestador, porém ele estava em formato 'pk', agora vamos buscar pelo username também
        try:
            prestador_obj = User.objects.get(username=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("Esse prestador de serviços não existe")
        return prestador_obj

    def validate_data_horario(self, value):
        # não pode horários passados
        if value < timezone.now():
            raise serializers.ValidationError("A data e hora devem ser futuras")
        # não pode fora do horário de serviço
        if (
            (
                (0 <= value.weekday() <= 4)
                and not (
                    (time(hour=9) <= value.time() < time(hour=12))
                    or (time(hour=13) <= value.time() < time(hour=18))
                )
            )
            or (
                value.weekday() == 5
                and not (time(hour=9) <= value.time() < time(hour=13))
            )
            or (value.weekday() == 6)
        ):
            raise serializers.ValidationError(
                "Agendamentos apenas de segunda a sexta das 9 às 12 pela manhã e das 13 às 18 pela tarde ou no sábado das 9 às 13!"
            )

        if value not in utils.get_horarios_disponiveis(value.date()):
            raise serializers.ValidationError("Esse horário não está disponível.")

        return value

    def validate_telefone_cliente(self, attrs):
        telefone_cliente = attrs
        # pelo menos 8 caracteres
        if len(telefone_cliente) < 8:
            raise serializers.ValidationError(
                "O telefone deve ter pelo menos 8 dígitos"
            )
        # conter somente números e caracteres especiais, se conter o '+'deve vir no inicio
        for char in telefone_cliente:
            if char not in "0123456789+-()":
                raise serializers.ValidationError(
                    "O telefone deve conter apenas números e os caracteres especiais + e ()"
                )
            if char in "+" and not telefone_cliente.startswith("+"):
                raise serializers.ValidationError(
                    "O sinal de '+' apenas pode ser utilizado no começo do número de telefone."
                )
        return attrs

    """ validate = r"[0-9+()-]{7}$"
        if not re.search(validate, telefone_cliente):
            raise serializers.ValidationError(
                "O telefone deve conter apenas números ou caracteres especiais"
            ) """

    def validate(self, attrs):
        telefone_cliente = attrs.get("telefone_cliente", "")
        email_cliente = attrs.get("email_cliente", "")
        data_horario = attrs.get("data_horario", "")
        if data_horario:
            data_horario = datetime.fromisoformat(str(data_horario)).replace(
                tzinfo=pytz.UTC
            )
        # se terminado em '.br' e possuir o '+' deve ser seguido por 55
        if (
            email_cliente.endswith(".br")
            and telefone_cliente.startswith("+")
            and not telefone_cliente.startswith("+55")
        ):
            raise serializers.ValidationError(
                "Email brasileiro deve conter telefone brasileiro."
            )
        # validação das regras de horário
        if data_horario:
            list_email = (
                Agendamento.objects.filter(email_cliente=email_cliente)
                .filter(horario_cancelado=False)
                .dates("data_horario", "day")
            )
            # recusa agendamento caso cliente (email) já tenha marcado um horário no dia
            if data_horario.date() in list_email:
                raise serializers.ValidationError(
                    "Cliente já marcou um horário para esse dia."
                )
            data_inicial = data_fim = data_horario - timedelta(
                hours=data_horario.hour, minutes=data_horario.minute
            )
            data_fim += timedelta(hours=23, minutes=59)
            list_horarios_dia = (
                Agendamento.objects.filter(data_horario__gt=data_inicial)
                .filter(data_horario__lt=data_fim)
                .filter(horario_cancelado=True)
                .datetimes("data_horario", "minute")
            )
            # recusa horários indisponíveis
            # horários cancelados são desconsiderados
            if data_horario in list_horarios_dia:
                raise serializers.ValidationError("Horário indisponível.", code=200)
        return attrs


class PrestadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "agendamentos"]

    agendamentos = AgendamentoSerializer(
        many=True, read_only=True
    )  # ou seja, pra cada agendamento que tiver, ele vai usar o AgendamentoSerializer, exibindo todos os agendamentos com seus campos


class SignUpUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )


# Isso se chama Nested Relationship, que é uma relação entre serializers. Portanto eu tenho um serializer que tem outro serializer dentro dele

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
