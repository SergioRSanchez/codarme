#  Operadores lógicos são:

#  not: negação

idade = 18
maior_idade = idade >= 18
menor_idade = not maior_idade

print("Idade da pessoa", idade)
print("Maior de idade?", maior_idade)
print("Menor de idade?", menor_idade)

#  and: conjunção

usuario_correto = True
senha_correta = False
sucesso = usuario_correto and senha_correta

print("Login bem sucedido:", sucesso)

#  or: disjunção
acompanhada_pais = False
cinema = maior_idade or acompanhada_pais
print("Pode acessar o cinema:", cinema)
