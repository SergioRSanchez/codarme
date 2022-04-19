import json
import requests
from datetime import date
from django.conf import settings
import logging


def is_feriado(date: date):
    logging.info(f"Fazendo requisição para BrasilAPI para a data: {date.isoformat()}")
    if (
        settings.TESTING == True
    ):  # Ele verifica se está rolando um teste, se for o caso, ele retorna False
        #  Se for Natal ou Ano Novo, retornamo True sempre (para testes)
        logging.info("Requisição não está sendo feita pois TESTING = True")
        if (date.day == 25 and date.month == 12) or (date.day == 1 and date.month == 1):
            return True
        return False

    ano = date.year
    r = requests.get(f"https://brasilapi.com.br/api/feriados/v1/{ano}")
    if not r.status_code == 200:
        # Para não impedir que usuários possam fazer o agendamento, assumo que esta data não é um feriado em caso de erro, e faço um log do que aconteceu
        logging.error(f"Brasil API retornou status_code: {r.status_code}")
        return False

    feriados = json.loads(r.text)
    for feriado in feriados:
        # datetime.strptime("2020-01-30", "%Y-%m-%d")
        data_as_str = feriado["date"]
        data = date.fromisoformat(data_as_str)  # Formato "2020-01-30"
        if data == date:
            return True

    return False
