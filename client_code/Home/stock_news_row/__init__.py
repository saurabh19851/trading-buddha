from ._anvil_designer import stock_news_rowTemplate
from anvil import *
import anvil.server

class stock_news_row(stock_news_rowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.image_1.source=self.item['image']
    self.link_1.text=self.item['title']
    self.link_1.url=self.item['url']
    self.ticker.text="Ticker: "+ self.item['symbol']
    self.sentiment.text='Sentiment: '+ self.item['sentiment']
    self.date.text=self.item['publishedDate']
    self.text.text=self.item['text']

    # Any code you write here will run before the form opens.

