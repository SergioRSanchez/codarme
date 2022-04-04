from functools import partial
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from datetime import datetime

from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer


# Create your views here.

class AgendamentoDetail(APIView):
    def get(self, request, id):
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(obj)
        return JsonResponse(serializer.data, status=200)
    def patch(self, request, id):
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    def delete(self, request, id):
        obj = get_object_or_404(Agendamento, id=id)
        obj.horario_cancelado = True
        obj.save()
        return JsonResponse({}, status=204)
        

class AgendamentoList(APIView):  #  Esse tipo de estrutura é chamado de "Class based view", ou seja, views baseadas em classes
    def get(self, request):
        queryset = Agendamento.objects.exclude(horario_cancelado=True)
        serializer = AgendamentoSerializer(queryset, many=True)  # many=True indica que o objeto sendo serializado é uma coleção
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request):
        data = request.data
        serializer = AgendamentoSerializer(data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(http_method_names=["GET"]) 
def get_horarios(request):
    data = request.query_params.get("data")
    if not data:
        data = datetime.now().date()
    else:
        data = datetime.fromisoformat(data).date()
    
    horarios_disponiveis = sorted(list(get_horarios_disponiveis(data)))
    return JsonResponse(horarios_disponiveis, safe=False)

#  Ainda não está certo, irei voltar posteriormente para melhorar.


'''  # Esse tipo de estrutura é chamado de "Function based view", ou seja, views baseadas em funções
     #  Irei deixar comentado os métodos abaixo, pois eles não são necessários, mas deixei para consultas posteriores

@api_view(http_method_names=["GET", "PUT", "PATCH", "DELETE"])
def agendamento_detail(request, id):  
    obj = get_object_or_404(Agendamento, id=id)
    if request.method == "GET":
        #  Buscar instância de Agendamento
        #  Instanciar serializer passando a instância de Agendamento
        serializer = AgendamentoSerializer(obj)
        #  Retornar JsonResponse com os dados do serializer
        return JsonResponse(serializer.data, status=200)
        
    if request.method == "PUT":  #  Esse método não se faz necessário, visto que temos o método Patch listado abaixo, porém deixei para posteriores consultas se necessárias
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            obj.data_horario = validated_data.get("data_horario", obj.data_horario)  # Caso o novo valor passado dessa chave seja nulo, ele usa o valor antigo
            obj.nome_cliente = validated_data.get("nome_cliente", obj.nome_cliente)
            obj.email_cliente = validated_data.get("email_cliente", obj.email_cliente)
            obj.telefone_cliente = validated_data.get("telefone_cliente", obj.telefone_cliente)
            obj.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    if request.method == "PATCH":
        serializer = AgendamentoSerializer(obj, data=request.data, partial=True)  #  O partial é para que ,nesse caso, o requirimento das chaves no serializer não sejam todas obrigatório, fazendo com que eu não precise passar todas as chaves.
        #  Se a gente passar a instância, representada por 'obj', a gene vai atualizar aquele objeto
        if serializer.is_valid():
            serializer.save()  # A FrameWork do Rest tem vários métodos e ordem de chamadas dos métodos, e nesse caso ele está chamando o método update no nosso Serializer em algum momentos
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    if request.method == "DELETE":
        #  obj.delete()  # Ao invés de deletar e perder aquele registro, quero deixar salvo que foi cancelado, podendo dessa maneira exibir uma lista de objetos cancelados
        obj.horario_cancelado = True  # Para isso tenho que criar um atributo "cancelado" em models.py, e fazer a migração. Quando criamos o objeto, esse atributo está como 'False', e quando cancelamos, ele deve virar 'True'
        obj.save()
        return Response(status=204)
'''

'''@api_view(http_method_names=["GET", "POST"]) 
def agendamento_list(request):
    if request.method == "GET":
        queryset = Agendamento.objects.exclude(horario_cancelado=True)
        serializer = AgendamentoSerializer(queryset, many=True)  # many=True indica que o objeto sendo serializado é uma coleção
        return JsonResponse(serializer.data, safe=False)  # safe=False: permite serialização de objetos que não são dicionários (lista)
    if request.method == "POST":
        data = request.data  #  {"nome_cliente": "Gabriel"...} -> Essa facilidade vem da api_view
        # Criar serializer a partir de `data`
        serializer = AgendamentoSerializer(data=data)  # Passando somente o 'data' a gente cria o objeto
        if serializer.is_valid():  #  Faz toda aquela validação que fazíamos manualmente
            validated_data = serializer.validated_data  #  Quando o serializer.is_valid() está certo, automaticamente o serializer.validated_data é populado
            serializer.save()  # A FrameWork do Rest tem vários métodos e ordem de chamadas dos métodos, e nesse caso ele está chamando o método create no nosso Serializer em algum momentos
            return JsonResponse(serializer.data, status=201)
        # TODO: retornar JsonResponse com os erros do serializer e status 400
        return JsonResponse(serializer.errors, status=400)
'''