import sys

def search_price():
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

    LOWER_COMPANIES = {k.lower() : v for k, v in COMPANIES.items()}

    if len(sys.argv) == 2:
        stock = LOWER_COMPANIES.get(sys.argv[1].lower())
        if stock in STOCKS:
            print(STOCKS.get(stock))
        else:
            print("Unknown company")
            

if __name__ == '__main__':
    search_price()
