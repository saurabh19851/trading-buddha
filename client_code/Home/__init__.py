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

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    data=anvil.server.call('gainers')
    self.gainers_panel.items=data

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


    










