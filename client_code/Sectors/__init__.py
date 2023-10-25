from ._anvil_designer import SectorsTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
from .. import Globals
from ..Home import Home
from ..Economy import Economy
from ..Stock import Stock

class Sectors(SectorsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.sectors.items=[('Communication services','XLC'),('Consumer Discretionary','XLY'),('Consumer Staples','XLP'),('Energy','XLE'),('Financials','XLF'),('Healthcare','XLV'),\
           ('Industrials','XLI'),('Materials','XLB'),('Real Estate','XLRE'),('Technology','XLK'),('Utiities','XLU')]
    # Any code you write here will run before the form opens.

    



  def form_show(self, **event_args):
    pass

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""


  def autocomplete_1_change(self, **event_args):
    self.autocomplete_1.suggestions=['AAPA','AAPB','AAPC','AAPD','AAPE','AAPF','AAPG','AAPL']

  def autocomplete_1_suggestion_clicked(self, **event_args):
    Globals.ticker=self.autocomplete_1.text
    open_form('Stock')

  def autocomplete_1_pressed_enter(self, **event_args):
    Globals.ticker=self.autocomplete_1.text
    open_form('Stock')

  def economy_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Economy')

  def sectors_change(self, **event_args):
    """This method is called when an item is selected"""
    sector_selected=self.sectors.selected_value
    fig=anvil.server.call('sectors',sector_selected)
    self.sector_graph.figure=fig
    

  def home_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("Home")


