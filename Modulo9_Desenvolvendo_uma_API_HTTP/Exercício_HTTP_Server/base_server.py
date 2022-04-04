from http.server import HTTPServer, BaseHTTPRequestHandler
import hashlib


class Usuario:
    id = 1

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.id = Usuario.id
        Usuario.id += 1

    def imprime_informacoes(self):
        print(f"ID do usuário: {self.id}")
        print(f"Nome do usuário: {self.nome}")
        print(f"Email do usuário: {self.email}")
        print(f"Senha do usuário: {self.senha}")
        print("------------------------------------------")


def hash_string(texto):
    return hashlib.sha256(texto.encode()).hexdigest()


usuario1 = Usuario("Alice", "alice@codar.me", "123456789")
usuario2 = Usuario("Luíza", "luiza@codar.me", "987654321")
usuario3 = Usuario("Natalia", "natalia@exemplo.com", "as76daf7a6sd8as")
usuarios = [usuario1, usuario2, usuario3]


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

        elif self.path == "/usuarios/":
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

            usuarios_html = ""
            for usuario in usuarios:
                usuarios_html += f"""
                <tr>
                  <td>{usuario.id}</td>
                  <td>{usuario.nome}</td>
                  <td>{usuario.email}</td>
                  <td>{hash_string(usuario.senha)[:5]+"..."}</td>
                </tr>
                """
            data = f"""
            <html>
              <head>{stylesheet}</head>
              <h1>Usuários</h1>
              <table>
                <tr>
                  <th>Id</th>
                  <th>Nome</th>
                  <th>Email</th>
                  <th>Senha</th>
                </tr>
                {usuarios_html}
              </table>
            </html>
            """.encode()
            self.wfile.write(data)
            print("Implementar!")


server = HTTPServer(("localhost", 8000), SimpleHandler)
server.serve_forever()
