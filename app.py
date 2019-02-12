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

graph = dash.Dash(__name__)


graph.config.requests_pathname_prefix = graph.config.routes_pathname_prefix.split('/')[-1]

graph.layout = html.Div(children=[
		html.H1(children="Graph Heading"),

    	html.H2(children='''
    		Graph Description
    		'''),

        dcc.Graph(id='live-graph', animate=True,
        	figure={
        		'layout': {
        			'title' : 'Graph Data Visualization'
        		}
        	}),
        dcc.Interval(
            id='graph-update',
            interval=2*1000,
            n_intervals=0
        ),
    ]
)

@graph.callback(Output('live-graph', 'figure'),
              [Input('graph-update', 'n_intervals')])

def update_graph_scatter(n):
	X.append(X[-1]+1)
	Y.append(Y[-1]+Y[-1]*random.uniform(-0.1,0.1))

	data = plotly.graph_objs.Scatter(
			x=list(X),
			y=list(Y),
			name='Scatter',
			mode= 'lines+markers'
			)

	return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
												yaxis=dict(range=[min(Y),max(Y)])
												)
	}

server = graph.server


if __name__ == '__main__':
	graph.run_server(debug=True)
