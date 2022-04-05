from cgitb import lookup
from functools import partial
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

from datetime import datetime

from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer


# Create your views here.

""" A gente começou construindo nossa view passo a passo, mostrando todo o processo, pegando item por item no banco de
dados, para no final construir ela usando uma API Genérica, que é uma API que faz o CRUD de forma genérica, com muitas
funções prontas, como o Create, Update, Delete, List, Retrieve, etc. """


class AgendamentoList(generics.ListCreateAPIView):  # /api/agendamentos/
    queryset = Agendamento.objects.exclude(horario_cancelado=True)
    serializer_class = AgendamentoSerializer


class AgendamentoDetail(
    generics.RetrieveUpdateDestroyAPIView  # faz todo o CRUD de um único item
):  # /api/agendamentos/<pk>/
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

    def perform_destroy(self, instance):
        instance.horario_cancelado = True
        instance.save()


""" 
====> Class Based View do Agendamento Detail usando mixins
class AgendamentoDetail(
    mixins.RetrieveModelMixin,  # RetrieveModelMixin -> Retorna um objeto específico
    mixins.UpdateModelMixin,  # UpdateModelMixin -> Atualiza um objeto específico
    mixins.DestroyModelMixin,  # DestroyModelMixin -> Deleta um objeto específico
    generics.GenericAPIView,
):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    # lookup_field = 'id'  # Para que o id seja o campo de busca
    #  Porém, preferimos por utilizar o 'pk', já que estamos usando muitas abstrações do django rest framework, tentamos customizar o menor número possível

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



====> Class Based View do Agendamento List usando mixins
class AgendamentoList(
    mixins.ListModelMixin,  # Adicionar mixin de listagem
    mixins.CreateModelMixin,  # Adicionar mixin de criação
    generics.GenericAPIView,  # Classe genérica de API
):
    queryset = Agendamento.objects.exclude(horario_cancelado=True)
    serializer_class = AgendamentoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs) 
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




====> Class Based View do Agendamento Detail usando APIView
class AgendaDetail(APIView):
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(obj)
        return JsonResponse(serializer.data, status=200)

class AgendaDetail(APIView):
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
class AgendaDetail(APIView):
        obj = get_object_or_404(Agendamento, id=id)
        obj.horario_cancelado = True
        obj.save()
        return JsonResponse({}, status=204) 



=====> Class Based View do Agendamento Detail usando APIView
class AgendaDetail(APIView):
        queryset = Agendamento.objects.exclude(horario_cancelado=True)
        serializer = AgendamentoSerializer(queryset, many=True)  # many=True indica que o objeto sendo serializado é uma coleção
        return JsonResponse(serializer.data, safe=False)

class AgendaDetail(APIView):
        data = request.data
        serializer = AgendamentoSerializer(data=data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400) 
"""


@api_view(
    http_method_names=["GET"]
)  #  Temos que fazer a get_horarios_disponiveis em agenda/utils.py para funcionar
def get_horarios(request):
    data = request.query_params.get("data")
    if not data:
        data = datetime.now().date()
    else:
        data = datetime.fromisoformat(data).date()

    horarios_disponiveis = sorted(list(get_horarios_disponiveis(data)))
    return JsonResponse(horarios_disponiveis, safe=False)


"""
# Esse tipo de estrutura é chamado de "Function based view", ou seja, views baseadas em funções
#  Irei deixar comentado os métodos abaixo, pois eles não são necessários, mas deixei para consultas posteriores

=====> Function Based View do Agendamento Detail

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


====> Function Based View do Agendamento List

@api_view(http_method_names=["GET", "POST"]) 
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
"""
