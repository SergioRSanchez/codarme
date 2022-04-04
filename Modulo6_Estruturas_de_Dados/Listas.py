notas = [8, 10, 8.5]
#        0   1    2
print(notas[2])  # Acessa o índice da lista

notas.append(9)  # Adiciona este objeto no final da lista, ou seja, no índice 3
print(notas)

#  A lista ela fica ordenada da maneira que foram inseridos os elementos, se
#  quiser que ela fique ordenada, tem que usar o método sort
#  Não foi passado nenhum parâmetro para o sort, então ele ordena do crescente
notas.sort()
print(notas)
notas.sort(reverse=True)  # Decrescente
print(notas)

#  Podemos remover o último elemento da lista, usando o método pop
#  Pode remover de qualquer posição da lista, só colocar o índice
notas.pop()
print(notas)

#  Para inserir um elemento na lista, sem ser no final, usamos o método insert
notas.insert(0, 9.5)
print(notas)

print("####################################")

pessoa = ["Gabriel", 27, "123456"]
print(f"O nome é {pessoa[0]}")
print(f"A idade é {pessoa[1]}")
print(f"A senha é {pessoa[2]}")

print("####################################")

pessoas = [["Gabriel", 27], ["Bruno", 30]]
print(f"O nome é {pessoas[1][0]}")
print(f"A idade é {pessoas[1][1]}")

print("####################################")

nota = [8, 9, 10, 7.5, 4, 6]
qtd = len(nota)
i = 0
total = 0.0
while i < qtd:
    total = total + nota[i]
    i += 1
print("O total das notas é: ", total)
media = total / qtd
print("A média das notas é: ", media)
