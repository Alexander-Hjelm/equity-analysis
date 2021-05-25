# Import yfinance
import matplotlib.pyplot as plt
import yfinance as yf  
import plotly.graph_objects as go
from datetime import datetime
import pandas

def plot_candlestick(data: pandas.DataFrame):
    fig = go.Figure(data=[go.Candlestick(
    open=data.Open,
    high=data.High,
    low=data.Low,
    close=data.Close)])

    #data.Close.plot()
    #data.Open.plot()
    #data.High.plot()
    #data.Low.plot()
    #plt.show()

    fig.show()


with open('input_stocks') as f:
    input_stocks = [line.rstrip() for line in f]

for st in input_stocks:

    now = datetime.now()
    now_str = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
    start_str = '2020-01-01'

    # Get the data for the stock Apple by specifying the stock ticker, start date, and end date
    data = yf.download(st, start_str, now_str)

    print(data)
    #data.append

    file_name = "data/{}".format(st)
    data.to_csv(file_name)

    data2 = pandas.read_csv(file_name)

    plot_candlestick(data2)

    #f = open(", "a")
    #f.write(data)
    #f.close()


# https://towardsdatascience.com/free-stock-data-for-python-using-yahoo-finance-api-9dafd96cad2e
