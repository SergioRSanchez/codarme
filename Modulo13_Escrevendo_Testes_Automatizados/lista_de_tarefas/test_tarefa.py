import unittest
from tarefa import Tarefa


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
        tarefa = Tarefa("Teste")
        tarefa.adicionar_descricao("Primeiro Teste")
        self.assertEqual(tarefa.descricao, "Primeiro Teste")
    
    def test_trocar_de_descricao(self):
        tarefa = Tarefa("Teste")
        tarefa.adicionar_descricao("Primeiro Teste")
        tarefa = Tarefa("Teste")
        tarefa.adicionar_descricao("Segundo Teste")
        self.assertEqual(tarefa.descricao, "Segundo Teste")



if __name__ == '__main__':
    unittest.main()