# ChessRatingPrediction

Scrapes USCF website to get tournament and rating history. Then you can see an interactive visualization of a particular player's interactive rating graph. 

I have also built an LSTM for predicting future rating graph which is in "LSTMs" folder. In this case, I used the rating data of IM(International Master) Praveen Balakrishnan!

# Setting up

1. Run getting_data.py(Enter the USCF ID, and the # of tournaments played) to get the appropriate data
2. Then run visualize.py using the same USCF ID. You will then be taken to a seperate webpage where you can see the rating graph!
3. If you wanna see the LSTM and the predictions it made checkout the LSTMs folder where I have the notebook, images, and trained model!

# Overview

We will go over what each Python file does

## getting_data.py

Takes in the USCF ID and the number of tournaments the specific player played.

Then we use that to iterate through the webpages and scrape the data we want to use to visualize the rating graph. 

Lastly, we put all of that information into a "csv" file labelled as USCF_ID.csv in the "data" directory.

## visualize.py

First we clean up the data, by dropping the empty columns, and removing certain characters at the end of the rating. 

Then used PlotLy, to plot the interactive rating graph. Date as x-value, and Rating as y-value. The interactive graph is displayed in a seperate tab, while the static graph is saved in the images directory.

# LSTMS

I built an LSTM model to predict the rating of IM Praveen Balakrishnan. I scaled the data, and then preprocessed with a time_step of 5. I then built my model! It was built with 3 LSTM  Cells, and a dense layer with a single neuron for the output. Then it was trained on 50 epochs worth of data.

Then I visualized, and predicted the data. You can see the accuracy in which the LSTM predicted the rating(although it seems to be overfitting the data slightly). The RMSE is quite similar though. 


# ToDo:

* Rating Graphs for more people(Hikaru Nakamura, Ray Robson and other GMs)
* Make it applicable to FIDE Rating Data
* Make Predictions on future data from past data!
