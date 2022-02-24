""" comandos úteis:
    source venv/bin/activate,
    FLASK_APP=NomeDoArquivo.py FLASK_ENV=development flask run """

from flask import Flask, jsonify, abort, make_response, request, json
from evento import Evento
from evento_online import EventoOnline


app = Flask(__name__)

ev_online = EventoOnline("Live de Python")
ev_online2 = EventoOnline("Live de JavaScript")
ev = Evento("Aula de Python", "Rio de Janeiro")
eventos = [ev_online, ev_online2, ev]

@app.route("/")
def index():
    return "<h1>Flask configurado com sucesso!</h1>"

@app.route("/api/eventos/")
def listar_eventos():
    eventos_dict = []
    for ev in eventos:
        eventos_dict.append(ev.__dict__)
    return jsonify(eventos_dict)

""" O jsonify, por baixo dos panos utiliza o json.dumps, mas ele também
transforma a resposta em um json para o Cliente (navegador no caso) que
está consumindo nossa API. Portanto ele já altera o Content-Type Header para
application/json, por exemplo. """

@app.route("/api/eventos/", methods=["POST"])
def criar_evento():
    #  Parsing
    data = json.loads(request.data)
    nome = data.get("nome")
    local = data.get("local")
    #  Validar evento
    if not nome:
        abort(400, "'nome' precisa ser informado!")
    #  Criando evento
    if local:
        evento = Evento(nome=nome, local=local)
    else:
        evento = EventoOnline(nome=nome)

    eventos.append(evento)
    
    #return data
    return {
        "id": evento.id,
        "url": f"/api/eventos/{evento.id}/"
    }
"""
request representa a requisição, data é o conjunto de dados. json.loads 
contrário do dumps (que pega um dicionário e retorna um json), portanto ele
recebe um objeto json e retorna um dicionário.
O Flask por padrão, quando recebe uma resposta em sua view como dicionário ele
transforma esse dicionário automaticamente em json.
Regras de Negócios, no caso é validar para que nosso evento tenha nome, caso
não tenha não vai rolar.
O processo que fizemos a cima se chama Parsing, que consiste em pegar uma
informação que está vindo em um certo e formato, lendo ela e transformando em
outra.
"""

@app.errorhandler(400) 
def nao_encontrado(erro):
    return (jsonify(erro=str(erro)), 400)

@app.errorhandler(404) 
def nao_encontrado(erro):
    return (jsonify(erro=str(erro)), 404)

@app.route("/api/eventos/<int:id>/")
def detalhar_evento(id):
    for ev in eventos:
        if ev.id == id:
            return jsonify(ev.__dict__)
    abort(404, "Evento não encontrado.")
    #data = {"erro": f"Não encontrei evento com id: {id}"}
    #return make_response(jsonify(data), 404)  Assim ele retorna um json