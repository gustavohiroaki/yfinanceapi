from flask import Flask,jsonify
from flask_cors import CORS
from get_ticker import get_ticker

__version__ = "1.0.0"

app = Flask(__name__)
CORS(app)

@app.route('/ticker/<string:ticker>')
def home(ticker):
    data = get_ticker(ticker + ".SA")
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)