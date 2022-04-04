from rest_framework.test import APITestCase
import json
from agenda.models import Agendamento


# Create your tests here.

class TestListagemAgendamento(APITestCase):
    def test_listagem_vazia(self):
        response = self.client.get("/api/agendamentos/")
        data = json.loads(response.content) #  json.loads(response.content) -> Converte o conteúdo da resposta em um dicionário
        self.assertEqual(data, [])

    def test_listagem_com_um_agendamento(self):
        Agendamento.objects.create(data_horario="2019-01-01T00:00:00Z", nome_cliente="João", email_cliente="joao@email.com", telefone_cliente="(11) 99999-9999")
        response = self.client.get("/api/agendamentos/")
        data = json.loads(response.content)
        serializer = {
            "id": 1,
            "data_horario": "2019-01-01T00:00:00Z",
            "nome_cliente": "João",
            "email_cliente": "joao@email.com",
            "telefone_cliente": "(11) 99999-9999"
            }
        self.assertEqual(data, [serializer])

        