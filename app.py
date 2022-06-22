from flask import Flask, request

from mbi import MBI

app = Flask(__name__)


@app.route('/')
def heartbeat():
    return "OK"


@app.route('/generate', methods=['GET'])
def generate():
    return {"mbi": MBI.generate()}


@app.route('/verify', methods=['POST'])
def verify():
    status, errors = MBI(request.form['mbi']).validate()
    if status is False:
        print(", ".join(errors))  # just printing to term, but should log
    return {"is_valid": str(status)}


if __name__ == '__main__':
    app.run()
