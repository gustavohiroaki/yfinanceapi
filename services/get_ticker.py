import yfinance as yf
import redis

def get_ticker(yf, cache, ticker):
    cached = cache.get( ticker)
    if cached:
        return cached
    data = yf.Ticker(ticker)
    if data.info:
        cache.set(ticker, data.info)
    return data.info

if __name__ == '__main__':
    import sys
    ticker = sys.argv[1]
    test = get_ticker(yf, ticker + '.SA')
    print(test)