from webbrowser import get
from flask import Flask, jsonify, request
from utils import get_bitcoin_price

app = Flask(__name__)


@app.get('/greet')
def index():
    """
    TODO: 
    1. Capture first name & last name 
    2. If either is not provided: respond with an error 
    3. If first name is not provided and second name is provided: respond with "Hello Mr. <second-name>!" 
    4. If first name is provided but second name is not provided: respond with "Hello, <first-name>!" 
    5. If both names are provided: respond with a question, "Is your name <fist-name> <second-name> 
    """

    return jsonify({"Message": "Hello World"})


@app.get('/bitcoin')
def bitcoin():
    bitcoin_price = get_bitcoin_price()
    return jsonify({'bitcoin_usd_price': bitcoin_price})


if __name__ == "__main__":
    app.run(debug=True)
