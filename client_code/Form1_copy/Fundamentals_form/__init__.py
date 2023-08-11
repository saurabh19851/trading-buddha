from ._anvil_designer import Fundamentals_formTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .. import Globals


class Fundamentals_form(Fundamentals_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    ticker=Globals.ticker
    income_statement_data,cols=anvil.server.call('get_annual_CF',ticker)
    self.income_statement.columns=cols
    self.income_statement_panel.items=income_statement_data





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
    pass

  def inc_stat_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass


