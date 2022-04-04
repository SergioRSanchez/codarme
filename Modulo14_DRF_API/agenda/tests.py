from datetime import datetime, timezone
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
        agendamento_serializado = {
            "id": 1,
            "data_horario": "2019-01-01T00:00:00Z",
            "nome_cliente": "João",
            "email_cliente": "joao@email.com",
            "telefone_cliente": "(11) 99999-9999"
            }
        self.assertEqual(data, [agendamento_serializado])
    

class TestCriacaoAgendamento(APITestCase):
    def test_cria_agendamento(self):
        agendamento_request_data = {
            "data_horario": "2023-01-01T14:00:00Z",
            "nome_cliente": "João",
            "email_cliente": "joao@email.com",
            "telefone_cliente": "(11)99999-9999"
        }
        response = self.client.post("/api/agendamentos/", agendamento_request_data, format="json")

        agendamento_criado = Agendamento.objects.get()
        
        self.assertEqual(agendamento_criado.data_horario, datetime(2023, 1, 1, 14, 0, 0, tzinfo=timezone.utc))
        self.assertEqual(response.status_code, 201)

    
    def test_quando_request_e_invalido_retorna_400(self):
        ...


    def test_cria_agendamento_e_pega_id(self):
        agendamento_request_data = {
            "data_horario": "2023-02-01T14:00:00Z",
            "nome_cliente": "João",
            "email_cliente": "joao@email.com",
            "telefone_cliente": "(11)99999-9999"
        }
        response = self.client.post("/api/agendamentos/", agendamento_request_data, format="json")
        agendamento_criado = Agendamento.objects.get()
        self.assertEqual(agendamento_criado.id, 1)