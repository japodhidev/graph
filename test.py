import datetime
import pandas as pd

def get_time():
    ''' Get the time now in 0000-00-00 00:00:00 format'''
    d_t = datetime.datetime.now()
    d_t = d_t.strftime('%Y-%m-%d %H:%M:%S')
    # print(d_t)
    return d_t


def write_csv():
    ''' Write relevant data to a CSV file on request '''

    x = []
    y = []
    z = []
    data = {'x': 9, 'y': 8, 'z': 6}
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
    date_c = pd.Timestamp(date_c)
    raw_data = {'timestamp': date_c, 'x-axis': x, 'y-axis': y, 'z-axis': z}

    d_frame = pd.DataFrame(raw_data, columns = ['timestamp', 'x-axis', 'y-axis', 'z-axis'])
    d_frame.to_csv('test.csv', mode='a', header=False)

if __name__ == '__main__':
    get_time()
    write_csv()
