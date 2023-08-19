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
def financial_ratios_ttm(ticker,ratios_type,period):
  ratios_data=fmpsdk.financial_ratios_ttm(apikey=api_key(),symbol=ticker)
  liq_ratios_list=['currentRatioTTM','quickRatioTTM','cashRatioTTM']
  profit_ratios_list=['grossProfitMarginTTM','operatingProfitMarginTTM','netProfitMarginTTM','returnOnAssetsTTM','returnOnEquityTTM','returnOnCapitalEmployedTTM']
  debt_ratios_list=['debtRatioTTM','debtEquityRatioTTM','totalDebtToCapitalizationTTM','companyEquityMultiplierTTM']
  oper_ratios_list=['daysOfSalesOutstandingTTM','daysOfInventoryOutstandingTTM','operatingCycleTTM']
  cf_ratios_list=['cashFlowToDebtRatioTTM','operatingCashFlowPerShareTTM','freeCashFlowPerShareTTM','operatingCashFlowSalesRatioTTM','cashFlowCoverageRatiosTTM']
  val_ratios_list=['dividendYielPercentageTTM','peRatioTTM','pegRatioTTM','payoutRatioTTM','priceToBookRatioTTM','priceToSalesRatioTTM','enterpriseValueMultipleTTM','payoutRatioTTM']
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
  for k,v in liq_ratios.items():
    a={'Ratios':k,'Value':v}
    selected_ratios.append(a)
  return cols,selected_ratios

@anvil.server.callable
def financial_ratios(ticker,ratio_type,period):
    selected_ratios=[]
    selected_ratios_data=[]
    cols=[]
    if period=='Annual':
        data=fmpsdk.financial_ratios(apikey=api_key(), symbol=ticker,period='annual',limit=8)
    elif period=='Quarterly':
        data=fmpsdk.financial_ratios(apikey=api_key(), symbol=ticker,period='quarter',limit=8)
    elif period=='TTM':
      cols,selected_ratios_data=financial_ratios_ttm(ticker,ratio_type,period)
      return cols, selected_ratios_data
    data.reverse()
    liq_ratios_list=['currentRatio','quickRatio','cashRatio']
    profit_ratios_list=['grossProfitMargin','operatingProfitMargin','netProfitMargin','returnOnAssets','returnOnEquity','returnOnCapitalEmployed']
    debt_ratios_list=['debtRatio','debtEquityRatio','totalDebtToCapitalization','companyEquityMultiplier']
    oper_ratios_list=['daysOfSalesOutstanding','daysOfInventoryOutstanding','operatingCycle']
    cf_ratios_list=['cashFlowToDebtRatio','operatingCashFlowPerShare','freeCashFlowPerShare','operatingCashFlowSalesRatio','cashFlowCoverageRatios']
    val_ratios_list=['dividendYield','dividendPayoutRatio','priceEarningsRatio','priceEarningsToGrowthRatio','payoutRatio','priceToBookRatio','priceToSalesRatio','enterpriseValueMultiple','payoutRatio']
    cols=[{"id": "Ratios", "title": "Ratios", "data_key": "Ratios" }]
    for x in data:
        date=x['date']
        a={"id": date, "title": date, "data_key": date }
        cols.append(a)
    if ratio_type=='Liquidity Ratios':
        selected_ratios=liq_ratios_list
    elif ratio_type=='Profitability Ratios':
        selected_ratios=profit_ratios_list
    elif ratio_type=='Leverage Ratios':
        selected_ratios=debt_ratios_list
    elif ratio_type=='Operating Ratios':
        selected_ratios=oper_ratios_list
    elif ratio_type=='Cashflow Ratios':
        selected_ratios=cf_ratios_list
    elif ratio_type=='Valuation Ratios':
        selected_ratios=val_ratios_list
    for x in selected_ratios:
        a=dict(Ratios=x)
        for y in data:
            a[y['date']]=f"{y[x]:.3f}"
        selected_ratios_data.append(a)
    return cols, selected_ratios_data
  