import plotly
import plotly.graph_objs as go


plotly.tools.set_credentials_file(username='japodhi', api_key='zTs5n4K159uYtkLcYxm3')

trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = [trace0, trace1]

plotly.plotly.plot(data, filename = 'basic-line', auto_open=True)