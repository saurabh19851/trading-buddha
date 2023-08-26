from ._anvil_designer import stock_news_rowTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class stock_news_row(stock_news_rowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.image_1.source=self.item['image']
    self.link_1.text=self.item['title']
    self.link_1.url=self.item['url']
    self.rich_text_1.content="Ticker: "+ self.item['symbol']
    self.rich_text_3.content='Sentiment: '+ self.item['sentiment']
    self.rich_text_2.content=self.item['publishedDate']
    self.rich_text_4.content=self.item['text']

    # Any code you write here will run before the form opens.

