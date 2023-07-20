from ._anvil_designer import Form1_copyTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .. import Globals


class Form1_copy(Form1_copyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    ticker=Globals.ticker
    company_profile,mkt_cap,avg_volume,pe=anvil.server.call('stock_info',ticker)
    self.sector.text=company_profile['sector']
    self.industry.text=company_profile['industry']
    self.logo.source=company_profile['image']
    self.name.text=company_profile['companyName']
    self.name.url=company_profile['website']
    beta=company_profile['beta']
    self.beta.text=f'{beta:.2f}'
    self.mkt_cap.text=f'{mkt_cap/1000000:,.2f}'
    self.volume.text=f'{int(avg_volume/1000):,}'
    self.pe.text=pe
    dates,closes,std=anvil.server.call('price_chart',ticker)
    self.price_chart.data=go.Scatter(x=dates,y=closes,mode='lines')
    self.last_close.text=closes[0]
    self.high_52weeks.text=max(closes[0:259])
    self.low_52weeks.text=min(closes[0:259])
    
    self.std.text=std
    
    

  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refreshing_data_bindings is called"""
    pass

  def form_show(self, **event_args):
    pass
    
  def text_box_1_show(self, **event_args):
    """This method is called when the TextBox is shown on the screen"""
  def num_format(num):
    return '{:}'