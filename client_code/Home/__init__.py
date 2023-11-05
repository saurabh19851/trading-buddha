from ._anvil_designer import HomeTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
from .. import Globals


class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    '''
    data_gainers=anvil.server.call('gainers')
    self.gainers_panel.items=data_gainers
    data_losers=anvil.server.call('losers')
    self.losers_panel.items=data_losers
    self.sp500.figure=anvil.server.call('indices_graph','^GSPC','S&P 500')
    self.nasdaq.figure=anvil.server.call('indices_graph','^IXIC','NASDAQ')
    self.dow_jones.figure=anvil.server.call('indices_graph','^DJI','Dow Jones')
    self.vix.figure=anvil.server.call('indices_graph','^IXIC','VIX')
    self.stock_news_panel.items=anvil.server.call('general_stock_news')
    self.general_news_panel.items=anvil.server.call('general_news',20)
    self.rich_text_1.background='rgba(255,99,71,0.5)'
    '''
    general_stock_news,general_news,gainers,losers,sp500_graph,nasdaq_graph,dowjones_graph,vix_graph=anvil.server.call('home_screen_data')
    self.stock_news_panel.items=general_stock_news
    self.general_news_panel.items=general_news
    self.gainers_panel.items=gainers
    self.losers_panel.items=losers
    self.sp500.figure=sp500_graph
    self.nasdaq.figure=nasdaq_graph
    self.dow_jones.figure=dowjones_graph
    self.vix.figure=vix_graph

  
  def form_show(self, **event_args):
    pass

  def autocomplete_1_change(self, **event_args):
    self.autocomplete_1.suggestions=anvil.server.call('list_tickers',self.autocomplete_1.text)

  def autocomplete_1_suggestion_clicked(self, **event_args):
    Globals.ticker=self.autocomplete_1.text
    from ..Stock import Stock
    open_form('Stock')

  def autocomplete_1_pressed_enter(self, **event_args):
    Globals.ticker=self.autocomplete_1.text
    from ..Stock import Stock
    open_form('Stock')

  def economy_click(self, **event_args):
    """This method is called when the link is clicked"""
    from ..Economy import Economy
    open_form('Economy')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def sector_click(self, **event_args):
    """This method is called when the link is clicked"""
    from ..Sectors import Sectors
    open_form('Sectors')

  def stock_indices_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    major_indicies=['^GSPC','^IXIC','^DJI','^VIX','^RUA','CLUSD','GCUSD']
    major_indices_data=anvil.server.call('indices_day_change',major_indicies)

    self.dr_sp500.text=str("S&P 500: "+f"{major_indices_data[0]['1D']:.2f}%")
    if major_indices_data[0]['1D']>0:
      self.dr_sp500.foreground='rgba(0, 128, 0,1)'
    else:
      self.dr_sp500.foreground='rgba(255, 87, 51,1)'
      
    self.dr_nasdaq.text=str("NASDAQ: "+f"{major_indices_data[1]['1D']:.2f}%")
    if major_indices_data[1]['1D']>0:
      self.dr_nasdaq.foreground='rgba(0, 128, 0,1)'
    else:
      self.dr_nasdaq.foreground='rgba(255, 87, 51,1)'
      
    self.dr_dji.text=str("Dow Jones: "+f"{major_indices_data[2]['1D']:.2f}%")
    if major_indices_data[2]['1D']>0:
      self.dr_dji.foreground='rgba(0, 128, 0,1)'
    else:
      self.dr_dji.foreground='rgba(255, 87, 51,1)'
      
    self.dr_vix.text=str("VIX: "+f"{major_indices_data[3]['1D']:.2f}%")
    if major_indices_data[3]['1D']>0:
      self.dr_vix.foreground='rgba(0, 128, 0,1)'
    else:
      self.dr_vix.foreground='rgba(255, 87, 51,1)'
      
    self.dr_russell3000.text=str("Russell 3000: "+f"{major_indices_data[4]['1D']:.2f}%")
    if major_indices_data[4]['1D']>0:
      self.dr_russell3000.foreground='rgba(0, 128, 0,1)'
    else:
      self.dr_russell3000.foreground='rgba(255, 87, 51,1)'
      
    self.dr_oil.text=str("Oil: "+f"{major_indices_data[5]['1D']:.2f}%")
    if major_indices_data[5]['1D']>0:
      self.dr_oil.foreground='rgba(0, 128, 0,1)'
    else:
      self.dr_oil.foreground='rgba(255, 87, 51,1)'
      
    self.dr_gold.text=str("Gold: "+f"{major_indices_data[6]['1D']:.2f}%")
    if major_indices_data[6]['1D']>0:
      self.dr_gold.foreground='rgba(0, 128, 0,1)'
    else:
      self.dr_gold.foreground='rgba(255, 87, 51,1)'

    




    










