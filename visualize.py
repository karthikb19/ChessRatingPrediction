import pandas as pd
import matplotlib.pyplot as plt
import math
def roundup(x):
    return int(math.ceil(x / 100.0)) * 100

def tick_data(x):
    return list(dict.fromkeys(x))

PLAYER_URL = 'http://www.uschess.org/msa/MbrDtlTnmtHst.php?15397834'
ID = PLAYER_URL[45:53]

NAME = ID + ".csv"
IMG = ID + ".png"
df =  pd.read_csv(NAME)
df = df.dropna()
df.to_csv("updated_sam.csv")
print(df.head())
print(len(df))

# df = df.sort_values(by="Date", ascending=1)

# rating_data = df["Rating"]
# dates = df["Date"]

# upd = []
# for rate in rating_data:
#     rate = roundup(rate)
#     upd.append(rate)

# ticks_labels = tick_data(upd)
# ticks_labels.reverse()
# rating_dates = []
# for date in dates:
#     date = date[0:4]
#     rating_dates.append(date)

# xyicks = rating_dates[::-1]

# plt.plot_date(rating_dates, rating_data)
# # x = range(11)
# # y = range(7)
# # plt.xticks(y, ['2014', '2015', '2016', '2017', '2018', '2019', '2020'])
# # plt.yticks()
# # plt.savefig(IMG)
# plt.show()
