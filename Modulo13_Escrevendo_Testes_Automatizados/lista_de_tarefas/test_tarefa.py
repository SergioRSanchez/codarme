import unittest
from tarefa import Tarefa
from datetime import datetime, timedelta


class TestConcluir(unittest.TestCase):

    def test_concluir_tarefa_altera_concluida_para_true(self):
        tarefa =  Tarefa("Estudar Python")
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)
    
    def test_concluir_tarefa_concluida_mantem_concluida_como_true(self):
        tarefa =  Tarefa("Estudar Python")
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)
    

class TestDescricao(unittest.TestCase):

    def test_adicionar_descricao(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.adicionar_descricao("asdas")
        self.assertEqual(tarefa.descricao, "asdas")
    
    def test_adicionar_nova_descricao(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.adicionar_descricao("Primeira Descrição")
        self.assertEqual(tarefa.descricao, "Primeira Descrição")
        tarefa.adicionar_descricao("Segunda Descrição")
        self.assertEqual(tarefa.descricao, "Segunda Descrição")

class TestAdiarNotificacao(unittest.TestCase):

    def test_adia_notificacao_em_N_minutos(self):
        dt_original = datetime(2022, 2, 10, 9, 10)
        tarefa = Tarefa("Estudar Python", data_notificacao=dt_original)
        tarefa.adiar_notificacao(15)
        dt_esperado = datetime(2022, 2, 10, 9, 25)
        self.assertEqual(tarefa.data_notificacao, dt_esperado)

class TestAtrasada(unittest.TestCase):
    def test_tarefa_esta_atrasada(self):
        hoje = datetime.today()
        dt_original = hoje + timedelta(days=-5)
        tarefa = Tarefa("Estudar Python", data=dt_original)
        tarefa.atrasada()
        self.assertEqual(tarefa.atrasada(), "Atrasada")
    
    def test_tarefa_esta_dentro_do_prazo(self):
        hoje = datetime.today()
        dt_original = hoje + timedelta(days=5)
        tarefa = Tarefa("Estudar Python", data=dt_original)
        tarefa.atrasada()
        self.assertEqual(tarefa.atrasada(), "Dentro do prazo")





if __name__ == '__main__':
    unittest.main()