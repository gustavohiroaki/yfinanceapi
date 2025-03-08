import yfinance as yf

def get_ticker(yf, ticker):
    data = yf.Ticker(ticker)
    return data.info

if __name__ == '__main__':
    import sys
    ticker = sys.argv[1]
    test = get_ticker(yf, ticker + '.SA')
    print(test)