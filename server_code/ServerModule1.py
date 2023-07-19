import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
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
api_key='622f44c679bbfc88f813b6d43f217749'

def api_key():
  fmp_api_key='622f44c679bbfc88f813b6d43f217749'
  return fmp_api_key

@anvil.server.callable
def session_api_key():
  api_key=anvil.server.session.get('api_key','622f44c679bbfc88f813b6d43f217749')
  anvil.server.session['api_key']=api_key

@anvil.server.callable
def stock_info_graph(ticker):
  company_profile=fmpsdk.company_profile(apikey=api_key(),symbol=ticker)
  
  
  

