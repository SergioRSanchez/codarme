""" comandos úteis:
    source venv/bin/activate,
    FLASK_APP=NomeDoArquivo.py FLASK_ENV=development flask run """

from crypt import methods
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

#  "Pegar" evento
def get_evento_or_404(id):
    for ev in eventos:
        if ev.id == id:
            return ev
    abort(404, "Evento não encontrado.")

#  Lidar com erro 400
@app.errorhandler(400) 
def nao_encontrado(erro):
    return (jsonify(erro=str(erro)), 400)

#  Lidar com erro 404
@app.errorhandler(404) 
def nao_encontrado(erro):
    return (jsonify(erro=str(erro)), 404)

#  Detalhar evento
@app.route("/api/eventos/<int:id>/")
def detalhar_evento(id):  #  view detalhar
    ev = get_evento_or_404(id)
    return jsonify(ev.__dict__)

#  Deletar evento
@app.route("/api/eventos/<int:id>/", methods=["DELETE"])
def deletar_evento(id):  #  view deletar
    ev = get_evento_or_404(id)
    eventos.remove(ev)
    return jsonify(id=id)

#  Editar evento (usamos PUT quando for editar tudo do evento)
@app.route("/api/eventos/<int:id>/", methods=["PUT"])
def editar_evento(id):  #  view editar
    #  Parsing
    data = request.get_json()
    nome = data.get("nome")
    local = data.get("local")
    #  Validar evento
    if not nome:
        abort(400, "'nome' precisa ser informado!")
    if not local:
        abort(400, "'local' precisa ser informado!")
    
    ev = get_evento_or_404(id)
    ev.nome = nome
    ev.local = local

    return jsonify(ev.__dict__)

#  Editar evento (usamos PATCH quando for editar alguma parte do evento)
@app.route("/api/eventos/<int:id>/", methods=["PATCH"])
def editar_evento_parcial(id):  #  view editar
    #  Parsing
    data = request.get_json()
    ev = get_evento_or_404(id)
    if "nome" in data.keys():
        #  Pra editar o nome
        nome = data.get("nome")
        if not nome:
            abort(400, "'nome' precisa ser informado!")
        ev.nome = nome
    
    if "local" in data.keys():
        local = data.get("local")
        if not local:
            abort(400, "'local' precisa ser informado!")
        ev.local = local
    return jsonify(ev.__dict__)