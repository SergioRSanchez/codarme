
class Evento:  # funciona como criar um tipo (string, int, float, etc)
    def altera_nome_evento(self, novo_nome):
        print("Alterando nome do evento")
        self.nome = novo_nome


ev = Evento()  # Vai criar um novo objeto na memória, do tipo Evento
ev.nome = "Aula de Python"
print(ev.nome)

#  Objetos que instaciamos através de classes, são mutáveis
#  Objetos criados de uma classe, são chamados de instâncias da classe

#  para chamar a função (método) altera nome, tem que colocar o ev na frente,
#  assim como era em dicionários
#  Da maneira abaixo daria erro, pois quando a gente chama um método a partir
#  de um objeto, o primeiro ARGUMENTO já é preenchido pelo objeto
""" ev.altera_nome_evento(ev, "Aula de JavaScript")
print(ev.nome) """

#  Portanto pra funcionar teria que ser:
ev.altera_nome_evento("Aula de JavaScript")  # obj.método
print(ev.nome)
#  Observe que na definição da função, o primeiro parâmetro é chamado de SELF

""" Resumindo, quando faço objeto.método o que o Python faz é chamar a classe,
no caso é Evento.método, que foi definido dentro da classe, porém como esse
método foi chamado através de um objeto, o interpretador Python vai passar o
próprio objeto como referência como o primeiro argumento daquela função.

obj.metodo(1, 2, 3) => Evento.metodo(obj, 1, 2, 3) """
