from flask import Flask, jsonify

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

@app.route('/')
def hello_world():
    return 'Hello, World! - v1'

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


@app.route('/2')
def hello_world2():
    return '/2'


@app.route('/3')
def hello_world3():
    return '/3'


if __name__ == '__main__':
    app.run(threaded=True)
    app.config.update(
        DEBUG=True,
        PROPAGATE_EXCEPTIONS=True)
