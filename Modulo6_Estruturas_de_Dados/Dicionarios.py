#  A estrutura de um dicionário é:
#  {key: value}
#  Onde a key é única e o value pode conter mais de uma informação

#  Em um dicionário, diferentemente das listas e tuplas que só podiam ser
#  acessadas pelo índice do elemento, eu posso acessar qualquer elemento
#  através das chaves (keys), que podem ser uma string por exemplo.

notas = {
    "alice": 10,
    "bob": 8,
    "carlos": 9
}
print(notas["alice"])
#  print(notas["abc"])  # Vai dar um KeyError, pois a chave não existe

#  lista = [1, 2, 3]
#  print(lista[10])  #  Em lista vai dar um IndexError, pois usa índices

janeiro = {
    1: "sábado",
    2: "domingo"
}
print(janeiro[1])

#  No dicionário podemos usar chaves arbitrárias para indicar cada valor,
#  exemplo, fica muito mais fácil acessar o nome, não precisar lembrar em que
#  posição está o item nome
alice = {
    "nome": "Alice",
    "idade": 27,
    "admin": False
}
bob = {
    "idade": 30,
    "admin": True,
    "nome": "Bob"
}
print(alice["nome"])
print(bob["nome"])
#  Repare como ficou mais fácil acessar o nome do elemento que eu queria,
#  independente de qual posição ele estava

#  Podemos adicionar listas e tuplas dentro do dicionário

sergio = {
    "nome": "Sergio",
    "endereço": {
        "rua": "25 de Março",
        "número": "1234"
    }
}
print(sergio["nome"])
print(sergio["endereço"])
print(sergio["endereço"]["rua"])  # Temos um dicionário dentro do dicionário
