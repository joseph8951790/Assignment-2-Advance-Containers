from flask import Flask, request, jsonify
import bcrypt, jwt

app = Flask(__name__)
SECRET_KEY = "supersecretkey"

@app.route('/register', methods=['POST'])
def register():
    return jsonify({"message": "User registered"})

@app.route('/login', methods=['POST'])
def login():
    return jsonify({"token": "fake-jwt-token"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)