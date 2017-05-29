from flask import jsonify
from main import app, events, events_path, itens, itens_path
from OngWebProject.model.events import Event


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/1')
def hello_1():
    return 'Hello, 1'

@app.route('/api/herdeiros/eventos/all')
def get_all_events():
    return events


@app.route('/api/herdeiros/itens/all')
def get_all_itens():
    return jsonify(itens)


@app.route('/create_events')
def create_events():
    eventos = []
    evento = {}
    evento['name'] = 'teste name'
    evento['date'] = "2017-06-05 17:00:00"
    eventos.append(evento)
    eventos.append(evento)
    eventos.append(evento)
    rtn = jsonify(eventos)
    f = open(events_path, 'w+')
    f.write(rtn)
    f.close()
    return rtn


@app.route('/api/herdeiros/eventos/add/<name>/<date>')
def add_event(name, date):
    event = Event(name, date)
    events.append(event)
    f = open(events_path, 'w+')
    f.write(events)
    f.close()
    return 'Event added!'
