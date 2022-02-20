from evento import Evento
from evento_online import EventoOnline

ev_online = EventoOnline("Live de Python")
ev2_online = EventoOnline("Live de JavaScript")
""" ev_online.imprime_informacoes()
ev2_online.imprime_informacoes() """
print(ev_online.to_json())
print(ev2_online.to_json())

ev = Evento("Aula de Python", "Rio de Janeiro")
ev.imprime_informacoes()

print(type(ev_online.to_json()))
""" Observe que agora com a instrução json, os dados se tornaram do tipo string
Portanto conseguimos uma representação como se fosse um dicionário, mas que na
verdade é um texto, portanto conseguimos passar essa informação para outra
utilizando http, que é um protocolo textual. """
