from multiprocessing import Condition
import matplotlib.pyplot as plt
import yfinance as yf  
import plotly.graph_objects as go
from datetime import datetime
import pandas
import json
import random
import os

def plot_candlestick(data: pandas.DataFrame):
    fig = go.Figure(data=[go.Candlestick(
    open=data.Open,
    high=data.High,
    low=data.Low,
    close=data.Close)])
    fig.show()

def get_data_filename(stock):
    return "data/{}".format(stock)

def download_stock_data(stocks):
    # Get retrieval dates
    with open('data/retr_dates.json', 'r') as f:
        retr_data=f.read()
    retr_dates = json.loads(retr_data)

    now = datetime.now()
    now_str = str(now.year) + '-' + str(now.month) + '-' + str(now.day)

    for st in stocks:
        if st in retr_dates:
            start_str = str(retr_dates[st])
        else:
            start_str = "2020-01-01"

        if start_str == now_str:
            continue

        # Get the data for the stock Apple by specifying the stock ticker, start date, and end date
        data = yf.download(st, start_str, now_str)
        
        if os.path.exists(get_data_filename(st)):
            # Join with existing data
            data2 = pandas.read_csv(get_data_filename(st))
            data = data.append(data2)

        # Save to file
        file_name = get_data_filename(st)
        data.to_csv(file_name)
        #print(data)
    
        retr_dates[st] = now_str
    
    # Store retrieval dates
    with open("data/retr_dates.json", "w") as f:
        f.write(json.dumps(retr_dates))

def get_moving_average(data, period):
    count = data.shape[0]
    sum_avg=0
    for i in range(count-period, count):
        sum_avg = sum_avg + data.at[i, "Close"]
    return sum_avg/period

def assign_points(stocks, period):
    stock_points_pairs = []
    for st in stocks:
        data = pandas.read_csv(get_data_filename(st))

        current = data.at[data.shape[0]-1,"Close"]
        stock_points_pairs.append((st, current/get_moving_average(data, period)))
    return stock_points_pairs


with open('input_stocks') as f:
    input_stocks = [line.rstrip() for line in f]

# Remove comment lines
input_stocks = list(filter(lambda line: not line.startswith("//"), input_stocks))

print(input_stocks)

download_stock_data(input_stocks)

points14 = assign_points(input_stocks, 14)
points14.sort(key=lambda a: -a[1])
points150 = assign_points(input_stocks, 150)
points150.sort(key=lambda a: -a[1])

print("################# 2 Weeks MA")
print('\n'.join(map(str, points14)))
print("################# 150 Day MA")
print('\n'.join(map(str, points150)))

#for st in input_stocks:
#    file_name = get_data_filename(st)
#    data2 = pandas.read_csv(file_name)
#    plot_candlestick(data2)

# TODO:
# Read moving average from plt
# Find a valuation strategy

# https://towardsdatascience.com/free-stock-data-for-python-using-yahoo-finance-api-9dafd96cad2e
