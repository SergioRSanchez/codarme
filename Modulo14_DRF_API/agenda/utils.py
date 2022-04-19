import csv
from typing import Iterable
from datetime import date, datetime, timedelta, timezone, tzinfo, time

from agenda.libs import brasil_api

from agenda.models import Agendamento


def get_horarios_disponiveis(data: date) -> Iterable[datetime]:
    """
    Retorna uma lista com objetos do tipo datetime cujas datas são o mesmo dia passado (data)
    e os horários são os horários disponíveis para aquele dia, conforme outros agendamentos existam.
    """
    # Chamar a API Brasil com o ano da data
    # Verificar se os feriados retornados possuem a data igual a data solicitada pelo nosso usuário
    # Caso afirmativo, retorna uma lista vazia

    if brasil_api.is_feriado(data) or data.weekday() == 6:
        return []

    start = datetime(
        year=data.year,
        month=data.month,
        day=data.day,
        hour=9,
        minute=0,
        tzinfo=timezone.utc,
    )
    if (
        data.weekday() == 5
    ):  #  Teria que ser data.weekday, porém está travando devido ele estar tentando validar no data_horario do serializers
        end = datetime(
            year=data.year,
            month=data.month,
            day=data.day,
            hour=13,
            minute=0,
            tzinfo=timezone.utc,
        )
    else:
        end = datetime(
            year=data.year,
            month=data.month,
            day=data.day,
            hour=18,
            minute=0,
            tzinfo=timezone.utc,
        )
    delta = timedelta(minutes=30)
    horarios_disponiveis = set()
    while start <= end:
        if not Agendamento.objects.filter(data_horario=start).exists():
            horarios_disponiveis.add(start)
        start = (
            start + delta
        )  # Vai mostrar os horários que não estão inclusos na Agenda, ou seja, não foram 'pegos', mais o delta de meia em meia hora
    return horarios_disponiveis


def gera_relatorio_prestadores(output, prestadores_data):
    writer = csv.writer(output)
    writer.writerow(
        [
            "prestador",
            "data_horario",
            "nome_cliente",
            "email_cliente",
            "telefone_cliente",
            "horario_cancelado",
        ]
    )
    for prestador in prestadores_data:
        for agendamento in prestador["agendamentos"]:
            writer.writerow(
                [
                    agendamento["prestador"],
                    agendamento["data_horario"],
                    agendamento["nome_cliente"],
                    agendamento["email_cliente"],
                    agendamento["telefone_cliente"],
                    agendamento["horario_cancelado"],
                ]
            )
