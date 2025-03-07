import yfinance as yf

def get_ticker(ticker):
    data = yf.Ticker(ticker)
    return data.info

if __name__ == '__main__':
    import sys
    ticker = sys.argv[1]
    test = get_ticker(ticker + '.SA')
    print(test)