# Flask specific imports
from flask import Flask, request, jsonify
import json
from flask import render_template, url_for, Response
from uuid import UUID

# Initialise Flask app
app = Flask(__name__)

# Flask variables populated by the HTTP POST method from the client
yaxis = []
xaxis = []
zaxis = []


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

@app.route('/api/<uuid:user_id>', methods=['POST'])
def user():
    '''
        Use the UUID as unique identify, somehow, add checks for validity of the uuid,
        send uuid relevant data back to the requested url
    '''
    uid = request.script_root()
    validate_uuid(uid)

@app.route('/api/xaxis', methods=['POST'])
def x_axis(name=None):
    # Return y-axis values as a json response
    print ("x length: ", len(xaxis))
    xax = jsonify(xaxis)

    return xax

@app.route('/api/yaxis', methods=['POST'])
def y_axis(name=None):
    # Return y-axis values as a json response
    yax = jsonify(yaxis)

    return yax

#@app.route('/api/axis', methods=['POST', 'GET'])
#def axis(name=None):
#    if request.method == 'POST':
#        res = ''
#        x = "x"
#        y = "y"
#        axis_ = request.get_json();
#        print ("axis: ", axis_)
#
##        print (len(axis_str))
#
#        if  axis_[1] == x:
#            res = xaxis
#        elif axis_[1] == y:
#            res = yaxis
#
#
#        resp = jsonify(res)
#        return resp
#
#    if request.method == 'GET':
#        get_msg = "Method not allowed"
#        return render_template('error.html', msg=get_msg)

def append_list(dq_x):
    print("data: ", dq_x)
    # Load data sent through the request
    dq_ = json.loads(dq_x)
    # Loop counter for iterating through the values sent
    counter = 0
    # Populate the values into coordinates
    for key, value in dq_.items():
        if counter == 0:
            xaxis.append(value)
        elif counter == 1:
            yaxis.append(value)
        elif counter == 2:
            zaxis.append(value)

        counter = counter + 1
#    print ("element: ", type(value))
#    print("x: ", xaxis)
    # Limit the length list to 6 elements long
    if (len(xaxis) == 6 or len(yaxis) == 6):
        xaxis.pop(0)
        yaxis.pop(0)
    # Counter measure of sorts if the worst comes to
    if (len(xaxis) == 10):
        xaxis.clear()
        yaxis.clear()

def validate_uuid(uid):
    uid = uid.decode("utf-8")
    uid_ = uid[1:]

    # Validate UUID
    try:
        valid = UUID(uid_, version=4)
        message = {'status': 'A valid UUID was provided'}
    except ValueError as e:
        message = {'status': 'An invalid UUID was provided'}

    return jsonify(message)

if __name__ == '__main__':
    app.run(debug=True)
