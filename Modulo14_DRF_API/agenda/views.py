from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer


# Create your views here.

@api_view(http_method_names=["GET", "PUT", "PATCH", "DELETE"])
def agendamento_detail(request, id):
    if request.method == "GET":
        #  Buscar instância de Agendamento
        obj = get_object_or_404(Agendamento, id=id)
        #  Instanciar serializer passando a instância de Agendamento
        serializer = AgendamentoSerializer(obj)
        #  Retornar JsonResponse com os dados do serializer
        return JsonResponse(serializer.data, status=200)
    if request.method == "PUT":
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            obj.data_horario = validated_data.get("data_horario", obj.data_horario)  # caso o novo valor passado dessa chave seja nulo, ele usa o valor antigo
            obj.nome_cliente = validated_data.get("nome_cliente", obj.nome_cliente)
            obj.email_cliente = validated_data.get("email_cliente", obj.email_cliente)
            obj.telefone_cliente = validated_data.get("telefone_cliente", obj.telefone_cliente)
            obj.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    if request.method == "PATCH":
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(data=request.data, partial=True)  #  o partial é para que ,nesse caso, o requirimento das chaves no serializer não sejam todas obrigatório, fazendo com que eu não precise passar todas as chaves
        if serializer.is_valid():
            validated_data = serializer.validated_data
            obj.data_horario = validated_data.get("data_horario", obj.data_horario)  # caso o novo valor passado dessa chave seja nulo, ele usa o valor antigo
            obj.nome_cliente = validated_data.get("nome_cliente", obj.nome_cliente)
            obj.email_cliente = validated_data.get("email_cliente", obj.email_cliente)
            obj.telefone_cliente = validated_data.get("telefone_cliente", obj.telefone_cliente)
            obj.save()
            return JsonResponse(validated_data, status=200)
        return JsonResponse(serializer.errors, status=400)
    if request.method == "DELETE":
        obj = get_object_or_404(Agendamento, id=id)
        #  obj.delete()  # ao invés de deletar e perder aquele registro, quero deixar salvo que foi cancelado, podendo dessa maneira exibir uma lista de objetos cancelados
        obj.horario_cancelado = True  # para isso tenho que criar um atributo "cancelado" em models.py, e fazer a migração. Quando criamos o objeto, esse atributo está como 'False', e quando cancelamos, ele deve virar 'True'
        obj.save()
        return Response(status=204)

#  Os objetos cancelados deve ser removidos da listagem de agendamento abaixo
#  Como requisito, não deve aparecer o atributo 'cancelado', portanto não devo mexer no AgendamentoSerializer, somente em models.py mesmo


@api_view(http_method_names=["GET", "POST"]) 
def agendamento_list(request):
    if request.method == "GET":
        queryset = Agendamento.objects.all()
        serializer = AgendamentoSerializer(queryset, many=True)  # many=True indica que o objeto sendo serializado é uma coleção
        return JsonResponse(serializer.data, safe=False)  # safe=False: permite serialização de objetos que não são dicionários (lista)
    if request.method == "POST":
        data = request.data  #  {"nome_cliente": "Gabriel"...} -> Essa facilidade vem da api_view
        # Criar serializer a partir de `data`
        serializer = AgendamentoSerializer(data=data)
        if serializer.is_valid():  #  Faz toda aquela validação que fazíamos manualmente
            validated_data = serializer.validated_data  #  quando o serializer.is_valid() está certo, automaticamente o serializer.validated_data é populado
            Agendamento.objects.create(
                data_horario=validated_data["data_horario"],
                nome_cliente=validated_data["nome_cliente"],
                email_cliente=validated_data["email_cliente"],
                telefone_cliente=validated_data["telefone_cliente"],
            )  # TODO: criar instância de Agendamento com valores validados.
            return JsonResponse(serializer.data, status=201)
        # TODO: retornar JsonResponse com os erros do serializer e status 400
        return JsonResponse(serializer.errors, status=400)



