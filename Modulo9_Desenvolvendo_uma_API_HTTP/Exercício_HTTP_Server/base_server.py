from http.server import HTTPServer, BaseHTTPRequestHandler
import hashlib
import json


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

    def to_json(self):
        return json.dumps({
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha
        })


def hash_string(texto):
    """
    Recebe um texto como string e retorna a representação hash desse texto.
    Exemplo:
        hash_string("123") -> "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07"
    """
    return hashlib.sha256(texto.encode()).hexdigest()


usuario1 = Usuario("Sergio", "sergio@exemplo.com", "1234567")
usuario2 = Usuario("Carol", "carol@exemplo.com", "7654321")
usuario3 = Usuario("Julia", "julia@exemplo.com", "283791731")
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
            # Enviar o status code da resposta: self.send_reponse(status_code)
            # Enviar cabeçalhos: self.send_header(nome, valor)
            # Finalizar cabeçalhos: self.end_headers()
            # Escrever dados para o "socket" (wfile): self.wfile.write(data)
            print("Implementar!")


server = HTTPServer(('localhost', 8000), SimpleHandler)
server.serve_forever()
