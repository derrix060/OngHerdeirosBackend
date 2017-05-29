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


@app.route('/2')
def hello_world2():
    return 'Hello, World! - v2'


@app.route('/3')
def hello_world3():
    return 'Hello, World! - v3'

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
