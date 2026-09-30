from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

cart = [
    {
        "product_id": 1,
        "quantity": 2
    },
    {
        "product_id": 2,
        "quantity": 1
    }
]


@app.route("/")
def home():
    return "Cart Service is running"


@app.route("/cart")
def get_cart():
    return jsonify(cart)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)