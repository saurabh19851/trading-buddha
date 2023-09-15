from ._anvil_designer import Option_strategiesTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
from .. import Globals


class Option_strategies(Option_strategiesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    #Code for getting stock basic information
    ticker=Globals.ticker





  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refreshing_data_bindings is called"""
    pass

  def form_show(self, **event_args):
    ticker=Globals.ticker
    cols,opt_data=anvil.server.call('options_data',ticker)
    self.options_chain_data_grid.columns=cols
    self.options_chain_repeating_panel.items=opt_data


  def autocomplete_1_change(self, **event_args):
    self.autocomplete_1.suggestions=['AAPL','AAPK','AAPT','AAPP','AAPB','AAPC']
