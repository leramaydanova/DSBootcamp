import requests, sys, pytest
from bs4 import BeautifulSoup

def parser_yahoo():
    url = f"https://finance.yahoo.com/quote/{sys.argv[1]}/financials/"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }

    page = requests.get(url, headers=headers, allow_redirects=False)

    if page.status_code != 200:
        raise Exception('Uncorrect URL')

    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find(class_='tableBody')
    rows = table.find_all(class_='row')
    for row in rows:
        columns = row.find_all(class_='column')
        title = columns[0].find(class_='rowTitle')
        if title.get_text() == sys.argv[2]:
            numbers = map(lambda x: x.get_text().strip(), columns[1:])
            return (sys.argv[2], *numbers)

class TestClass:

    @pytest.mark.parametrize("ticker, metric, expected", [
        ("MSFT", "Total Revenue", "Total Revenue"),
        ("AAPL", "Operating Income", "Operating Income"),
        ("GOOGL", "Gross Profit", "Gross Profit"),
    ])

    def test_metric(self, monkeypatch, ticker, metric, expected):
        test_args = ["py", ticker, metric]
        monkeypatch.setattr(sys, "argv", test_args)
        print(sys.argv[2])
        res = parser_yahoo()
        assert res[0] == expected

    def test_return_type(self, monkeypatch):
        test_args = ["py", "MSFT", "Total Revenue"]
        monkeypatch.setattr(sys, "argv", test_args)
        res = parser_yahoo()
        assert isinstance(res, tuple)

    def test_raise_by_ticker(self, monkeypatch):
        test_args = ["py", "MSF", "Total Revenue"]
        monkeypatch.setattr(sys, "argv", test_args)

        with pytest.raises(Exception, match = "Uncorrect URL"):
            res = parser_yahoo()