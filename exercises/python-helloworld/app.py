from flask import Flask, request
import logging


logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s : %(message)s')
app = Flask(__name__)


@app.route("/")
def hello():
    logging.debug("%s endpoint was reached", request.endpoint)
    return "Hello World!"


@app.route("/status")
def status():
    logging.debug("%s endpoint was reached", request.endpoint)
    return {'result': 'OK - healthy'}


@app.route("/metrics")
def metrics():
    logging.debug("%s endpoint was reached", request.endpoint)
    return {'data': {'UserCount': 140, 'UserCountActive': 23}}


if __name__ == "__main__":
    app.run(host='0.0.0.0')
