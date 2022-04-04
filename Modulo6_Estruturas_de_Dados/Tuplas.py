x = 5, 10  # Geralmente a tupla vem entre parenteses, mas não é obrigatório
#  Porém a boa prática pede que seja posta entre parenteses
print(x[0])
print(x[1])
print(type(x))

print("####################################")

#  Utilizamos listas como no exemplo das notas
#  Utilizamos tuplas como no exemplos das pessoas, em que há elementos lá dentr

#  Note que é possível mudar um valor dentro de uma lista, são mutáveis
notas = [8, 10]
print(notas)
notas[0] = 9
print(notas)

#  Em uma tupla já não é possível, pois elas são imutáveis, se eu executar
#  esse código abaixo vai dar erro
# nota = (8, 10)
# print(nota)
# nota[0] = 9
# print(nota)
#  Não é possível alterar, adicionar ou remover elementos

#  Em tuplas a gente usa o conceito de desempacotar
pessoa = ("Gabriel", 27, True)
nome, idade, admin = pessoa
print(idade)

#  Também posso desempacotar uma lista
#  Porém a lista é utilizada de uma outra maneira, ela é utilizada para uma
#  iteração, ou seja, utilizo todos os seus elementos para achar uma média
#  de notas por exemplo, em que todos dados são do mesmo "tipo"
#  Enquanto a tupla eu utilizo para guardar um elemento com dados diferentes
#  entre sim, por exemplo: nome, idade, sexo
pessoas = ["Gabriel", 27, True]
nomes, idades, admins = pessoas
print(idades)

#  Para fazer um exemplo completo, posso ter uma lista com tuplas dentro, por
#  exemplo, uma lista de pessoas

convidados = (["Sergio", 31, True], ["Carol", 30, True])
sergio, carol = convidados
print(sergio)
