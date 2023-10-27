from ._anvil_designer import RowTemplate10Template
from anvil import *
import anvil.server

class RowTemplate10(RowTemplate10Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
