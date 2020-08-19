import pandas as pd   
import plotly.express as px
import plotly.graph_objects as go   

df = pd.read_csv("updated_sam.csv")
fig = px.line(df, x='Date', y='Rating')
fig.write_image("updated_sam.png")
fig.show()