import unittest

from datetime import date, datetime, timedelta

from tarefa import Tarefa
from lista_de_tarefas import ListaDeTarefas


class TestAdicionarTarefa(unittest.TestCase):
    def test_adiciona_tarefa_a_lista_de_tarefas(self):
        tarefa = Tarefa("Tarefa Teste")
        lista = ListaDeTarefas()

        lista.adicionar_tarefa(tarefa)

        # self.assertEqual(lista.get_tarefas()[0], tarefa)
        self.assertIn(tarefa, lista.get_tarefas())


class TestGetTarefas(unittest.TestCase):
    def test_retorna_lista_de_tarefas_adicionadas(self):
        tarefa_um = Tarefa("Tarefa Teste 1")
        tarefa_dois = Tarefa("Tarefa Teste 2")
        lista = ListaDeTarefas()

        lista.adicionar_tarefa(tarefa_um)
        lista.adicionar_tarefa(tarefa_dois)

        self.assertEqual(lista.get_tarefas(), [
            tarefa_um,
            tarefa_dois,
        ])

class TestGetTarefasAtrasadas(unittest.TestCase):
    def test_retorna_lista_de_tarefas_atrasadas(self):
        hoje = datetime.today()
        dt_original = hoje + timedelta(days=-5)
        tarefa = Tarefa("Estudar Python", data=dt_original)
        lista = ListaDeTarefas()

        lista.adicionar_tarefa(tarefa)

        self.assertEqual(lista.get_tarefas_atrasadas(),[tarefa])

class TestGetTarefasDeHoje(unittest.TestCase):
    def test_retorna_lista_de_tarefas_de_hoje(self):
        hoje = date.today()
        tarefa = Tarefa("Estudar Python", data=hoje)
        lista = ListaDeTarefas()

        lista.adicionar_tarefa(tarefa)

        self.assertEqual(lista.get_tarefas_para_hoje(), [tarefa])


unittest.main()