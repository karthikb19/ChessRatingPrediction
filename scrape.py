from bs4 import BeautifulSoup
import urllib.request
import requests
import pandas as pd
from requests_html import HTMLSession
import math
import os
import plotly.express as px
import plotly.graph_objects as go  
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

def cleaning(pi, df):
    labels = df["Rating"]
    for i in range(len(labels)):
        print(labels[i])
        if(len(str((labels[i]))) == 9 or len(str((labels[i]))) == 8):
            labels[i] =  labels[i][0:3]
        elif(len(str((labels[i])))) == 10:
            labels[i] =  labels[i][0:4]
        else:
            continue

    df = df.dropna()
    return df


def visualize(pi, df):
    fig = px.line(df, x='Date', y='Rating', title="Graph of " + pi)
    fig.write_image(pi + ".png")
    fig.show()

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
    
    DATA_FILE = PLAYER_ID
    data = open(DATA_FILE, 'w')
    data.write('Date' + ',' + 'Rating' + '\n')
    for t in range(0, len(TOURNAMENTS)):
        data.write(TOURNAMENTS[t]['date'] + ',' + TOURNAMENTS[t]['arating'] + '\n')
    
    os.rename(DATA_FILE, "data/" + DATA_FILE)
    NEW_DATA_FILE =  "data/" + DATA_FILE
    print("YES")
    print("data/" + str(PLAYER_ID) + ".csv")

    df = pd.read_csv(f'{NEW_DATA_FILE}.csv')
    df = cleaning(PLAYER_ID, df)
    print(df.tail())
    df.to_csv(f'{NEW_DATA_FILE}.csv')
    visualize(PLAYER_ID, df)



if __name__ == "__main__":
    main()