import requests, sys, time, cProfile, pstats, os
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

    # time.sleep(5)
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

    raise Exception('Uncorrect field of table')

def with_sleep():
    cProfile.run('parser_yahoo()', filename='profilingResults.cprof')
    with open("profiling-sleep.txt", "w") as f:
        ps = pstats.Stats("profilingResults.cprof", stream=f)
        ps.sort_stats('tottime')
        ps.print_stats()
        os.remove('profilingResults.cprof')

def without_sleep():
    cProfile.run('parser_yahoo()', filename='profilingResults.cprof')
    with open("profiling-tottime.txt", "w") as f:
        ps = pstats.Stats("profilingResults.cprof", stream=f)
        ps.sort_stats('tottime')
        ps.print_stats()
        os.remove('profilingResults.cprof')

if __name__ == '__main__':
    with_sleep()