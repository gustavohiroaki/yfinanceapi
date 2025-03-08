import yfinance as yf
from flask import Flask,jsonify
from flask_cors import CORS
from .get_ticker import get_ticker

app = Flask(__name__)
CORS(app)

@app.route('/ticker/<string:ticker>')
def home(ticker):
    data = get_ticker(yf, ticker + ".SA")
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)