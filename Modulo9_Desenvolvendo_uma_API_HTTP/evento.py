""" Quando a gente procura por um atributo em um objeto, primeiro ele procura
no objeto pra saber se tem um atributo, caso ele não tenha ele olha se a classe
daquele objeto tem um atributo.
Herança faz com que uma classe herde todos os atributos e comportamentos de
outra classe, e sobrescreva alguns deles."""

import json


class Evento:
    id = 1

    def __init__(self, nome, local=""):
        self.nome = nome
        self.local = local
        self.id = Evento.id  # self.id é um atributo de instância
        Evento.id += 1  # Evento.id é um atributo de classe

    def imprime_informacoes(self):  # Método de Instância
        print(f"ID do evento: {self.id}")
        print(f"Nome do evento: {self.nome}")
        print(f"Local do evento: {self.local}")
        print("----------------------------------------------------")

    def to_json(self):
        return json.dumps({"id": self.id, "local": self.local, "nome": self.nome})

    @staticmethod
    def calcula_limite_pessoas_area(area):
        if 5 <= area < 10:
            return 5
        elif 10 <= area < 20:
            return 15
        elif area >= 20:
            return 30
        else:
            return 0


"""     @classmethod
    def cria_evento_online(cls, nome):
        evento = cls(nome, local=f"https://tamarcado.com/eventos?id={cls.id}")
        return evento

Foi substituído pela especialização"""


""" ev = Evento("Aula de Python")
ev2 = Evento("Aula de JavaScript", "Rio de Janeiro")

ev.imprime_informacoes()
ev2.imprime_informacoes()
print(Evento.calcula_limite_pessoas_area(6))"""
