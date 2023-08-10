from ._anvil_designer import stock_news_templateTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class stock_news_template(stock_news_templateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.news_image.source=self.item['image']
    self.news_link.text=self.item['title']
    self.news_link.url=self.item['url']
    self.news_ticker.text=self.item['symbol']
    self.news_sentiment.content=self.item['sentiment']
    self.news_date.content=self.item['publishedDate']
    self.news_text.content=self.item['text']
    # Any code you write here will run before the form opens.
