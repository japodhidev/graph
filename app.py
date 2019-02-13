import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque

X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config.requests_pathname_prefix = app.config.routes_pathname_prefix.split('/')[-1]

app.layout = html.Div(children=[
        html.H1(id='header', children='Graph'),
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=2*1000,
            n_intervals=0
        ),
    ]
)

@app.callback(Output('live-graph', 'figure'),
              [Input('graph-update', 'n_intervals')])

def update_graph_scatter(n):
    X.append(X[-1]+1)
    Y.append(Y[-1]+Y[-1]*random.uniform(-0.1,0.1))

    data = go.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
            )

    return {'data': [data],
            'layout' : go.Layout(
                title={'text': 'Vibration Analysis'},
                xaxis=dict(range=[min(X),max(X)], title= 'Displacement', gridcolor='#bdbdbd', gridwidth=1), 
                yaxis=dict(range=[min(Y),max(Y)], title= 'x-axis', gridcolor='#bdbdbd', gridwidth=1)
            )
    }


server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)