import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go  
import math


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
    fig.write_image("images/" + pi + ".png")
    fig.show()



def main():
    print("Player ID: ")
    PLAYER_ID = input()
    DATA_PLAYER_ID = "data/" + PLAYER_ID + ".csv"

    df = pd.read_csv(DATA_PLAYER_ID)
    df = cleaning(PLAYER_ID, df)
    df.to_csv(DATA_PLAYER_ID)
    visualize(PLAYER_ID, df)

if __name__ == "__main__":
    main()
