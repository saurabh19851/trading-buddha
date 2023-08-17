import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import fmpsdk
import pandas as pd
import numpy as np
import datetime
import requests


@anvil.server.callable
def api_key():
  fmp_api_key='622f44c679bbfc88f813b6d43f217749'
  return fmp_api_key

#Code for getting annual Income statement Data
@anvil.server.callable
def get_annual_IS(ticker):
  income_statement=fmpsdk.income_statement(api_key(),ticker,period='annual')
  income_statement.reverse()
  rows=['Revenue','Cost of Revenue','Gross Profit','Operating Expenses','Operating Income','EBITDA','Net Income','EPS']
  data_filter=['revenue','costOfRevenue','grossProfit','operatingExpenses','operatingIncome','ebitda','netIncome','eps']
  data_ic=[{} for x in data_filter]
  years=["Name"]
  cols=[]
  for x in income_statement:
    for idx,val in enumerate(data_filter):
        data_ic[idx]['Name']=rows[idx]
        if val!='eps':
          data_ic[idx][x['calendarYear']]='{:,.0f}'.format(x[val]/1000000)
        else:
          data_ic[idx][x['calendarYear']]='{:,.1f}'.format(x[val])
    years.append(x['calendarYear'])
  for x in years:
    col=dict(id=x,title=x,data_key=x)
    cols.append(col)
  return data_ic,cols

#Code for getting Quarterly statement Data
@anvil.server.callable
def get_quarterly_IS(ticker):
  income_statement=fmpsdk.income_statement(api_key(),ticker,period='quarter')
  income_statement.reverse()
  rows=['Revenue','Cost of Revenue','Gross Profit','Operating Expenses','Operating Income','EBITDA','Net Income','EPS']
  data_filter=['revenue','costOfRevenue','grossProfit','operatingExpenses','operatingIncome','ebitda','netIncome','eps']
  data_ic=[{} for x in data_filter]
  years=["Name"]
  cols=[]
  for x in income_statement:
    for idx,val in enumerate(data_filter):
        data_ic[idx]['Name']=rows[idx]
        if val!='eps':
          data_ic[idx][x['period']+' '+x['calendarYear']]='{:,.0f}'.format(x[val]/1000000)
        else:
          data_ic[idx][x['period']+' '+x['calendarYear']]='{:,.1f}'.format(x[val])
    years.append(x['period']+' '+x['calendarYear'])
  for x in years:
    col=dict(id=x,title=x,data_key=x)
    cols.append(col)
  return data_ic,cols

#Code for getting Yearly Balance Sheet Data
@anvil.server.callable
def get_annual_BS(ticker):
  bs=fmpsdk.balance_sheet_statement(api_key(),ticker,period='annual')
  bs.reverse()
  rows=['Current Assets','Total Assets','Current Liabilities','Total Liabilities','Retained Earnings','Equity']
  data_filter=['totalCurrentAssets','totalAssets','totalCurrentLiabilities','totalLiabilities','retainedEarnings','totalEquity']
  data_bs=[{} for x in data_filter]
  years=["Name"]
  cols=[]
  for x in bs:
    for idx,val in enumerate(data_filter):
      data_bs[idx]['Name']=rows[idx]
      data_bs[idx][x['period']+' '+x['calendarYear']]='{:,.0f}'.format(x[val]/1000000)
    years.append(x['period']+' '+x['calendarYear'])
  for x in years:
    col=dict(id=x,title=x,data_key=x)
    cols.append(col)
  return data_bs,cols

#Code for getting Quaterly Balance Sheet Data
@anvil.server.callable
def get_quarterly_BS(ticker):
  bs=fmpsdk.balance_sheet_statement(api_key(),ticker,period='quarter')
  bs.reverse()
  rows=['Current Assets','Total Assets','Current Liabilities','Total Liabilities','Retained Earnings','Equity']
  data_filter=['totalCurrentAssets','totalAssets','totalCurrentLiabilities','totalLiabilities','retainedEarnings','totalEquity']
  data_bs=[{} for x in data_filter]
  years=["Name"]
  cols=[]
  for x in bs:
    for idx,val in enumerate(data_filter):
      data_bs[idx]['Name']=rows[idx]
      data_bs[idx][x['period']+' '+x['calendarYear']]='{:,.0f}'.format(x[val]/1000000)
    years.append(x['period']+' '+x['calendarYear'])
  for x in years:
    col=dict(id=x,title=x,data_key=x)
    cols.append(col)
  return data_bs,cols

#Code for getting Annual Cashflow
@anvil.server.callable
def get_annual_CF(ticker):
  cf=fmpsdk.cash_flow_statement(api_key(), ticker,period='annual')
  cf.reverse()
  rows=['Operating','Investing','Financing']
  data_filter=['netCashProvidedByOperatingActivities','netCashUsedForInvestingActivites','netCashUsedProvidedByFinancingActivities']
  data_cf=[{} for x in data_filter]
  years=["Name"]
  cols=[]
  for x in cf:
    for idx,val in enumerate(data_filter):
      data_cf[idx]['Name']=rows[idx]
      data_cf[idx][x['period']+' '+x['calendarYear']]='{:,.0f}'.format(x[val]/1000000)
    years.append(x['period']+' '+x['calendarYear'])
    for x in years:
      col=dict(id=x,title=x,data_key=x)
      cols.append(col)
  return data_cf,cols

# Code to get quarterly CF
@anvil.server.callable
def get_quarterly_CF(ticker):
  cf=fmpsdk.cash_flow_statement(api_key(), ticker,period='quarter')
  cf.reverse()
  rows=['Operating','Investing','Financing']
  data_filter=['netCashProvidedByOperatingActivities','netCashUsedForInvestingActivites','netCashUsedProvidedByFinancingActivities']
  data_cf=[{} for x in data_filter]
  years=["Name"]
  cols=[]
  for x in cf:
    for idx,val in enumerate(data_filter):
      data_cf[idx]['Name']=rows[idx]
      data_cf[idx][x['period']+' '+x['calendarYear']]='{:,.0f}'.format(x[val]/1000000)
    years.append(x['period']+' '+x['calendarYear'])
    for x in years:
      col=dict(id=x,title=x,data_key=x)
      cols.append(col)
  return data_cf,cols

@anvil.server.callable
def financial_ratios_ttm(ticker):
  data=fmpsdk.financial_ratios_ttm(apikey=api_key(),symbol=ticker)
  liq_ratios_list=['currentRatioTTM','quickRatioTTM','cashRatioTTM']
  profit_ratios_list=['grossProfitMarginTTM','operatingProfitMarginTTM','netProfitMarginTTM','returnOnAssetsTTM','returnOnEquityTTM','returnOnCapitalEmployedTTM']
  debt_ratios_list=['debtRatioTTM','debtEquityRatioTTM','totalDebtToCapitalizationTTM','companyEquityMultiplierTTM']
  oper_ratios_list=['daysOfSalesOutstandingTTM','daysOfInventoryOutstandingTTM','operatingCycleTTM']
  cf_ratios_list=['cashFlowToDebtRatioTTM','operatingCashFlowPerShareTTM','freeCashFlowPerShareTTM','operatingCashFlowSalesRatioTTM','cashFlowCoverageRatiosTTM']
  val_ratios_list=['dividendYielPercentageTTM','peRatioTTM','pegRatioTTM','payoutRatioTTM','priceToBookRatioTTM','priceToSalesRatioTTM','enterpriseValueMultipleTTM','payoutRatioTTM']
  param={'apikey':api_key()}
  ratios_data=requests.get('https://financialmodelingprep.com/api/v3/ratios-ttm/'+ticker,param)
  ratios_data=ratios_data[0]
  liq_ratios={k:v for (k,v) in ratios_data.items() if k in liq_ratios_list}
  profit_ratios={k:v for (k,v) in ratios_data.items() if k in profit_ratios_list}
  debt_ratios={k:v for (k,v) in ratios_data.items() if k in debt_ratios_list}
  oper_ratios={k:v for (k,v) in ratios_data.items() if k in oper_ratios_list}
  cf_ratios={k:v for (k,v) in ratios_data.items() if k in cf_ratios_list}
  val_ratios={k:v for (k,v) in ratios_data.items() if k in val_ratios_list}
  cols=[{"id": "Ratios", "title": "Ratios", "data_key": "Ratios" },{"id": "Value", "title": "Value", "data_key": "Value" }]
  ratios_to_return=[]
  selected_ratios=[]
  for x in liq_ratios:
    a={'Ratios':x.}
  
  
  return liq_ratios,profit_ratios,debt_ratios,oper_ratios,cf_ratios,val_ratios
  