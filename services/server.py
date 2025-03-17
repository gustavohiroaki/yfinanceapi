import os
import yfinance as yf
import redis
from dotenv import load_dotenv
from flask import Flask,jsonify
from flask_cors import CORS
from .cache import Cache
from .get_ticker import get_ticker

load_dotenv()

app = Flask(__name__)
redis = redis.Redis(host=os.environ.get("REDIS_HOST"), port=os.environ.get("REDIS_PORT"))
cache = Cache(redis)
CORS(app)

@app.route('/ticker/<string:ticker>')
def home(ticker):
    data = get_ticker(yf, cache, ticker)
    return jsonify(data)


def create_app():
    return app