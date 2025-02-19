from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/order', methods=['POST'])
def create_order():
    return jsonify({"message": "Order created"}), 201

@app.route('/order/<int:id>', methods=['GET'])
def get_order(id):
    return jsonify({"id": id, "status": "processed"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)