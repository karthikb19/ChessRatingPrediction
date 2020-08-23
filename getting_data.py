from bs4 import BeautifulSoup
import urllib.request
import requests
import pandas as pd
from requests_html import HTMLSession
import math
import os
import sys 

def get_data(PLAYER_URL, page):
    url = PLAYER_URL + '.' + str(page)
    with urllib.request.urlopen(url) as response:
        html = response.read()
    scrape = BeautifulSoup(html, "html.parser")
    return scrape.findAll('tr', bgcolor=['FFFF80', 'FFFFC0'])[1:]


def getting_tournament_data(tournament):
    date = [word for word in tournament.find('td', width='120').stripped_strings][0]
    ratings = [text for text in tournament.find('td', width='160').stripped_strings]
    name = tournament.find('td', width='350').a.getText()
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
    BASE_URL = 'http://www.uschess.org/msa/MbrDtlTnmtHst.php?'

    PLAYER_ID = input("Enter your USCF ID: ")
    PLAYER_URL = BASE_URL + PLAYER_ID

    NUM_TOURNEYS = int(input("Enter the number of tournaments you played: "))
    MAX_PAGE = math.ceil(NUM_TOURNEYS / 50) + 1


    TOURNAMENTS = []
    for page in range(1, MAX_PAGE):
        page_data = get_data(PLAYER_URL, page)
        for tourney in page_data:
            TOURNAMENTS.append(getting_tournament_data(tourney))
    
    DATA_FILE = PLAYER_ID + ".csv"
    data = open(DATA_FILE, 'w')
    data.write('Date' + ',' + 'Rating' + '\n')
    for t in range(0, len(TOURNAMENTS)):
        data.write(TOURNAMENTS[t]['date'] + ',' + TOURNAMENTS[t]['arating'] + '\n')
    
    os.rename(DATA_FILE, "data/" + DATA_FILE)
    NEW_DATA_FILE =  "data/" + DATA_FILE
    print("YES")
    print("data/" + str(PLAYER_ID) + ".csv")


if __name__ == "__main__":
    main()
