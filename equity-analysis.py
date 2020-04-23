# Import yfinance
import matplotlib.pyplot as plt
import yfinance as yf  
import plotly.graph_objects as go
from datetime import datetime

now = datetime.now()
now_str = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
start_str = '2020-01-01'

# Get the data for the stock Apple by specifying the stock ticker, start date, and end date
data = yf.download('ASSA-B.ST', start_str, now_str)
 
# Plot the close prices
data.Close.plot()
data.Open.plot()
data.High.plot()
data.Low.plot()
plt.show()

fig = go.Figure(data=[go.Candlestick(
                open=data.Open,
                high=data.High,
                low=data.Low,
                close=data.Close)])

fig.show()

print(data)


# https://towardsdatascience.com/free-stock-data-for-python-using-yahoo-finance-api-9dafd96cad2e
