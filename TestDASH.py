import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codpen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, serve_locally=True)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig1 = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')
fig2 = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')
fig3 = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children="Dash: A bel application framework for Python"), dcc.Graph(id='example-graph1', figure=fig1,
                                                                                 style={'width': '49%'}),
    html.Div(children="Dash: B bel application framework for Python"), dcc.Graph(id='example-graph2', figure=fig2),
    html.Div(children="Dash: C bel application framework for Python"), dcc.Graph(id='example-graph3', figure=fig3),

])

if __name__ == '__main__':
    app.run_server(debug=True)
