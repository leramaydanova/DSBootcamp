import sys

def search_ticker():
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

    if len(sys.argv) == 2:
        print_res(STOCKS, COMPANIES)


def print_res(stocks, companies):
    LOWER_STOCKS = {k.lower() : v for k, v in stocks.items()}

    ticker = sys.argv[1].lower()
    if ticker in LOWER_STOCKS:
        for name, v in companies.items():
            if v.lower() == ticker:
                print(name + ' ' + str(LOWER_STOCKS.get(ticker)))
                break
    else:
        print("Unknown ticker")
            


if __name__ == '__main__':
    search_ticker()
