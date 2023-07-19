from ._anvil_designer import HomeTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    sp500,dowjones,nasdaq=anvil.server.call('sp500_dowjones_nasdaq_graph')
    self.plot_1.figure=sp500
    self.plot_2.figure=dowjones
    self.plot_3.figure=nasdaq
    

    # Any code you write here will run before the form opens.

  def text_box_1_show(self, **event_args):
    """This method is called when the TextBox is shown on the screen"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert(f'Hello {self.text_box_1.text}!')

  def repeating_panel_1_show(self, **event_args):
    """This method is called when the RepeatingPanel is shown on the screen"""
    pass

  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refreshing_data_bindings is called"""
    pass

  def link_2_click(self, **event_args):
   open_form('Home.Form1')

  def outlined_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    open.form(Form1_copy)







