from ._anvil_designer import HomeTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .. import Globals
from ..Form1_copy import Form1_copy
from ..Economy import Economy
from ..Sectors import Sectors

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    data_gainers=anvil.server.call('gainers')
    self.gainers_panel.items=data_gainers
    data_losers=anvil.server.call('losers')
    self.losers_panel.items=data_losers
    self.sp500.figure=anvil.server.call('indices_graph','^GSPC','S&P 500')
    self.nasdaq.figure=anvil.server.call('indices_graph','^IXIC','NASDAQ')
    self.dow_jones.figure=anvil.server.call('indices_graph','^DJI','Dow Jones')
    self.vix.figure=anvil.server.call('indices_graph','^IXIC','VIX')
    self.stock_news_panel.items=anvil.server.call('general_stock_news')
    self.general_news_panel.items=anvil.server.call('general_news',20)
    self.rich_text_1.background='rgba(255,99,71,0.5)'
    

  def form_show(self, **event_args):
    pass

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    Globals.ticker=self.ticker_search.text
    open_form('Form1_copy')

  def autocomplete_1_change(self, **event_args):
    self.autocomplete_1.suggestions=['AAPA','AAPB','AAPC','AAPD','AAPE','AAPF','AAPG','AAPL']

  def autocomplete_1_suggestion_clicked(self, **event_args):
    Globals.ticker=self.autocomplete_1.text
    open_form('Form1_copy')

  def autocomplete_1_pressed_enter(self, **event_args):
    Globals.ticker=self.autocomplete_1.text
    open_form('Form1_copy')

  def economy_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Economy')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def sector_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Sectors')

  def stock_indices_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    major_indicies=['^GSPC','^IXIC','^DJI','^VIX','^RUA','CLUSD','GCUSD']
    major_indices_data=anvil.server.call('indices_day_change',major_indicies)
    
    self.dr_sp500.content=str("S&P 500: "+f"{major_indices_data[0]['1D']:.2f}%")
    if major_indices_data[0]['1D']>0:
      self.dr_sp500.background='rgba(124, 252, 0,0.2)'
      self.dr_sp500.foreground='rgba(0, 128, 0,1)'
    else:
      self.dr_sp500.background='rgba(255, 87, 51,0.2)'
      self.dr_sp500.foreground='rgba(255, 87, 51,1)'
      
    self.dr_nasdaq.content=str("NASDAQ: "+f"{major_indices_data[1]['1D']:.2f}%")
    if major_indices_data[1]['1D']>0:
      self.dr_nasdaq.background='rgba(124, 252, 0,0.2)'
      self.dr_nasdaq.foreground='rgba(0, 128, 0,1)'
    else:
      self.dr_nasdaq.background='rgba(255, 87, 51,0.2)'
      self.dr_nasdaq.foreground='rgba(255, 87, 51,1)'
      
    self.dr_dji.content=str("Dow Jones: "+f"{major_indices_data[2]['1D']:.2f}%")
    if major_indices_data[2]['1D']>0:
      self.dr_dji.background='rgba(124, 252, 0,0.2)'
      self.dr_dji.foreground='rgba(0, 128, 0,1)'
    else:
      self.dr_dji.background='rgba(255, 87, 51,0.2)'
      self.dr_dji.foreground='rgba(255, 87, 51,1)'
      
    self.dr_vix.content=str("VIX: "+f"{major_indices_data[3]['1D']:.2f}%")
    if major_indices_data[3]['1D']>0:
      self.dr_vix.background='rgba(124, 252, 0,0.2)'
      self.dr_vix.foreground='rgba(0, 128, 0,1)'
    else:
      self.dr_vix.background='rgba(255, 87, 51,0.2)'
      self.dr_vix.foreground='rgba(255, 87, 51,1)'
      
    self.dr_russell3000.content=str("Russell 3000: "+f"{major_indices_data[4]['1D']:.2f}%")
    if major_indices_data[4]['1D']>0:
      self.dr_russell3000.background='rgba(124, 252, 0,0.2)'
      self.dr_russell3000.foreground='rgba(0, 128, 0,1)'
    else:
      self.dr_russell3000.background='rgba(255, 87, 51,0.2)'
      self.dr_russell3000.foreground='rgba(255, 87, 51,1)'
      
    self.dr_oil.content=str("Oil: "+f"{major_indices_data[5]['1D']:.2f}%")
    if major_indices_data[5]['1D']>0:
      self.dr_oil.background='rgba(124, 252, 0,0.2)'
      self.dr_oil.foreground='rgba(0, 128, 0,1)'
    else:
      self.dr_oil.background='rgba(255, 87, 51,0.2)'
      self.dr_oil.foreground='rgba(255, 87, 51,1)'
      
    self.dr_gold.content=str("Gold: "+f"{major_indices_data[6]['1D']:.2f}%")
    if major_indices_data[6]['1D']>0:
      self.dr_gold.background='rgba(124, 252, 0,0.2)'
      self.dr_gold.foreground='rgba(0, 128, 0,1)'
    else:
      self.dr_gold.background='rgba(255, 87, 51,0.2)'
      self.dr_gold.foreground='rgba(255, 87, 51,1)'

    




    










