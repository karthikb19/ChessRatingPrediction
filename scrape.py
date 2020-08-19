from bs4 import BeautifulSoup
import urllib.request
import requests
import pandas as pd
from requests_html import HTMLSession

BASE_URL = 'http://www.uschess.org/msa/'
PLAYER_URL = 'http://www.uschess.org/msa/MbrDtlTnmtHst.php?15397813'
ID = PLAYER_URL[45:53]
MAX_PAGE = 4
def get_data(page):
    url = PLAYER_URL + '.' + str(page)
    with urllib.request.urlopen(url) as response:
        html = response.read()
    # print(html)
    scrape = BeautifulSoup(html, "html.parser")
    # print(scrape)
    # print(scrape.findAll('tr', bgcolor=['FFFF80', 'FFFFC0']))[1:]
    return scrape.findAll('tr', bgcolor=['FFFF80', 'FFFFC0'])[1:]


def getting_tournament_data(tournament):
    for word in tournament.find('td', width='120'):
        print(word)

    date = [word for word in tournament.find('td', width='120').stripped_strings][0]
    ratings = [text for text in tournament.find('td', width='160').stripped_strings]
    before = ''
    after = ''
    if(len(ratings) == 2):
        before = ratings[0][:-3]
        after = ratings[1]
    DATE_RATING = {
        'date' : date,
        'brating': before,
        'arating' : after
    }
    print(DATE_RATING)
    return DATE_RATING


def main():
    TOURNAMENTS = []
    for page in range(1, MAX_PAGE):
        page_data = get_data(page)
        for tourney in page_data:
            TOURNAMENTS.append(getting_tournament_data(tourney))
    

    data = open(ID+'.csv', 'w')
    for t in range(0, len(TOURNAMENTS)):
        data.write(TOURNAMENTS[t]['date'] + ',' + TOURNAMENTS[t]['arating'] + '\n')


if __name__ == "__main__":
    main()