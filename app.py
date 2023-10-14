from flask import Flask, request, Response
from flask_cors import CORS

from utils import ask_chatgpt, speak

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)


@app.route('/audio/', methods=['POST'])
def convers():
    print('Request: /audio/', request.json)
    id = request.json['id']
    msg = request.json['msg']

    speech = speak.speak(msg)
    response = Response(speech)
    response.headers['Content-Type'] = 'audio/mp3'
    response.headers['Content-Length'] = str(len(speech))

    return response


@app.route('/msg/', methods=['POST'])
def convers2():
    id = request.json['id']
    req = request.json['msg']
    msg = ask_chatgpt.ask(id, req)
    lts = {'msg': msg}

    return lts


if __name__ == "__main__":
    app.run(debug=False, host='127.0.0.1', port=5050)
