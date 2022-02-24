""" comandos úteis:
    source venv/bin/activate,
    FLASK_APP=NomeDoArquivo.py FLASK_ENV=development flask run """

from flask import Flask, jsonify
from evento import Evento
from evento_online import EventoOnline
import json

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
#  O jsonify, por baixo dos panos utiliza o json.dumps, mas ele também
#  transforma a resposta em um json para o Cliente (navegador no caso) que
#  está consumindo nossa API. Portanto ele já altera o Content-Type Header para
#  application/json, por exemplo.


    