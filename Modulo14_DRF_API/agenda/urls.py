from django.urls import path
from agenda.views import AgendamentoDetail, AgendamentoList, PrestadorList, get_horarios

urlpatterns = [
    path("agendamentos/", AgendamentoList.as_view()),
    path("agendamentos/<int:pk>/", AgendamentoDetail.as_view()),
    path("horarios/", get_horarios),  # Não sei se está certo
    path("prestadores/", PrestadorList.as_view()),
]
