from datetime import datetime, timezone, time
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
import json
from agenda.models import Agendamento
from unittest import mock

# Create your tests here.


class AgendamentoAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.seuze = User.objects.create_user(
            email="seuze@email.com", username="seuze", password="sergio123"
        )
        self.client.login(username="seuze", password="sergio123")

        return super().setUp()


class TestListagemAgendamentos(APITestCase):
    def test_listagem_vazia(self):
        response = self.client.get("/api/agendamentos/?username=seuze")
        data = json.loads(
            response.content
        )  #  json.loads(response.content) -> Converte o conteúdo da resposta em um dicionário
        self.assertEqual(data, [])
        assert data == []
        # self.assertDictEqual(data[0], agendamento_serializado)

    def test_listagem_de_agendamentos_criados(self):
        Agendamento.objects.create(
            data_horario=datetime(2023, 3, 15, 9, tzinfo=timezone.utc),
            nome_cliente="João",
            email_cliente="joao@email.com",
            telefone_cliente="(11) 99999-9999",
            prestador="seuze",
        )
        response = self.client.get("/api/agendamentos/?username=seuze")
        data = json.loads(response.content)
        agendamento_serializado = {
            "id": 1,
            "data_horario": "2023-03-15T09:00:00Z",
            "nome_cliente": "João",
            "email_cliente": "joao@email.com",
            "telefone_cliente": "(11) 99999-9999",
            "prestador": "seuze",
            "horario_cancelado": False,
        }
        self.assertEqual(data, [agendamento_serializado])
        assert data[0] == agendamento_serializado


class TestCriacaoAgendamento(APITestCase):
    def test_cria_agendamento(self):
        agendamento_request_data = {
            "data_horario": "2023-03-15T09:00:00Z",
            "nome_cliente": "João",
            "email_cliente": "joao@email.com",
            "telefone_cliente": "(11)99999-9999",
            "prestador": "seuze",
        }
        response = self.client.post("/api/agendamentos/", agendamento_request_data)

        assert response.status_code == 201

        agendamento_criado = Agendamento.objects.get()
        self.assertEqual(
            agendamento_criado.data_horario,
            datetime(2023, 3, 15, 9, tzinfo=timezone.utc),
        )
        assert agendamento_criado.prestador == self.seuze

    def test_quando_agendamento_e_no_passado_retorna_400(self):
        agendamento_request_data = {
            "data_horario": "2023-03-15T09:00:00Z",
            "nome_cliente": "João",
            "email_cliente": "joao@email.com",
            "telefone_cliente": "(11)99999-9999",
            "prestador": "seuze",
        }
        response = self.client.post("/api/agendamentos/", agendamento_request_data)
        assert response.status_code == 400

    def test_cancela_agendamento(self):
        agendamento_request_data = {
            "data_horario": "2023-03-15T09:00:00Z",
            "nome_cliente": "João",
            "email_cliente": "joao@email.com",
            "telefone_cliente": "(11)99999-9999",
            "prestador": "seuze",
        }
        response = self.client.post("/api/agendamentos/", agendamento_request_data)
        assert response.status_code == 201

        agendamento_criado = Agendamento.objects.get()
        assert agendamento_criado.horario_cancelado == False

        response = self.client.delete(
            f"/api/agendamentos/{agendamento_criado.pk}/", agendamento_request_data
        )
        assert response.status_code == 204

        agendamento_criado.refresh_from_db()
        assert agendamento_criado.horario_cancelado == True


class TestGetHorarios(APITestCase):
    @mock.patch(
        "agenda.libs.brasil_api.is_feriado", return_value=True
    )  # o Mock "engana" o sistema, então ele vai retornar o valor que a gente tá passando, no caso "True"
    def test_quando_data_e_feriado_retorna_lista_vazia(self, is_feriado_mock):
        response = self.client.get("/api/horarios/?data=2022-12-25")
        self.assertEqual(response.data, [])
        assert response.status_code == 200

    @mock.patch("agenda.libs.brasil_api.is_feriado", return_value=False)
    def test_quando_data_e_dia_comum_retorna_lista_com_horarios(self, _):
        response = self.client.get("/api/horarios/?data=2022-10-03")
        self.assertNotEqual(response.data, [])
        self.assertEqual(
            response.data[0], datetime(2022, 10, 3, 9, tzinfo=timezone.utc)
        )
        self.assertEqual(
            response.data[-1], datetime(2022, 10, 3, 17, 30, tzinfo=timezone.utc)
        )
        assert response.status_code == 200
