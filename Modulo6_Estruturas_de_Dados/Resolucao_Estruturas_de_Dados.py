import statistics
from typing import Counter

"""
1 - Escreva um programa que lê números inteiros positivos do usuário, um após
o outro, e monta uma lista a partir desses números e depois imprime a lista
montada. O programa deve continuar solicitando por números até que o elemento
digitado seja um número negativo (que não deve ser inserido)
"""
print("Exercício 1:\n")

numero1 = input("Digite um número inteiro positivo: ")
lista1 = []
while numero1.isnumeric():
    numero = int(numero1)
    lista1.append(numero1)
    numero1 = input("Digite um número inteiro positivo: ")
else:
    print(lista1)

print("\n################################################\n")

"""
2 - Dada uma lista de números inteiros, escreva um programa que calcula a soma
de todos os números da lista.
"""
print("Exercício 2:\n")

lista2 = [1, 10, 20, 35, 22, 12]  # Resultado deve ser 100
print(sum(lista2))

print("\n################################################\n")

"""
3 - Dada uma lista de números inteiros, escreva um programa que calcula a
média dos números da lista. O resultado não deve incluir números decimais.
Exemplo: 12.3 deve imprimir somente 12  (pode usar // (divisão inteira))
"""
print("Exercício 3:\n")

lista3 = [1, 10, 20, 35, 22, 12]  # Resultado deve ser 16
media = statistics.mean(lista3) // 1
print(media)

print("\n################################################\n")

"""
4 - Suponha o seguinte programa:
Alunos e suas respectivas notas
"""
print("Exercício 4:\n")

alunos = [
    ("Alice", 8),
    ("Bob", 7),
    ("Carlos", 9),
]

#  Escreva um programa que calcula a média das notas de todos os alunos.

soma = []
for aluno, nota in alunos:
    soma.append(nota)
print(statistics.mean(soma))

print("\n################################################\n")

"""
5 - Suponha o seguinte programa:
Alunos e suas notas representadas através de dicionários
"""
print("Exercício 5:\n")

alunos2 = [
    {
        "nome": "Alice",
        "nota": 8,
    },
    {
        "nome": "Bob",
        "nota": 7,
    },
    {
        "nome": "Carlos",
        "nota": 9,
    },
]

#  Escreva um programa que calcula a média das notas de todos os alunos.

soma2 = []
for elemento in alunos2:
    soma2.append(elemento["nota"])
print(statistics.mean(soma2))

print("\n################################################\n")

"""
6 - Escreva um programa que dado uma lista de números inteiros, imprime o maior
número dessa lista
"""
print("Exercício 6:\n")

lista6 = [1, 3, 2, 5]  # Deve imprimir 5
print(max(lista6))

print("\n################################################\n")

"""
7 - Uma string também pode ser percorrida utilizando for


for x in "abc":
    print(x)


Vai imprimir:
#  a
#  b
#  c
Escreva um programa que solicite uma string para o usuário e imprima quantas
vezes cada letra aparece na palavra:

banana
O resultado deve ser:

{
    "a": 3,
    "b": 1,
    "n": 2
}
"""
print("Exercício 7:\n")

palavra = input("Digite uma string: ")
c = Counter(palavra)
print(c)

print("\n################################################\n")

"""
8 - Escreva um programa que declara uma lista com elementos de diferentes
tipos e imprime na tela essa lista invertida. Não é permitido utilizar
métodos como reverse ou sort

lista8 = ["a", 5, {1}]
lista_invertida = inverte_lista(lista8)
print(lista_invertida)  #  [{1}, 5. "a"]
"""
print("Exercício 8:\n")

lista8 = ["a", 5, {1}]
lista_invertida = lista8[::-1]
print(lista_invertida)
