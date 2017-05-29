from flask import Flask

app = Flask(__name__)
events_path = './OngWebProject/sources/events.json'
itens_path = './OngWebProject/sources/itens.json'

f = open(events_path, 'r')
events = []
events = f.read()
f.close()
f = open(itens_path, 'r')
itens = []
itens = f.read()
f.close()

import OngWebProject.routes
