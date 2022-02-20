from evento import Evento


class EventoOnline(Evento):  # EventoOnline é uma especialização de Evento
    def __init__(self, nome, _=""):  # o _ é pra quando o argumento é ignorado
        local = f"https://tamarcado.com/eventos?id={EventoOnline.id}"
        # Tem que chamar o construtor da classe Pai:
        super().__init__(nome, local)  # super() referencia classe Pai

    def imprime_informacoes(self):  # Método de Instância
        print(f"ID do evento: {self.id}")
        print(f"Nome do evento: {self.nome}")
        print(f"Link para acessar o evento: {self.local}")
        print("--------------------------------------------------------------")
