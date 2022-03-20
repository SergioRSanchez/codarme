import unittest

from calculadora_de_notas import Turma, Aluno


class TestAdicionaAluno(unittest.TestCase):

    def test_adiciona_aluno_na_lista_da_turma(self):
        aluno = Aluno("Sergio", 10)
        lista = Turma()

        lista.adiciona_aluno_na_lista_da_turma(aluno)

        self.assertIn(aluno, lista.get_aluno_turma())
    

class TestAluno(unittest.TestCase):
    def test_adiciona_aluno(self):
        aluno = Aluno("nome", "nota")
        aluno.adiciona_aluno(nome="Sergio", nota=10)
        self.assertEqual(aluno.nome, "Sergio")
        self.assertEqual(aluno.nota, 10)
    
class TestGetAluno(unittest.TestCase):

    def test_get_aluno_da_turma(self):
        aluno1 = Aluno("Sergio", 9)
        aluno2 = Aluno("Carol", 10)
        lista = Turma()

        lista.adiciona_aluno_na_lista_da_turma(aluno1)
        lista.adiciona_aluno_na_lista_da_turma(aluno2)

        self.assertEqual(lista.get_aluno_turma(), [
            aluno1,
            aluno2,
        ])
    

class TestGetMedia(unittest.TestCase):
    
    def test_get_media(self):
        aluno1 = Aluno("Sergio", 9)
        aluno2 = Aluno("Carol", 10)
        lista = Turma()

        lista.adiciona_aluno_na_lista_da_turma(aluno1)
        lista.adiciona_aluno_na_lista_da_turma(aluno2)

        lista.get_media()
        self.assertEqual(lista.get_media(), 8)



if __name__ == '__main__':
    unittest.main()