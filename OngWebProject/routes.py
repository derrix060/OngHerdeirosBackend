from flask import jsonify
from OngWebProject import app, events, events_path, itens, itens_path
from app.model.events import Event


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/herdeiros/eventos/all')
def get_all_events():
    return jsonify(events)


@app.route('/api/herdeiros/itens/all')
def get_all_itens():
    return jsonify(itens)


@app.route('/api/herdeiros/eventos/add/<name>/<date>')
def add_event(name, date):
    event = Event(name, date)
    events.append(event)
    f = open(events_path, 'w+')
    f.write(events)
    f.close()
    return 'Event added!'
