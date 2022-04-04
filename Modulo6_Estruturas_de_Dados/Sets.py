usuarios = {"alice", "bob"}
usuarios2 = set(["alice", "bob"])

print(usuarios)
print(usuarios2)
print(usuarios == usuarios2)
#  Ou seja, usando o comando 'set' eu transformo uma lista em set.
#  Um conjunto(set) não pode possuir elementos repetidos
usuarios.add("bob")
print(usuarios)  # Observe que não adicionou outro bob, só manteve o que tinha
usuarios.add("carlos")
print(usuarios)
#  Observe que os sets não possuem uma ordem dos elementos

#  Essa particularidade dos sets torna possível remover duplicatas
usuarios3 = ["sergio", "alice", "sergio"]
usuarios_unicos = set(usuarios3)  # Sergio apareceu somente uma vez
print(usuarios_unicos)

#  Como na matemática, os conjuntos tem operações, tais como união, intersecção
print(usuarios.union(usuarios_unicos))  # Uniu os dois sets
#  Posso utilizar o comando | (pipe) para realizar a união também
e_igual = usuarios.union(usuarios_unicos) == usuarios | usuarios_unicos
print(e_igual)


#  Ou intersecção
print(usuarios.intersection(usuarios_unicos))
e_intersec = usuarios.intersection(usuarios_unicos) == usuarios & usuarios_unicos
print(e_intersec)

#  Ou diferença
print(usuarios.difference(usuarios_unicos))
e_differenc = usuarios.difference(usuarios_unicos) == usuarios - usuarios_unicos
print(e_differenc)

#  Ainda tem outras operações, que podem ser vistas na documentação oficial
