from ._anvil_designer import Fundamentals_formTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .. import Globals


class Fundamentals_form(Fundamentals_formTemplate):
  financial_type=''
  period=''
  ticker=Globals.ticker
  fin_ratio=''
  ratio_period=''
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    #Code for populating financial statement table
    self.financial_type='is'
    self.period='y'
    data,cols=anvil.server.call('get_annual_IS',ticker)
    self.financial_table.columns=cols
    self.financial_table_panel.items=data
    #Code for populating Financial Ratios Table
    self.fin_ratio='Liq Ratio'
    self.ratio_period='ttm'
    ratios_cols,ratios_data=anvil.server.call('financial_ratios_ttm',ticker)
    self.ratios_grid.columns=ratios_cols
    self.ratios_panel.items=ratios_data
    

  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refreshing_data_bindings is called"""
    pass

  def form_show(self, **event_args):
    pass

  def text_box_1_show(self, **event_args):
    """This method is called when the TextBox is shown on the screen"""

  def autocomplete_1_change(self, **event_args):
    self.autocomplete_1.suggestions=['AAPL','AAPK','AAPT','AAPP','AAPB','AAPC']

  def Cash_flow_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.financial_type='cf'
    if self.period=='y':
      data,cols=anvil.server.call('get_annual_CF',self.ticker)
      self.financial_table.columns=cols
      self.financial_table_panel.items=data
    elif self.period=='q':
      data,cols=anvil.server.call('get_quarterly_CF',self.ticker)
      self.financial_table.columns=cols
      self.financial_table_panel.items=data
    
  def inc_stat_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.financial_type='is'
    if self.period=='y':
      data,cols=anvil.server.call('get_annual_IS',self.ticker)
      self.financial_table.columns=cols
      self.financial_table_panel.items=data
    else:
      data,cols=anvil.server.call('get_quarterly_IS',self.ticker)
      self.financial_table.columns=cols
      self.financial_table_panel.items=data

  def bal_sheet_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.financial_type='bs'
    if self.period=='y':
      data,cols=anvil.server.call('get_annual_BS',self.ticker)
      self.financial_table.columns=cols
      self.financial_table_panel.items=data
    else:
      data,cols=anvil.server.call('get_quarterly_BS',self.ticker)
      self.financial_table.columns=cols
      self.financial_table_panel.items=data

  def annual_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.period='y'
    if self.financial_type=='is':
      data,cols=anvil.server.call('get_annual_IS',self.ticker)
      self.financial_table.columns=cols
      self.financial_table_panel.items=data
    elif self.financial_type=='bs':
      data,cols=anvil.server.call('get_annual_BS',self.ticker)
      self.financial_table.columns=cols
      self.financial_table_panel.items=data
    elif self.financial_type=='cf':
      data,cols=anvil.server.call('get_annual_CF',self.ticker)
      self.financial_table.columns=cols
      self.financial_table_panel.items=data

  def Quarterly_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.period='q'
    if self.financial_type=='is':
      data,cols=anvil.server.call('get_quarterly_IS',self.ticker)
      self.financial_table.columns=cols
      self.financial_table_panel.items=data
    elif self.financial_type=='bs':
      data,cols=anvil.server.call('get_quarterly_BS',self.ticker)
      self.financial_table.columns=cols
      self.financial_table_panel.items=data
    elif self.financial_type=='cf':
      data,cols=anvil.server.call('get_quarterly_CF',self.ticker)
      self.financial_table.columns=cols
      self.financial_table_panel.items=data



      


    


