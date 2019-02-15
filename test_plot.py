import plotly
import plotly.graph_objs as go
import requests
import json

data = {'x': 0.46, 'y': 0.46, 'z': 0.38}

# for key, value in data.items():
# 	print (key, value)
js_dt = json.dumps(data)
response = requests.post('https://sheltered-coast-93272.herokuapp.com/', 
	json=js_dt)
if response.ok:
	print(response.text)
# plotly.tools.set_credentials_file(username='japodhi', api_key='zTs5n4K159uYtkLcYxm3')

# trace0 = go.Scatter(
#     x=[1, 2, 3, 4],
#     y=[10, 15, 13, 17]
# )
# trace1 = go.Scatter(
#     x=[1, 2, 3, 4],
#     y=[16, 5, 11, 9]
# )
# data = [trace0, trace1]

# plotly.plotly.plot(data, filename = 'basic-line', auto_open=True)