from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer




# Create your views here.

@api_view(http_method_names=["GET"])
def agendamento_detail(request, id):
    if request.method == "GET":
        #  Buscar instância de Agendamento
        obj = get_object_or_404(Agendamento, id=id)
        #  Instanciar serializer passando a instância de Agendamento
        serializer = AgendamentoSerializer(obj)
        #  Retornar JsonResponse com os dados do serializer
        return JsonResponse(serializer.data, status=200)



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