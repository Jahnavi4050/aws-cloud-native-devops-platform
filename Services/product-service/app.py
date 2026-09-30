from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 60000
    },
    {
        "id": 2,
        "name": "Mobile",
        "price": 30000
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 2000
    }
]


@app.route("/")
def home():
    return "Product Service is running"


@app.route("/products")
def get_products():
    return jsonify(products)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)