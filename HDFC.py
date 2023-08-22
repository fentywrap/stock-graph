import plotly.graph_objects as go
import pandas as pd
df = pd.read_csv('HDFC.csv')
fig = go.Figure([go.Scatter(x=df['Date'], y=df['High'])])

fig.update_xaxes(ticks= "outside",
                 ticklabelmode= "period",
                 tickcolor= "black",
                 ticklen=5,
                 minor=dict(
                     griddash='dot',
                     gridcolor='black')
                )
fig.update_traces(line_color = 'dark blue')
fig.show()