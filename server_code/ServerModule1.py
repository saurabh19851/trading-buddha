import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import fmpsdk
import pandas as pd
import numpy as np
import datetime
import requests

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

@anvil.server.callable
def api_key():
  fmp_api_key='622f44c679bbfc88f813b6d43f217749'
  return fmp_api_key

'''
@anvil.server.callable
def session_api_key():
  api_key=anvil.server.session.get('api_key','622f44c679bbfc88f813b6d43f217749')
  anvil.server.session['api_key']=api_key
'''
#Code for fetching company info
@anvil.server.callable
def stock_info(ticker):
  company_profile=fmpsdk.company_profile(apikey=api_key(),symbol=ticker)[0]
  quote=fmpsdk.quote(api_key(),ticker)[0]
  mkt_cap=quote['marketCap']
  avg_volume=quote['avgVolume']
  pe=quote['pe']
  return company_profile,mkt_cap,avg_volume,pe


#Code for price chart info
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


#Code for returns
def returns(ticker):
  prices = fmp.historical_price_full(apikey=api_key(), symbol=ticker, series_type='line')
  dates = []
  closes = []
  for x in prices:
    date = x['date']
    close = x['close']
    dates.append(date)
    closes.append(close)
  dates = pd.to_datetime(dates)
  closes = pd.DataFrame(data=closes, index=dates)
  closes.sort_index(ascending=False, inplace=True)
  today = datetime.date.today()
  start = datetime.date(today.year-10, today.month, today.day)
  end = datetime.date.today()
  bus_day_2D = pd.bdate_range(start, end, freq='2B').sort_values(ascending=False)
  bus_day_W = pd.bdate_range(start, end, freq='W-Fri').sort_values(ascending=False)
  bus_day_M = pd.bdate_range(start, end, freq='BM').sort_values(ascending=False)
  bus_day_Q = pd.bdate_range(start, end, freq='BQ').sort_values(ascending=False)
  bus_day_HY = pd.bdate_range(start, end, freq='2BQ').sort_values(ascending=False)
  bus_day_Y = pd.bdate_range(start, end, freq='BY').sort_values(ascending=False)
  bus_day_3Y = pd.bdate_range(start, end, freq='3BY').sort_values(ascending=False)
  bus_day_5Y = pd.bdate_range(start, end, freq='5BY').sort_values(ascending=False)
  bus_day_10Y = pd.bdate_range(start, end, freq='10BY').sort_values(ascending=False)
  closes_2D = closes.filter(items=bus_day_D, axis=0)
  closes_1W = closes.filter(items=bus_day_W, axis=0)
  closes_1M = closes.filter(items=bus_day_M, axis=0)
  closes_1Q = closes.filter(items=bus_day_Q, axis=0)
  closes_HY = closes.filter(items=bus_day_HY, axis=0)
  closes_1Y = closes.filter(items=bus_day_Y, axis=0)
  closes_3Y = closes.filter(items=bus_day_3Y, axis=0)
  closes_5Y = closes.filter(items=bus_day_5Y, axis=0)
  closes_10Y = closes.filter(items=bus_day_10Y, axis=0)
  pct_chng_1D = (closes.iloc[0,0]-closes_2D.iloc[0,0])/closes.iloc[0,0]
  pct_chng_1W = (closes.iloc[0,0]-closes_1W.iloc[0,0])/closes.iloc[0,0]
  pct_chng_1Q = (closes.iloc[0,0]-closes_1Q.iloc[0,0])/closes.iloc[0,0]
  pct_chng_HY = (closes.iloc[0,0]-closes_HY.iloc[0,0])/closes.iloc[0,0]
  pct_chng_1Y = (closes.iloc[0,0]-closes_1Y.iloc[0,0])/closes.iloc[0,0]
  pct_chng_3Y = (closes.iloc[0,0]-closes_3Y.iloc[0,0])/closes.iloc[0,0]
  pct_chng_5Y = (closes.iloc[0,0]-closes_5Y.iloc[0,0])/closes.iloc[0,0]
  pct_chng_10Y = (closes.iloc[0,0]-closes_10Y.iloc[0,0])/closes.iloc[0,0]


#Code for getting Economic Indicators Data
@anvil.server.callable
def econ_indicators(selection):
  d=datetime.datetime.today().strftime('%Y-%m-%d')
  params={'name':selection,'from':'2010-01-01','to':d,'apikey':api_key()}
  response=requests.get('https://financialmodelingprep.com/api/v4/economic?', params)
  data=response.json()
  dates=[]
  values=[]
  for x in data:
    dates.append(x['date'])
    values.append(x['value'])
  return dates,values





