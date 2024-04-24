from flask import Flask, jsonify, request
import json
from Kyberz import Kyber
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.debug = True

crypto = Kyber()

@app.route("/")
def hello_world():
    return "Hello Garvit !"

@app.get("/api/create_key")
def create_key():
    return crypto.create_keys()

@app.get("/api/encrypt")
def encrypt():
    keys = crypto.create_keys()
    message = request.args.get('message')
    ciphertext = crypto.encrypt(message, keys['public_key'])
    return {"private_key": json.dumps(keys['private_key']),"public_key": json.dumps(keys['public_key']),"cipher_text":json.dumps(ciphertext)}


if __name__ == "__main__":

    app.run()
