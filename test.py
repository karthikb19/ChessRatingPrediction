import pandas as pd
df = pd.read_csv("data/14056673.csv")
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
print(df.head())
df.to_csv("data/14056673_1.csv", index = False)