from ._anvil_designer import Option_strategiesTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
from .. import Globals
from ..Stock import Stock
from ..Stock.Fundamentals_form import Fundamentals_form
from ..options import options



class Option_strategies(Option_strategiesTemplate):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    #Code for getting stock basic information
    self.ticker=Globals.ticker
    self.call_put=''
    self.options=[]
    self.expiry_dates=[]
    self.selected_expiry=''
    self.strikes=[]
    self.str_strikes=[]
    self.selected_Strike=0.0
    self.options_chain=[]
    self.premium=[]
    self.buy_sell=''
    self.selected_option={}
    self.options_list=[]
    

  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refreshing_data_bindings is called"""
    pass

  def form_show(self, **event_args):
    self.options_chain=Globals.option_chain
    self.call_put_dropdown.items=[("Call",'calls'),("Put",'puts')]
    self.buy_sell_dropdown.items=['Buy','Sell']
    

  def autocomplete_1_change(self, **event_args):
    self.autocomplete_1.suggestions=['AAPL','AAPK','AAPT','AAPP','AAPB','AAPC']

  def expiry_date_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    self.selected_expiry=self.expiry_date_dropdown.selected_value
    self.strikes=[x['Strike'] for x in self.options if x['Expiry']==self.selected_expiry]
    self.str_strikes=[str(x) for x in self.strikes]
    self.strike_dropdown.items=self.str_strikes
    

  def call_put_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    self.call_put=self.call_put_dropdown.selected_value
    self.options=[x for x in self.options_chain if x['Option Type']==self.call_put]
    self.expiry_dates=[x['Expiry'] for x in self.options_chain if x['Option Type']==self.call_put]
    self.expiry_dates=list(set(self.expiry_dates))
    self.expiry_date_dropdown.items=self.expiry_dates

  def strike_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    self.selected_Strike=self.strike_dropdown.selected_value

  def buy_sell_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    self.buy_sell=self.buy_sell_dropdown.selected_value
    self.premium=[x['Last Price'] for x in self.options_chain if x['Expiry']==self.selected_expiry if x['Option Type']==self.call_put if x['Strike']==float(self.selected_Strike)]

  def add_option_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.selected_option={"Option_Type":self.call_put,"Expiry":self.selected_expiry,"Strike":self.selected_Strike,"Buy_Sell":self.buy_sell,"Premium":self.premium[0]}
    self.options_list.append(self.selected_option)
    row=DataRowPanel(item=self.selected_option)
    self.selected_option_grid.add_component(row)

  def create_strategy_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    cols,pnl_data,fig=anvil.server.call('option_pnl',self.ticker,self.options_list)
    self.total_pnl.figure=fig
    self.options_pnl_grid.columns=cols
    self.options_pnl_panel.items=pnl_data

  def market_data_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Stock")

  def fundamental_data_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Stock.Fundamentals_form')

  def option_chain_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('options')




    






