#  usando o for e o in
#  Listas, Tuplas, Sets e Dicionários são considerados iteráveis, portanto
#  podemos utilizar 'for' e 'in' nelas

notas = (8, 9, 10)  # Tuplas
notas2 = [8, 9, 10]  # Listas
notas3 = {8, 9, 10}  # Sets

for nota in notas:
    print(nota)

for nota in notas2:
    print(nota)

for nota in notas3:
    print(nota)

#  Quando a gente iterá sobre um dicionário, a gente está iterando sobre as
#  chaves desse dicionário

notas4 = {
    "alice": 10,
    "bob": 9,
    "carlos": 8,
}

for nota in notas4:
    print(nota)
    print(notas4[nota])


#  Temos 3 métodos úteis em dicionários:
#  dict.keys()  Retorna um iterável com as chaves
#  dict.value()  Retorna um iterável com os valores
#  dict.items()  Retorna um iterável com os elementos completos

for nota2 in notas4.items():
    print(nota2)

for k, v in notas4.items():
    print(k, v)
