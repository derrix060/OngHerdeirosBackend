from flask import Flask

app = Flask(__name__)

events_path = './sources/events.json'
itens_path = '.source/itens.json'

f = open(events_path, 'r')
events = []
events = f.read()
f.close()
f = open(itens_path, 'r')
itens = []
itens = f.read()
f.close()
