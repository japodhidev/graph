import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque

# Flask specific imports
from flask import Flask, request, jsonify
import json
from flask import render_template, url_for

# Initialise Flask app
app = Flask(__name__)

# Flask variables populated by the HTTP POST method from the client
yaxis = []
xaxis = []
zaxis = []



# Dash Graph's x, y axes
X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)


@app.route('/', methods=['POST', 'GET'])
def pi(name=None):

    if request.method == 'POST':
        pi_data = request.json
        # print(f'Value from client {pi_data}')
        append_list(pi_data)
        # for i in pi_data:
        #     # X.append(pi_data[i])
        #     print ("i: ", pi_data[i])
        # print ("Here: ", list(X))
        # append_list(X)
        return jsonify(pi_data)
    if request.method == 'GET':
        # print ("y: ", yaxis)
        # print ("x: ", xaxis)
        # print ("z: ", zaxis)
        x_lst = str(xaxis)
        y_lst = str(yaxis)
        return render_template('index.html', xa=x_lst, ya=y_lst)

def append_list(dq_x):
    # print(type(dq_x))
    dq_ = json.loads(dq_x)
    counter = 0
    for key, value in dq_.items():
        
        if counter == 0:
            zaxis.append(value)
        elif counter == 1:
            yaxis.append(value)
        elif counter == 2:
            xaxis.append(value)
            
        counter = counter + 1
    print ("element: ", type(value))
    print(yaxis)
    if (len(xaxis) == 2):
        xaxis.pop(0)
        yaxis.pop(0)

# xaxis = xaxis[:3]
# yaxis = yaxis[:3]
# zaxis = zaxis[:3]

if __name__ == '__main__':
    app.run(debug=True)
