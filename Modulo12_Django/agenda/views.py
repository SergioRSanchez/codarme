from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


from agenda.models import Evento, Categoria
from datetime import date


# Create your views here.
def listar_eventos(request):
    #  Buscar os eventos criados no banco
    eventos = Evento.objects.exclude(data__lt=date.today()).order_by("data")
    #  Exibir um template listando esses eventos
    return render(
        request=request,
        context={"eventos": eventos},
        template_name="agenda/listar_eventos.html",
    )


def listar_categorias(request):
    eventos = Categoria.objects.all()
    return render(
        request=request,
        context={"eventos": eventos},
        template_name="agenda/listar_categorias.html",
    )


def exibir_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    return render(
        request=request,
        context={"evento": evento},
        template_name="agenda/exibir_evento.html",
    )


def exibir_categoria(request, id):
    categorias = get_object_or_404(Categoria, id=id)
    eventos = Evento.objects.filter(categoria=categorias)
    eventos_contagem = eventos.count()
    return render(
        request=request,
        context={"categoria": categorias, "contagem": eventos_contagem},
        template_name="agenda/exibir_categoria.html",
    )


def participar_evento(request):
    evento_id = request.POST.get("evento_id")
    evento = get_object_or_404(Evento, id=evento_id)
    evento.participantes += 1
    evento.save()

    return HttpResponseRedirect(reverse("exibir_evento", args=(evento_id,)))
