import anvil.server
import yahooquery as yq
import datetime
import fmpsdk
import pandas as pd
import numpy as np
import plotly.express as px
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
def option_pnl(ticker, options):
    data = fmpsdk.quote(api_key(), ticker)
    curr_price = data[0]['price']
    stock_price_range = pd.DataFrame(np.arange(
        curr_price*0.1, curr_price*2.0, curr_price*0.05), columns=['stock price'])
    buy_sell=''
    call_put = ''
    strike = 0
    premium = 0
    expiry=''
    for y in options:
        call_put=y['Option_Type']
        expiry=y['Expiry']
        strike=float(y['Strike'])
        buy_sell=y['Buy_Sell']
        premium=y['Premium']
        col_name=buy_sell+call_put+str(strike)
        if buy_sell == 'Buy':
            if call_put == 'calls':
                stock_price_range[col_name] = stock_price_range['stock price'].apply(lambda x: max(0, x-strike)-premium)
            elif call_put == 'puts':
                stock_price_range[col_name] = stock_price_range['stock price'].apply(lambda x: max(0, strike-x)-premium)
        elif buy_sell == 'Sell':
            if call_put == 'calls':
                stock_price_range[col_name] = stock_price_range['stock price'].apply(lambda x: min(0, strike-x)+premium)
            elif call_put == 'puts':
                options_pnl = min(0, stock_price_range-strike)+premium
                stock_price_range[col_name] = stock_price_range['stock price'].apply(lambda x: min(0, x-strike)+premium)
    stock_price_range['total PnL']=stock_price_range.iloc[:,1:].sum(axis=1)
    fig=px.line(stock_price_range,x='stock price',y='total PnL')
    stock_price_dict=stock_price_range.to_dict(orient='records')
    columns=stock_price_range.columns
    cols=[]
    for x in columns:
        col=dict(id=x,title=x,data_key=x)
        cols.append(col)
    return cols,stock_price_dict,fig