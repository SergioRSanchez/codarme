from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from evento import Evento
from evento_online import EventoOnline


ev_online = EventoOnline("Live de Python")
ev2_online = EventoOnline("Live de JavaScript")
ev = Evento("Aula de Python", "Rio de Janeiro")
eventos = [ev_online, ev2_online, ev]


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf8")
            self.end_headers()
            data = f"""
            <html>
                <head>
                    <title>Olá, Mundo!</title>
                </head>
                <body>
                    <p>Testando nosso servidor HTTP!</p>
                    <p>Diretório: {self.path}</p>
                </body>
            </html>
            """.encode()
            self.wfile.write(data)
        elif self.path == "/eventos":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf8")
            self.end_headers()

            stylesheet = """
            <style>
                table {
                    border-collapse: collapse;
                }

                td, th {
                    border: 1px solid #dddddd;
                    text-align: left;
                    padding: 8px;
                }
            </style>
            """
            eventos_html = ""
            for ev in eventos:
                eventos_html += f"""
                <tr>
                    <td>{ev.id}</td>
                    <td>{ev.nome}</td>
                    <td>{ev.local}</td>
                </tr>
                """
            data = f"""
            <html>
                <head>{stylesheet}</head>
                <table>
                    <tr>
                        <th>Id</th>
                        <th>Nome</th>
                        <th>Local</th>
                    </tr>
                    {eventos_html}
                </table>
            </html>
            """.encode()
            self.wfile.write(data)
        elif self.path == "/api/eventos":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf8")
            self.end_headers()
            lista_dict_eventos = []
            for ev in eventos:
                lista_dict_eventos.append(
                    {
                        "id": ev.id,
                        "nome": ev.nome,
                        "local": ev.local,
                    }
                )

            # só consegue seriarizar(transformar em json) arquivos que forem dicionário
            data = json.dumps(lista_dict_eventos).encode()
            self.wfile.write(data)


server = HTTPServer(("localhost", 8000), SimpleHandler)
server.serve_forever()
