import anvil.server
import datetime
import fmpsdk
import datetime
import dateutil
import pandas as pd
import numpy as np
import plotly.express as px
import requests
import plotly.graph_objects as go

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def api_key():
  fmp_api_key='622f44c679bbfc88f813b6d43f217749'
  return fmp_api_key

#Code to get economic calendar data
@anvil.server.callable
def economic_calendar():
  start_date=str(datetime.timedelta(days=10))
  end_date=str(datetime.timedelta(days=-10))
  param = {'from':start_date,'to':end_date,'apikey': api_key()} 
  req=requests.get('https://financialmodelingprep.com/api/v3/economic_calendar?', param)
  data=req.json()
  data_US=[]
  for x in data:
    if x['country']=='US':
      data_US.append(x)
  return data_US

#Code to get graphs
@anvil.server.callable
def indices_graph(ticker,title):
  today=str(datetime.date.today())
  hist_date=str(datetime.date.today()-dateutil.relativedelta.relativedelta(years=30))
  data=fmpsdk.historical_price_full(apikey=api_key(), symbol=ticker,series_type='line',from_date=hist_date,to_date=today)
  data=pd.DataFrame(data)
  data.set_index(keys=['date'],inplace=True)
  data.columns=[title]
  fig=px.line(data,x=data.index,y=title)
  fig.update_layout(showlegend=False)
  fig.update_xaxes(rangeselector=dict(buttons=list([dict(count=1, label="1m", step="month", stepmode="backward"),\
                                                   dict(count=6, label="6m", step="month", stepmode="backward"),\
                                                   dict(count=1, label="YTD", step="year", stepmode="todate"),\
                                                   dict(count=1, label="1y", step="year", stepmode="backward"),\
                                                   dict(count=5, label="5y", step="year", stepmode="backward"),\
                                                   dict(count=10, label="10y", step="year", stepmode="backward"),dict(step="all")])))
  return fig

#Code to get general stock market news
@anvil.server.callable
def general_stock_news():
  param = {'page':0,'apikey':api_key()} 
  req=requests.get('https://financialmodelingprep.com/api/v4/stock-news-sentiments-rss-feed?', param)
  data=req.json()
  return data

#Code to get daily indices change
@anvil.server.callable
def indices_day_change(tickers):
  tickers=','.join(tickers)
  param={'apikey':api_key()}
  link='https://financialmodelingprep.com/api/v3/stock-price-change/'+tickers
  req=requests.get(link,param)
  data=req.json()
  return data

#Code for getting daily gainers
@anvil.server.callable
def gainers():
  param={'apikey':api_key()}
  a=requests.get('https://financialmodelingprep.com/api/v3/stock_market/gainers?',param)
  data=a.json()
  data=data[0:10]
  return data

#Code for getting daily losers
@anvil.server.callable
def losers():
  param={'apikey':api_key()}
  a=requests.get('https://financialmodelingprep.com/api/v3/stock_market/losers?',param)
  data=a.json()
  data=data[0:10]
  return data

#Function for getting general news 
@anvil.server.callable
def general_news(p):
  data=[]
  for x in range(p):  
      param={'page':p,'apikey':api_key()}
      req=requests.get('https://financialmodelingprep.com/api/v4/general_news?',param)
      raw_data=req.json()
      for y in raw_data:
          data.append(y)
  return data

#Function to call all functions in one sever call
@anvil.server.callable
def home_screen_data():
  #indices_day_change=indices_day_change()
  general_stock_news,general_news,gainers,losers,sp500_graph,nasdaq_graph,dowjones_graph,vix_graph={},{},{},{},{},{},{},{}
  general_stock_news=general_stock_news()
  general_news=general_news(20)
  gainers=gainers()
  losers=losers()
  sp500_graph=indices_graph('^GSPC','S&P 500')
  nasdaq_graph=indices_graph('^IXIC','NASDAQ')
  dowjones_graph=indices_graph('^DJI','Dow Jones')
  vix_graph=indices_graph('^IXIC','VIX')
  return general_stock_news,general_news,gainers,losers,sp500_graph,nasdaq_graph,dowjones_graph,vix_graph