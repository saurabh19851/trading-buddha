from ._anvil_designer import RowTemplate7Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ... import Globals

class RowTemplate7(RowTemplate7Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    ticker=Globals.ticker
    dates,title,text,url,images=anvil.server.call('news',)
    self.news_title_link.tag

    # Any code you write here will run before the form opens.
