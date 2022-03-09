from django.urls import path
from agenda.views import exibir_evento, listar_eventos, participar_evento

urlpatterns = [
    path("eventos/", listar_eventos, name="listar_eventos"),
    path("eventos/<int:id>/", exibir_evento, name="exibir_evento"),
    path("participar/", participar_evento, name="participar_evento"),
]