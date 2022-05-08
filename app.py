import requests as requests
from flask import Flask
from flask_cors import CORS
import json

JOKES_API_URL = 'https://v2.jokeapi.dev/joke/Any?safe-mode'
app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = False


@app.route('/jokes', methods=['GET'])
def jokes():
    response = requests.get(JOKES_API_URL)
    jokeData = json.loads(response.content)
    return jokeData


if __name__ == '__main__':
    app.run()
