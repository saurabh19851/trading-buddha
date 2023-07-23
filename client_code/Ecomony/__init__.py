from ._anvil_designer import EcomonyTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .. import Globals


class Ecomony(EcomonyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.indicators.items=['GDP','Real GDP','nominal GDP','Federal Funds','CPI','Inflation Rate','Inflation','Retail Sales','Consumer Sentiment',\
                           'Durable Goods','Unemployment Rate','Nonfarm payroll','Initial Claims','Industrial Production','Housing Unit Starts',\
                           'Vehicle Sales','US Recession Probabilities']
                          



  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refreshing_data_bindings is called"""
    pass

  def form_show(self, **event_args):
    pass

  def text_box_1_show(self, **event_args):
    """This method is called when the TextBox is shown on the screen"""

  def autocomplete_1_change(self, **event_args):
    self.autocomplete_1.suggestions=['AAPL','AAPK','AAPT','AAPP','AAPB','AAPC']

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def indicators_change(self, **event_args):
    """This method is called when an item is selected"""
    


