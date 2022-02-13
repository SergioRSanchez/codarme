#  1 - "FizzBuzz" é um exercício clássico de programação. O programa recebe um
#  número inteiro e imprime:

#  a) "Fizz" caso seja múltiplo de 3
#  b) "Buzz" caso seja múltiplo de 5
#  c) "FizzBuzz" caso seja múltiplo de 3 e 5
import re
print("EXERCÍCIO 1 - FIZZBUZZ")

numero = input("Digite um número inteiro: ")
if numero.isdigit() == True:
    numero = int(numero)
    if numero % 5 == 0 and numero % 3 == 0:
        print(f"FizzBuzz, o número {numero} é divisível por 3 e 5. \n")
    elif numero % 5 == 0:
        print(f"Buzz, o número {numero} é divisível por 5. \n")
    elif numero % 3 == 0:
        print(f"Fizz, o número {numero} é divisível por 3. \n")
    else:
        print(f"O número {numero} não é divisível por 3 ou por 5.")
else:
    print("Não digitou um número \n")
print("")

#  2 - Implemente uma calculadora que receba 3 valores do usuário:

#  a) Operando "a" (Pode ser um inteiro ou float)
#  b) Operando "b" (Pode ser um inteiro ou float)
#  c) Operador "op" (sinal da operação desejada)

#  O seu programa deve receber esses 3 valores e imprimir o resultado da
#  operação. Caso o operador seja o de divisão, e o segundo operador seja zero
#  deve imprimir a mensagem "Não é possível realizar divisão por ZERO"
print("EXERCÍCIO 2 - CALCULADORA")


def is_float(val):
    if isinstance(val, float):
        return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val):
        return True

    return False


def is_int(val):
    if isinstance(val, int):
        return True
    if re.search(r'^\-{,1}[0-9]+$', val):
        return True

    return False


def is_number(val):
    return is_int(val) or is_float(val)


a = input("Digite o primeiro número: ")
b = input("Digite o segundo número: ")
op = input("Digite o operador: ")
if is_number(a) and is_number(b):
    a = float(a)
    b = float(b)
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        if b != 0:
            print(a / b)
        else:
            print("Não é possível realizar divisão por ZERO.")
    else:
        print("Operador inválido")
else:
    print("Você precisa digitar um número.")
print("")

#  3 - Escreve um programa de autenticação que receba um nome e senha, e
#  informe se:

#  a) A autenticação foi bem sucedida
#  b) Se o nome de usuário não existe
#  c) Se a senha está incorreta

#  Os valores corretos de nome de usuário e senha devem estar armazenados
#  em constantes, como no exemplo abaixo:
print("EXERCÍCIO 3 - LOGIN")

usuario = "ADMIN"
senha = "123123"

login = input("Insira o nome de usuario: ").upper()
password = input("Insira a senha: ")

if login == usuario:
    if password == senha:
        print("A autenticação foi bem sucedida.")
    else:
        print("A senha está incorreta")
else:
    print("Nome de usuário não existe.")
print("")

#  WHILE

#  1 - Escreve um programa que receba um número inteiro "n" e imprima a soma
#  de todos os números de 1 até "n" ("n" incluso)
print("EXERCÍCIO 1 - SOMA")

n = input("Digite um número: ")
if n.isdigit():
    n = int(n)
    i = 0
    soma = 0
    while i <= n:
        soma = i + soma
        i += 1
    print(soma)
else:
    print("Não digitou um número inteiro.")
print("")

#  2 - Escreve um programa que receba um número inteiro "n" e imprima todos os
#  números pares de 1 até "n" ("n" incluso)
print("EXERCÍCIO 2 - PARES")

p = input("Digite um número: ")
if p.isdigit():
    p = int(p)
    j = 0
    while j <= p:
        if j % 2 == 0:
            print(j)
        j += 1
else:
    print("Não digitou um número inteiro.")
print("")

#  3 - Um número primo é um número que é divisível apenas por 1 e por ele mesmo
#  Escreva um programa que receba um número "n" e informe se esse número é
#  primo ou não.
print("EXERCÍCIO 3 - PRIMOS")

primo = input("Digite um número para saber se ele é primo: ")
if primo.isdigit():
    primo = int(primo)
    if primo == 2 or primo == 3 or primo == 5 or primo == 7:
        print("O número é primo")
    else:
        if primo % 2 != 0 and primo % 3 != 0 and primo % 5 != 0 and primo % 7 != 0:
            print("O número é primo")
        else:
            print("O número não é primo")
else:
    print("Não digitou um número inteiro.")
print("")

#  4 - O jogo "Acerte o Número" funciona da seguinte maneira:

#  a) Existe um certo número inteiro declarado dentro do programa que o usuário
#  desconhece. Por exemplo: numero = 8
#  b) O usuário tem 3 tentativas para acertar o número.
#  c) A cada tentativa, é informado ao usuário se o número que ele digitou é
#  maior ou menor que o número correto.
#  d) O jogo termina quando o usuário erra 3 vezes (perdeu) ou quando o usuário
#  acerta o número (ganhou)

#  Implemente o jogo "Acerte o Número"
print("EXERCÍCIO 4 - ACERTE O NÚMERO")

secreto = input("Digite o número inteiro a ser adivinhado: ")
chances = 3
digitadas = []
while True:
    if chances <= 0:
        print("Perdeu")
        break
    chute = input("Digite um chute: ")
    if chute == secreto:
        print("Ganhou")
        break
    elif chute < secreto:
        chances -= 1
        print(f"Menor que o número correto, você ainda tem {chances} chances.")
    elif chute > secreto:
        chances -= 1
        print(f"Maior que o número correto, você ainda tem {chances} chances.")
