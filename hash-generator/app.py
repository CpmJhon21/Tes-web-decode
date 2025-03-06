from flask import Flask, render_template, request, jsonify
import hashlib
import base64
import hmac
import secrets
from urllib.parse import quote, unquote

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Base64 Encode/Decode
@app.route('/base64_encode', methods=['POST'])
def base64_encode():
    data = request.json.get("data", "")
    return jsonify({"result": base64.b64encode(data.encode()).decode()})

@app.route('/base64_decode', methods=['POST'])
def base64_decode():
    data = request.json.get("data", "")
    return jsonify({"result": base64.b64decode(data.encode()).decode()})

# Hash Generator
@app.route('/hash/<algo>', methods=['POST'])
def hash_generator(algo):
    data = request.json.get("data", "")
    if algo not in ["md5", "sha1", "sha256", "sha512"]:
        return jsonify({"error": "Invalid algorithm"}), 400
    hash_obj = hashlib.new(algo, data.encode()).hexdigest()
    return jsonify({"result": hash_obj})

# URL Encode/Decode
@app.route('/url_encode', methods=['POST'])
def url_encode():
    data = request.json.get("data", "")
    return jsonify({"result": quote(data)})

@app.route('/url_decode', methods=['POST'])
def url_decode():
    data = request.json.get("data", "")
    return jsonify({"result": unquote(data)})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
