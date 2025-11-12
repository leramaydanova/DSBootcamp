import sys

def stocks():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
        }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
        }
    

    words = [s.strip() for s in sys.argv[1].lower().split(",")]

    if not words or len(sys.argv) != 2 or words.count(''):
        return
    
       
    LOWER_STOCKS = {v.lower() : (k, v) for k, v in COMPANIES.items()}
    LOWER_COMPANIES = {k.lower() : (k, v) for k, v in COMPANIES.items()}

    for s in words:
        if s in LOWER_COMPANIES:
            company, ticker = LOWER_COMPANIES[s]
            price = STOCKS[ticker]
            print(f"{company} stock price is {price}")
        elif (LOWER_STOCKS.get(s)):
            company, ticker = LOWER_STOCKS[s]
            print(f"{ticker} is a ticker symbol for {company}")
        else:
            print(f"{s} is an unknown company or an unknown ticker symbol")
    

if __name__ == '__main__':
    stocks()