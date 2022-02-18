""" Objetos mutáveis são aqueles que podem ser alterados depois de criados na
memória do computador. Exemplo de um objeto mutável são as listas.
Exemplo lista1 = [1, 2, 3] vai criar um objeto na memória com endereço 0 por
exemplo e valor 1, 2 e 3, e vai criar um símbolo chamado lista1. """


lista1 = [1, 2, 3]
print(lista1)
print(id(lista1))
lista1.append(4)
print(lista1)
print(id(lista1))
#  Observe que mesmo inserindo o 4 na lista, o endereço da lista continuou o
#  mesmo.
lista2 = lista1
lista2.append(5)
print(lista2)
print(lista1)
print(id(lista1))
print(id(lista2))

""" Observe que adicionando o 5 na lista2, ele foi adicionado também na lista1.
Isso acontece pq o símbolo lista2, por ser igual a lista1, estava apontando
para o objeto com o endereço da lista1, e quando modificamos a lista2, o objeto
todo foi modificado, o que chamamos de EFEITO COLATERAL, em todos os símbolos
que apontavam para aquele objeto. Agora observe que se criarmos uma terceira
lista, com os mesmos valores da lista1, o endereço dela será diferente, pois
como listas são mutáveis, o Python entende que mesmo tendo o mesmo valor, o
objeto que essa nova lista aponta deve ser novo. """

print(lista1)
lista3 = [1, 2, 3, 4, 5]
print(lista3)
print(id(lista1))
print(id(lista3))
print(lista1 == lista3)
print(id(lista1) == id(lista3))
#  Mesmo as listas sendo iguais, o endereço delas é diferente.

print("#########################################")

#  Vamos a outro exemplo:

notas_originais = [8, 10, 7]
notas_ordenadas = notas_originais
notas_ordenadas.sort()
print("Notas ordenadas: ", notas_ordenadas, id(notas_ordenadas))
print("Notas originais: ", notas_originais, id(notas_originais))

""" Observe que as notas originais também foram ordenadas. Isso acontece pq o
método .sort() é um método inplace, ou seja, ele altera o objeto, portanto,
como tinhamos mais de um símbolo apontando para o mesmo objeto, ambos foram
ordenados. Para alterar somente uma lista, sem ter esse impacto, devemos
utilizar o método sorted(notas_ordenadas). """

notas_originais2 = [8, 10, 7]
notas_ordenadas2 = sorted(notas_originais2)
print("Notas ordenadas: ", notas_ordenadas2, id(notas_ordenadas2))
print("Notas originais: ", notas_originais2, id(notas_originais2))

""" Observe que apesar de ter "copiado" a lista original, ela é um objeto com
um endereço completamente diferente. 
Vejamos um perigo que essa mutabilidade pode causar. Vamos supor que temos uma
funçao:
def faz_alguma_coisa(lista):
    ...     Realiza varias coisas aqui
    lista.append(6)     Algum momento adiciona 6
    ...     Faz mais coisas 

aí eu tenho uma lista1 = [1, 2, 3]
e tenho um x = faz_alguma_coisa(lista1)
aquele PARÂMETRO lá em cima (lista) vai assumir o ARGUMENTO de baixo (lista1),
ou seja, vai apontar para o mesmo objeto, e como ele é mutável, esse objeto vai
ser alterado, mesmo a gente não querendo. Isso é o que chamos de Função com
Efeito Colateral. Isso demonstra a diferença de mutabilidade das listas e das
Tuplas. Veja a seguir"""

tupla = (1, 2, 3)
tupla1 = (1, 2, 3)
print(id(tupla) == id(tupla1))

""" Diferente das listas, o endereço de tuplas diferentes contendo os mesmos
números é o mesmo, pois as Tuplas são imutáveis, portanto aquele objeto na
memória não pode ser alterado. Ele simplesmente adiciona um novo símbolo
apontando para o mesmo objeto.
Então resumidamente, existem objetos que são mutáveis, como listas, sets e
dicinários. E objetos que são imutáveis, como as tuplas, ints, floats, strings.
"""
