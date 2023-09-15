from ._anvil_designer import general_news_rowTemplate
from anvil import *
import anvil.server

class general_news_row(general_news_rowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.image_1.source=self.item['image']
    self.rich_text_2.content=self.item['publishedDate']
    self.link_1.text=self.item['title']
    self.link_1.url=self.item['url']
    self.rich_text_1.content=self.item['text']
    # Any code you write here will run before the form opens.


