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
  quote=fmpsdk.quote(api_key(),ticker)[0]
  mkt_cap=quote['marketCap']
  avg_volume=quote['avgVolume']
  pe=quote['pe']
  return company_profile,mkt_cap,avg_volume,pe
  
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
  return dates,closes,int(std)

def returns(ticker):
  prices=fmpsdk.historical_price_full(apikey=api_key(),symbol=ticker,series_type='line')
  dates=[]
  closes=[]
  for x in prices:
    date=x['date']
    close=x['close']
    dates.append(date)
    closes.append(close)
  dates=pd.to_datetime(dates)
  closes=pd.DataFrame(data=close,index=dates)
  today=datetime.date.today()
  start = datetime.date(today.year-10, today.month, today.day)
  end = datetime.date.today()
  bus_day_D=pd.bdate_range(start, end, freq='B')
  bus_day_W=pd.bdate_range(start, end, freq='W')
  bus_day_M=pd.bdate_range(start, end, freq='BM')
  bus_day_Q=pd.date_range(start, end, freq='BQ')
  bus_day_HY=pd.date_range(start, end, freq='2BQ')
  bus_day_Y=pd.date_range(start, end, freq='BY')
  bus_day_3Y=pd.date_range(start, end, freq='3BY')
  bus_day_5Y=pd.date_range(start, end, freq='5BY')
  bus_day_10Y=pd.date_range(start, end, freq='10BY')