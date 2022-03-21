"""
CALCULADORA DE NOTAS
====================
1. Recebe uma turma, composta por uma lista de Alunos(nome, nota) e média para aprovar um aluno.
2. Calcula a média das notas da turma (get_media).
3. Qual a maior e menor nota (get_maior_nota, get_menor_nota).
4. Retorna alunos aprovados e reprovados (get_aprovados, get_reprovados).
5. Retorna lista de notas em representação de "letra".
    - nota == 10       =>    "A+"
    - 9 <= nota < 10   =>    "A"
    - 7 <= nota < 9    =>    "B"
    - 5 <= nota < 7    =>    "C"
    - 3 <= nota < 5    =>    "D"
    - 1 <= nota < 3    =>    "E"
    - 0 <= nota < 1    =>    "F
"""

import statistics


class Turma:
    
    def __init__(self):
        self.lista_turma = []
    
    
    def adiciona_aluno_na_lista_da_turma(self, aluno):
        self.lista_turma.append(aluno)
    

    def get_aluno_turma(self):
        lista_turma_de_alunos = []
        for aluno in self.lista_turma:
            lista_turma_de_alunos.append(aluno)
        return lista_turma_de_alunos
    
    
    def get_media(self):
        soma_das_notas = []
        for nome, nota in self.lista_turma:
            soma_das_notas.append(nota)
            media = statistics.mean(soma_das_notas)
            return media




class Aluno:
    
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    
    def adiciona_aluno(self, nome, nota):
        self.nome = nome
        self.nota = nota