"""
1 - Escreva uma função que recebe um número inteiro positivo e retorna True
caso ele seja primo e False, caso contrário
Sugestão:
"""
print("Exercício 1\n")


def e_primo(n):
    n = int(n)
    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    elif n == 1:
        return False
    else:
        if n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
            return True
        else:
            return False


numero = input("Insira um número inteiro positivo: ")
if numero.isdigit():
    numero = int(numero)
    print(e_primo(numero))
else:
    print("Não digitou um número inteiro positivo")


"""
2 - Implemente uma função que receba uma lista de números inteiros e retorna
uma tupla (pos,num), onde pos é a posição (ou índice) do maior número na lista
e num é o valor desse número.
"""
print("\nExercício 2\n")


def tupla_maior():
    lista2 = []
    numero2 = input("insira o número: ")
    while True:
        if numero2.isdigit():
            lista2.append(numero2)
            numero2 = input("insira o número: ")
        else:
            break
    print(tuple((lista2.index(max(lista2)), max(lista2))))


tupla_maior()


"""
3 - Implemente uma função maior_idade(pessoa) que receba uma tupla
representando uma pessoa com nome e idade e imprime na tela se a pessoa é maior
de idade ou não.
"""
print("\nExercício 3\n")


def maior_de_idade(pessoa, idade):
    lista3 = tuple([pessoa, idade])
    print(lista3)
    if idade >= 18:
        print("Maior de idade.")
    else:
        print("Menor de idade.")


nome = input("Insira o nome: ")
idade = int(input("Insira a idade: "))
maior_de_idade(pessoa=nome, idade=idade)


"""
4 - Adapte a função maior_idade(pessoa) de forma que ela possa receber tanto
uma tupla quanto um dicionário. Dica: método type pode te ajudar.
"""
print("\nExercício 4\n")


def maior_de_idade2(pessoa2, idade2):
    lista4 = dict({"nome": pessoa2, "idade": idade2})
    print(lista4)
    if idade2 >= 18:
        print("Maior de idade.")
    else:
        print("Menor de idade.")


nome2 = input("Insira o nome: ")
idade2 = int(input("Insira a idade: "))
maior_de_idade2(pessoa2=nome2, idade2=idade2)


"""
5 - Implemente uma função que recebe dois argumentos, uma lista e um elemento,
e retorna True caso o elemento seja encontrado nessa lista, e False caso
contrário. Não é permitido usar o método "in".
"""
print("\nExercício 5\n")


def procura():
    lista5 = []
    numeros_lista = input("Insira os números da lista: ")
    while True:
        if numeros_lista.isdigit():
            lista5.append(numeros_lista)
            numeros_lista = input("Insira os números da lista: ")
        else:
            break
    elemento = input("Digite o número a ser procurado: ")
    lista5 = set(lista5)
    elemento = set(elemento)
    print(elemento == lista5 & elemento)


procura()


"""
6 - Uma função fatorial calcula o valor da multiplicação de um certo número
inteiro não-negativo por todos os números positivos menores que ele. A exceção
é o fatorial de zero que é igual a "1". Por exemplo:

fatorial(3) = 3 * 2 * 1 = 6
fatorial(1) = 1
fatorial(0) = 1

Ou seja, podemos definir a função fatorial como:

fatorial(n) = n * n-1 * n-2 * ... * 1

Implemente a função fatorial(n) de modo que ela retorne o valor do fatorial de
n.
"""
print("\nExercício 6\n")


def fatorial(num):
    return 1 if (num == 1 or n == 0) else num * fatorial(num - 1)


n = int(input("Fatorial de: "))
print(f"O fatorial de {n} é", fatorial(n))
