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
    self.news_panel.items=anvil.server.call('general_stock_news')
    

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
    




    










