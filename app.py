# Flask specific imports
from flask import Flask, request, jsonify
import json
from flask import render_template, url_for, Response
from uuid import UUID
import validators
import datetime
import pandas as pd

# Initialise Flask app
app = Flask(__name__)

# Flask variables populated by the HTTP POST method from the client
yaxis = []
xaxis = []
zaxis = []

x_h = []
y_h = []
axis_time = []



@app.route('/', methods=['POST', 'GET'])
def pi(name=None):

    if request.method == 'POST':
        pi_data = request.json
        append_list(pi_data)
        write_csv(pi_data)

        return jsonify(pi_data)
    if request.method == 'GET':

        x_lst = str(xaxis)
        y_lst = str(yaxis)
        z_lst = str(yaxis)
        return render_template('index.html', xa=x_lst, ya=y_lst, za=z_lst)

@app.route('/api', methods=['POST'])
def rasp(name=None):
    # Get data sent through from the client via a POST request
    pi_data = request.json
    # Populate variables with the data received
    append_list(pi_data)

    # Return a json response
    return jsonify(pi_data)

@app.route('/api/<userid>', methods=['POST'])
def user(userid):
    '''
        Use the UUID as unique identify, somehow, add checks for validity of the uuid,
        send uuid relevant data back to the requested url
    '''
    boolTry = validators.uuid(str(userid))

    if boolTry == True:
        message = {'status': 'A valid UUID was provided'}
        return jsonify(message)
    else:
        message = {'status': 'An invalid UUID was provided'}
        return jsonify(message)

@app.route('/api/xaxis', methods=['POST'])
def x_axis(name=None):
    # Return y-axis values as a json response
    # print ("x length: ", len(xaxis))
    print("res x: ", xaxis)
    xax = jsonify(xaxis)
    xaxis.clear()
    print("res pop'd x: ", xaxis)
    return xax

@app.route('/api/yaxis', methods=['POST'])
def y_axis(name=None):
    # Return y-axis values as a json response
    print("res y: ", yaxis)
    yax = jsonify(yaxis)
    yaxis.clear()
    print("res pop'd y: ", yaxis)
    return yax

@app.route('/api/history', methods=['GET'])
def history():
    historyPopulate()
    return render_template('history.html')

@app.route('/api/history/x', methods=['POST'])
def historyX():
    x = {'x': x_h, 'timestamp': axis_time}
    return jsonify(x)

@app.route('/api/history/y', methods=['POST'])
def historyY():
    y = {'y': y_h, 'timestamp': axis_time}
    return jsonify(y)

# @app.route('/test')
# def test():
#     return render_template('test.html')
#
def append_list(dq_x):
    print("data: ", dq_x)
    # Load data sent through the requests
    # Populate the values into coordinates

    for key, value in dq_x.items():
        if key == 'x':
            xaxis.append(value)
            print("x: ", len(xaxis))
            print("value: ", xaxis)
        if key == 'y':
            yaxis.append(value)
        if key == 'z':
            zaxis.append(value)

    # Limit the length list to 6 elements long
    if (len(xaxis) == 3 or len(yaxis) == 3):
        xaxis.pop(0)
        print("pop 0 x: ", len(xaxis))
        print("value: ", xaxis)
        yaxis.pop(0)
        # del xaxis[0:3]
        # del yaxis[0:3]
    # Counter measure of sorts if the worst comes to
    # if (len(xaxis) == 10):
    #     xaxis.clear()
    #     yaxis.clear()

def validate_uuid(uid):
    # Validate UUID
    try:
        valid = UUID(str(uid), version=4)

        return True
    except ValueError as e:

        return False

def get_time():
    ''' Get the time now in 0000-00-00 00:00:00 format'''
    d_time = datetime.datetime.now()
    d_t = d_time.strftime('%Y-%m-%d %H:%M:%S')
    d_d = d_time.strftime('%A')
    time_dict = {'timestamp': d_t, 'day': d_d}
    return time_dict

def read_csv():
    ''' Read timestamp, x, y & z values from file '''
    d_frame = pd.read_csv('histogram.csv')

    return d_frame

def write_csv(data):
    ''' Write relevant data to a CSV file on request '''

    x = []
    y = []
    z = []

    # Append each value in a dict in a corresponding list variable
    for key, value in data.items():
        if key == 'x':
            x.append(value)
        if key == 'y':
            y.append(value)
        if key == 'z':
            z.append(value)

    date_c = get_time()

    date_t = pd.Timestamp(date_c['timestamp'])
    raw_data = {'timestamp': date_t, 'day': date_c['day'], 'x-axis': x, 'y-axis': y, 'z-axis': z}
    d_frame = pd.DataFrame(raw_data, columns = ['timestamp', 'day', 'x-axis', 'y-axis', 'z-axis'])
    d_frame.to_csv('histogram.csv', mode='a', header=False, index='Unnamed: 0')

def historyPopulate():
    # Read in data from csv and populate axes
    d_frame = read_csv()

    # Loop through each series and populate axes
    # Only populate empty lists
    for i in d_frame['x-axis']:
        if not x_h:
            x_h.append(i)
        else:
            x_h.clear()
            x_h.append(i)

    for j in d_frame['y-axis']:
        if not y_h:
            y_h.append(j)
        else:
            y_h.clear()
            y_h.append(j)

    for k in d_frame['timestamp']:
        if not axis_time:
            axis_time.append(k)
        else:
            axis_time.clear()
            axis_time.append(k)

if __name__ == '__main__':
    app.run(debug=True)
