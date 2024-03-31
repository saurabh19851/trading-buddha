from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
from anvil.js.window import jQuery
from anvil.js import get_dom_node


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    iframe = jQuery("<iframe width='100%' height='475px'>").attr("src","https://fred.stlouisfed.org/graph/graph-landing.php?g=1jhCp")
    iframe.appendTo(get_dom_node(self.column_panel_1))
    # Any code you write here will run before the form opens.
