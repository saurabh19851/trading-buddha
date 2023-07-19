import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import fmpsdk
import pandas as pd
import numpy as np

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
api_key='622f44c679bbfc88f813b6d43f217749'

def api_key():
  fmp_api_key='622f44c679bbfc88f813b6d43f217749'
  return fmp_api_key

'''
@anvil.server.callable
def session_api_key():
  api_key=anvil.server.session.get('api_key','622f44c679bbfc88f813b6d43f217749')
  anvil.server.session['api_key']=api_key
'''

@anvil.server.callable
def stock_info(ticker):
  company_profile=fmpsdk.company_profile(apikey=api_key(),symbol=ticker)[0]
  return company_profile
  
@anvil.server.callable
def price_chart(ticker):
  prices=fmpsdk.historical_price_full(apikey=api_key(),symbol=ticker,series_type='line')
  dates=[]
  closes=[]
  for x in prices:
    date=x['date']
    close=x['close']
    dates.append(date)
    closes.append(close)
  std=np.std(closes[0:259])
  mkt_cap=fmpsdk.
  return dates,closes,int(std)
    

  
  

