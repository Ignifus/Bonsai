from flask import Flask
from flask import abort
from bonsai_client import init

app = Flask(__name__)

@app.route("/")
def hello():
    logging.info('|| INFO - {"method": "index", "timestamp":' + str(time.time()) + ', "description": "/hello"}')
    return "<h1>Aplicacion A</h1>"

@app.route("/goodbye")
def goodbye():
    logging.info('|| INFO - {"method": "goodbye", "timestamp":' + str(time.time()) + ', "description": "/goodbye"}')
    return "<h1>Chau! applicacion A</h1>"

@app.route("/securearea")
def securearea():
    logging.info('|| INFO - {"method": "secure-area", "timestamp":' + str(time.time()) + ', "description": "/securearea"}')
    abort(403)    

@app.route("/content")
def content():
    logging.info('|| INFO - {"method": "content", "timestamp":' + str(time.time()) + ', "description": "/content"}')
    return "<h1>Contenido de la applicacion A</h1>"

@app.errorhandler(404)
def not_found(error):
    logging.error('|| HTTP - {"code": "404", "timestamp":' + str(time.time()) + '}')
    return '<h1>Pagina no encontrada (A)</h1>'

@app.errorhandler(403)
def forbidden(e):
    logging.error('|| HTTP - {"code": "403", "timestamp":' + str(time.time()) + '}')
    return "<h1>Forbidden Area (A)</h1>"

if __name__ == "__main__":
    import logging
    import time
    logging.basicConfig(filename='logs_a.log',level=logging.INFO)

    init("TestAppA", "sarasacosmica", "logs_a.log")

    app.run(host='127.0.0.1', port=3001)