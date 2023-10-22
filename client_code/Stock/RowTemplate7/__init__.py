from ._anvil_designer import RowTemplate7Template
from anvil import *
import anvil.server
from ... import Globals

class RowTemplate7(RowTemplate7Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.news_title_link.text=self.item['title']
    self.news_title_link.url=self.item['url']
    self.news_date.content=self.item['publishedDate']
    self.news_text.content=self.item['text']
    self.news_image.source=self.item['image']

    # Any code you write here will run before the form opens.
