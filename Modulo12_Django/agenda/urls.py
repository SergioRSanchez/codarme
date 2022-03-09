from django.urls import path
from agenda.views import exibir_evento
from agenda.views import index

urlpatterns = [
    path("", index),
    path("evento", exibir_evento),
]