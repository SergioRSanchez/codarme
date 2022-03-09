from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse

from agenda.models import Evento
from datetime import date


# Create your views here.
def listar_eventos(request):
    #  Buscar os eventos criados no banco
    eventos = Evento.objects.filter(data__gte=date.today()).order_by('data')
    #  Exibir um template listando esses eventos
    return render(request=request, 
        context={"eventos": eventos}, 
        template_name="agenda/listar_eventos.html"
    )

def exibir_evento(request, id):
    evento = get_object_or_404(Evento, id=id)
    return render(
        request=request,
        context={"evento": evento},
        template_name="agenda/exibir_evento.html"
    )

def participar_evento(request):
    evento_id = request.POST.get("evento_id")
    evento = get_object_or_404(Evento, id=evento_id)
    evento.participantes += 1
    evento.save()
    
    return HttpResponseRedirect(reverse('exibir_evento', args=(evento_id,)))