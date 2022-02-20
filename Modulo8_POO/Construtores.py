#  Forçar um objeto criado a ter um conjunto de atributos

class Event():
    def __init__(self, nome):
        self.nome = nome
        self.local = "Brasil"
#  Agora tu não consegue criar um objeto sem passar o atributo nome pra ele
#  E todos os objetos terão o atributo local como Brasil


ev = Event("Aula de Python")
ev2 = Event("Aula de JS")

print(ev.nome)
print(ev.local)
print(ev2.nome)
print(ev2.local)
