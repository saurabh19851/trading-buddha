import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import datetime
import fmpsdk

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
def indices_graph(ticker):
  data=