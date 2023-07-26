from ._anvil_designer import Fundamentals_formTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .. import Globals


class Fundamentals_form(Fundamentals_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    #Code for getting stock basic information
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

    #Code for plotting price chart and volatility
    dates,closes,std=anvil.server.call('price_chart',ticker)
    self.price_chart.data=go.Scatter(x=dates,y=closes,mode='lines')
    self.last_close.text=closes[0]
    self.high_52weeks.text=max(closes[0:259])
    self.low_52weeks.text=min(closes[0:259])
    self.std.text=std
    #Code for calculating returns and entering them in returns table




  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refreshing_data_bindings is called"""
    pass

  def form_show(self, **event_args):
    pass

  def text_box_1_show(self, **event_args):
    """This method is called when the TextBox is shown on the screen"""

  def autocomplete_1_change(self, **event_args):
    self.autocomplete_1.suggestions=['AAPL','AAPK','AAPT','AAPP','AAPB','AAPC']
