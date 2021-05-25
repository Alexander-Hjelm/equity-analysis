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

def get_data_filename(stock):
    return "data/{}".format(stock)

def download_stock_data(stocks, start_time_str):
    now = datetime.now()
    now_str = str(now.year) + '-' + str(now.month) + '-' + str(now.day)

    for st in stocks:
        # Get the data for the stock Apple by specifying the stock ticker, start date, and end date
        data = yf.download(st, start_time_str, now_str)
        
        file_name = get_data_filename(st)
        data.to_csv(file_name)
        #print(data)
        
    # TODO: Store/Get the latest retrieval time in a separate json file



with open('input_stocks') as f:
    input_stocks = [line.rstrip() for line in f]

download_stock_data(input_stocks, '2020-01-01')

for st in input_stocks:
    data2 = pandas.read_csv(file_name)

    plot_candlestick(data2)

    #f = open(", "a")
    #f.write(data)
    #f.close()


# https://towardsdatascience.com/free-stock-data-for-python-using-yahoo-finance-api-9dafd96cad2e
