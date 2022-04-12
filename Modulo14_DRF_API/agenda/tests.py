from datetime import datetime, timezone
import email
from urllib import response
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
import json
from agenda.models import Agendamento

# Create your tests here.


class TestListagemAgendamento(APITestCase):
    def test_listagem_vazia(self):
        response = self.client.get("/api/agendamentos/?username=usuario1")
        data = json.loads(
            response.content
        )  #  json.loads(response.content) -> Converte o conteúdo da resposta em um dicionário
        self.assertEqual(data, [])
        # self.assertDictEqual(data[0], agendamento_serializado)

    def test_listagem_com_um_agendamento(self):
        Agendamento.objects.create(
            data_horario="2019-01-01T00:00:00Z",
            nome_cliente="João",
            email_cliente="joao@email.com",
            telefone_cliente="(11) 99999-9999",
        )
        response = self.client.get("/api/agendamentos/")
        data = json.loads(response.content)
        agendamento_serializado = {
            "id": 1,
            "data_horario": "2019-01-01T00:00:00Z",
            "nome_cliente": "João",
            "email_cliente": "joao@email.com",
            "telefone_cliente": "(11) 99999-9999",
        }
        self.assertEqual(data, [agendamento_serializado])


class TestCriacaoAgendamento(APITestCase):
    def test_cria_agendamento(self):
        usuario = User.objects.create_user(
            email="ssanchezfilho@gmail.com", username="usuario1", password="1234"
        )
        agendamento_request_data = {
            "data_horario": "2023-01-01T14:00:00Z",
            "nome_cliente": "João",
            "email_cliente": "joao@email.com",
            "telefone_cliente": "(11)99999-9999",
            "prestador": "usuario1",
        }
        response = self.client.post(
            "/api/agendamentos/?=username=usuario1",
            agendamento_request_data,
            format="json",
        )
        agendamento_criado = Agendamento.objects.get()
        self.assertEqual(
            agendamento_criado.data_horario,
            datetime(2023, 1, 1, 14, 0, 0, tzinfo=timezone.utc),
        )
        self.assertEqual(response.status_code, 201)

    def test_quando_request_e_invalido_retorna_400(self):
        ...

    def test_cria_agendamento_e_pega_id(self):
        Agendamento.objects.create(
            data_horario="2019-01-01T00:00:00Z",
            nome_cliente="João",
            email_cliente="joao@email.com",
            telefone_cliente="(11) 99999-9999",
            prestador="usuario1",
        )
        response = self.client.get("/api/agendamentos/1/")
        data = json.loads(response.content)
        agendamento_serializado = {
            "data_horario": "2019-01-01T00:00:00Z",
            "nome_cliente": "João",
            "email_cliente": "joao@email.com",
            "telefone_cliente": "(11)99999-9999",
            "prestador": "usuario1",
        }
        agendamento_criado = Agendamento.objects.get()
        self.assertEqual(agendamento_criado.nome_cliente, "João")
        self.assertEqual(response.status_code, 200)


class TestGetHorarios(APITestCase):
    def test_quando_data_e_feriado_retorna_lista_vazia(self):
        response = self.client.get("/api/horarios/?data=2022-12-25")
        self.assertEqual(response.data, [])

    def test_quando_data_e_dia_comum_retorna_lista_com_horarios(self):
        response = self.client.get("/api/horarios/?data=2022-10-03")
        self.assertNotEqual(response.data, [])
        self.assertEqual(
            response.data[0], datetime(2022, 10, 3, 9, tzinfo=timezone.utc)
        )
        self.assertEqual(
            response.data[-1], datetime(2022, 10, 3, 17, 30, tzinfo=timezone.utc)
        )
