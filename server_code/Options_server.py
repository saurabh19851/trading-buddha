import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import yahooquery as yq
import datetime
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
@anvil.server.callable
def options_data(ticker):
    options=yq.Ticker(ticker)
    options=options.option_chain
    options=options.reset_index()
    today_date=datetime.date.today()
    options['today']=pd.to_datetime(today_date)
    dif_days=(options['expiration']-options['today'])
    options['days to maturity']=dif_days.apply(lambda x: int(x.days))
    options['expiration date']=options['expiration'].apply(lambda x: (str(x.date())))
    cols=['expiration date','days to maturity','optionType','strike','lastPrice','percentChange','openInterest','impliedVolatility','inTheMoney']
    options_data=options.loc[:,cols]
    columns_name={'expiration date':'Expiry','days to maturity':'Days to Expiry','optionType':'Option Type',\
                  'strike':'Strike','lastPrice':'Last Price','percentChange':'Change (%)',\
                      'openInterest':'Open Interest','impliedVolatility':'Implied Vol','inTheMoney':'In Money'}
    options_data.rename(columns=columns_name,inplace=True)
    columns=options_data.columns
    cols=[]
    for x in columns:
        col=dict(id=x,title=x,data_key=x)
        cols.append(col)
    opt_data=options_data.to_dict('records')
    return cols,opt_data