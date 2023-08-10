import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
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

@anvil.server.callable
def general_stock_news():
  param = {'page':0,'apikey':api_key()} 
  req=requests.get('https://financialmodelingprep.com/api/v4/stock-news-sentiments-rss-feed?', param)
  data=req.json()
  return data