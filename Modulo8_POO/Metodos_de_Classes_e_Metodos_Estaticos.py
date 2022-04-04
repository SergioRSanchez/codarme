# Quando falamos de Métodos (Funções) em uma Classe em Python, existem 3 tipos:


class Event:
    def metodo_instancia(self):
        return ("método de instância chamado", self)

    #  chamado a partir do nosso objeto, e self é a referência pro objeto

    @classmethod
    def metodo_classe(cls):
        return ("método de classe chamado", cls)

    #  chamado a partir de uma classe

    @staticmethod
    def metodo_estatico():
        return "estático chamado"


#  está dentro do corpo da nossa classe, porém ele não tem referência nem a
#  nossa classe nem a alguma instância dessa classe, é um método independente
#  não recebe nenhum argumento


#  Método Instância
ev = Event()
a = ev.metodo_instancia()  # Event.metodo_instancia(ev)
print(a)

#  Método Classe
b = Event.metodo_classe()  # Event.metodo_classe(Event)
print(b)
#  Método classe sendo retornado a partir de nosso objeto
#  Por ser @classmethod ele sabe que a referencia é classe e não o objeto
c = ev.metodo_classe()
print(c)

#  Método Estático
d = Event.metodo_estatico()  # Event.metodo_estatico()
print(d)
#  Método Estático sendo retornado a partir de nosso objeto
#  Por ser @staticmethod ele sabe que a referencia é static e não o objeto
e = Event.metodo_estatico()
print(e)

""" Resumindo, por padrão os métodos que forem definidos dentro de uma classe,
serão definidos como método instância, e precisam receber o self, ou seja,
esperam ser chamados a partir de um objeto; se colocar o @classmethod é um
método a ser chamado a partir de uma classe e precisar receber o cls; e se for
chamar o método a partir da classe ou do objeto, mas ele não depende e não tem
que receber referência da classe ou da nossa instância, então @staticmethod """
