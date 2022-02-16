#  1 - Escreva um programa que receba inteiro do usuário e imprima True caso o
#  número seja par e False caso seja ímpar.
from curses.ascii import isdigit

numero = input("Escreva um número inteiro: ")
if numero.isdigit() == True:
    numero = int(numero)
    divisivel = numero % 2 == 0

    if divisivel == True:
        print(divisivel)
    else:
        print(divisivel)
else:
    print("Não digitou um número")
print("")

#  2 - O que vai ser impresso na tela ao executar o código abaixo?

a = 5
b = 10
x = True
y = False

print((x or y) and (a < b))
print((x or y) and not (a < b))
print("")
#  3 - Considere o programa abaixo

#  resultado = 2 + 3 * 2 ** 2
#  print(resultado)

#  É possível conseguir resultados diferentes, sem alterar os números e
#  operadores, apenas com a utilização de parênteses, por exemplo

resultado = (2 + 3) * 2 ** 2
print(resultado)
#  = 20

#  Utilize parênteses de modo que o código imprima os seguintes resultados:

#  14
resultado = 2 + 3 * 2 ** 2
print(resultado)

#  38
resultado = 2 + (3 * 2) ** 2
print(resultado)

#  100
resultado = ((2 + 3) * 2) ** 2
print(resultado)
print("")
#  4 - Alice é responsável por escrever um programa que verifica se um cupom de
#  desconto pode ser utilizado. O programa recebe 3 valores e retorna True caso
#  o cupom possa ser utilizado, ou False, caso contrário.

#  Os três valores que o programa recebe são: 1) Valor da compra(float);
#  2) Valor do frete(float) e 3) Cliente é cadastrado no programa de fidelidade
# (string "S" (sim) ou "N" (não))

#  O cupom tem a seguinte regra:

#  Caso o valor da compra somado ao frete seja superior a R$ 100, ou o cliente
#  seja cadastrado no programa de fidelidade, o cupom de desconto pode ser
#  utilizado. Caso o contrário, o cupom não pode ser utilizado.

#  Objetivo é implementar o código para tal tarefa.

compra = input("Insira o valor da compra: ")
frete = input("Insira o valor do frete: ")
if compra.isdigit() and frete.isdigit() == True:
    compra = float(compra)
    frete = float(frete)
    fidelidade = input(
        "O cliente é cadastrado no programa de fidelidade? [S] ou [N]: ").upper()

    if compra + frete >= 100 or fidelidade == "S":
        print("Cupom Liberado")
    else:
        print("Cupom não liberado")
else:
    print("Não digitou um número")
