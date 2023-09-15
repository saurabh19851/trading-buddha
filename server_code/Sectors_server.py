import anvil.server
import fmpsdk
import pandas as pd
import numpy as np
import datetime
import requests
import plotly.express as px

@anvil.server.callable
def api_key():
  fmp_api_key='622f44c679bbfc88f813b6d43f217749'
  return fmp_api_key


@anvil.server.callable
def sectors():
  indices=['S&P 500','Communication services','Consumer Discretionary','Consumer Staples','Energy','Financials','Healthcare',\
           'Industrials','Materials','Real Estate','Technology','Utiities']
  tickers=['XLC','XLY','XLP','XLE','XLF','XLV','XLI','XLB','XLRE','XLK','XLU']
  data=pd.DataFrame(fmpsdk.historical_price_full(apikey=api_key(), symbol='SPY',series_type='line'))
  data.columns=['date','SPY']
  for x in tickers:
    a=pd.DataFrame(fmpsdk.historical_price_full(apikey=api_key(), symbol=x,series_type='line'))
    a.columns=['date',x]
    data=pd.merge(data, a,how='inner',on='date')
  data=data.set_index('date')
  data=data[::-1]
  returns=data.pct_change()
  cum_returns=((1+returns).cumprod())*100
  cum_returns.columns=indices
  fig=px.line(cum_returns,x=cum_returns.index,y=cum_returns.columns[0:])
  fig.update_layout(title={'text':'Sector Performance','xanchor':'center','yanchor':'top'},legend={'yanchor':'bottom','xanchor':'center'})
  return fig
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
