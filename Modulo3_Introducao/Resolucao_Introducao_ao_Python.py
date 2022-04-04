# Exercício 1:
string = "Essa é uma string"
inteiro = 10
decimal = 10.5
booleano = 20 == 20

print(type(string))
print(type(inteiro))
print(type(decimal))
print(type(booleano))

#  Exercício 2:
valor_compras = 100.10
desconto = 0.1
quantidade_itens = 10
final = float(valor_compras - (valor_compras * desconto)) * quantidade_itens

print(f"O valor final da compra, considerando o desconto é {final:.2f} reais")
print(f"O custo médio de cada item é de {final/10:.2f} reais")
