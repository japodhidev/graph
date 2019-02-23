import datetime
import pandas as pd
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go

def get_time():
    ''' Get the time now in 0000-00-00 00:00:00 format'''
    d_time = datetime.datetime.now()
    d_t = d_time.strftime('%Y-%m-%d %H:%M:%S')
    d_d = d_time.strftime('%A')
    time_dict = {'timestamp': d_t, 'day': d_d}
    return time_dict


def write_csv():
    ''' Write relevant data to a CSV file on request '''

    x = []
    y = []
    z = []
    data = {'x': 1, 'y': 3, 'z': 0}
    # Append each value in a dict in a corresponding list variable
    for key, value in data.items():
        if key == 'x':
            x.append(value)
        if key == 'y':
            y.append(value)
        if key == 'z':
            z.append(value)
    # print(x, y, z)
    date_c = get_time();
    # print(date_c['timestamp'])
    date_t = pd.Timestamp(date_c['timestamp'])
    raw_data = {'timestamp': date_t, 'day': date_c['day'], 'x-axis': x, 'y-axis': y, 'z-axis': z}

    d_frame = pd.DataFrame(raw_data, columns = ['timestamp', 'day', 'x-axis', 'y-axis', 'z-axis'])
    d_frame.to_csv('test.csv', mode='a', header=False, index='Unnamed: 0')

def read_csv():
    ''' Read timestamp, x, y & z values from file '''
    d_frame = pd.read_csv('test.csv')
    # print (d_frame)
    return d_frame

def return_json(data_f):
    return data_f.to_json(orient='index')

if __name__ == '__main__':
    # write_csv()
    d_F = read_csv()
    print(return_json(d_F))
    # data = [go.Scatter( x=d_F['timestamp'], y=d_F['y-axis'] )]
    # plot(data, filename='pandas-time-series')
