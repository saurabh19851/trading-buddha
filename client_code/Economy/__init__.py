from ._anvil_designer import EconomyTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
from anvil.js.window import jQuery
from anvil.js import get_dom_node
from .. import Globals


class Economy(EconomyTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    
                          



  def form_refreshing_data_bindings(self, **event_args):
    """This method is called when refreshing_data_bindings is called"""
    pass

  def form_show(self, **event_args):
    pass

  def text_box_1_show(self, **event_args):
    """This method is called when the TextBox is shown on the screen"""

  def autocomplete_1_change(self, **event_args):
    self.autocomplete_1.suggestions=['AAPL','AAPK','AAPT','AAPP','AAPB','AAPC']

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def indicators_change(self, **event_args):
    """This method is called when an item is selected"""
    selection=self.indicators.selected_value
    dates,values=anvil.server.call('econ_indicators',selection)
    self.indicator_chart.data=go.Scatter(x=dates,y=values,mode='lines')

  def home_click(self, **event_args):
    """This method is called when the link is clicked"""
    from ..Home import Home
    open_form('Home')
    

  def Sectors_click(self, **event_args):
    """This method is called when the link is clicked"""
    from ..Sectors import Sectors
    open_form('Sectors')

  def autocomplete_1_suggestion_clicked(self, **event_args):
    Globals.ticker=self.autocomplete_1.text
    from ..Stock import Stock
    open_form('Stock')

  def autocomplete_1_pressed_enter(self, **event_args):
    Globals.ticker=self.autocomplete_1.text
    from ..Stock import Stock
    open_form('Stock')

  def button_click(self, **event_args):
    """This method is called when the button is clicked"""
    button=event_args['sender']
    a=''
    b="<iframe width='100%' height='550px'>"
    link=''
    self.graph.clear()
    if button.text=='GDP':
        a='https://fred.stlouisfed.org/graph/graph-landing.php?g=1jbWT'
    elif button.text=='Real GDP':
        a='https://fred.stlouisfed.org/graph/graph-landing.php?g=1jbWV'
    elif button.text=='Nominal GDP':
        a='https://fred.stlouisfed.org/graph/graph-landing.php?g=1jsj9'
    elif button.text=='Federal Funds':
        a='https://fred.stlouisfed.org/graph/graph-landing.php?g=1jsjm'
    elif button.text=='CPI':
        a='https://fred.stlouisfed.org/graph/graph-landing.php?g=1icWK'
    elif button.text=='Inflation Rate':
        a='https://fred.stlouisfed.org/graph/graph-landing.php?g=1jj5k'
    elif button.text=='Oil Price':
        a='https://fred.stlouisfed.org/graph/graph-landing.php?g=1jj3O'
    elif button.text=='Manufacturing Output':
        a='https://fred.stlouisfed.org/graph/graph-landing.php?g=1jhzI'
    elif button.text=='Job Postings':
        a='https://fred.stlouisfed.org/graph/graph-landing.php?g=1jhs0'
    elif button.text=='Manufacturing Employees':
        a='"https://fred.stlouisfed.org/graph/graph-landing.php?g=1jhi5'
    elif button.text=='Delinquency Rate: Consumer Loans':
        a='https://fred.stlouisfed.org/graph/graph-landing.php?g=1jfRu'
    elif button.text=='Charge-Off: Business Loans':
        a='https://fred.stlouisfed.org/graph/graph-landing.php?g=1jfRl'
    elif button.text=='Financial Conditions Index':
        a='https://fred.stlouisfed.org/graph/graph-landing.php?g=1jsmA'
    elif button.text=='Leading Index':
        a='https://fred.stlouisfed.org/graph/graph-landing.php?g=11Zzp' 
    elif button.text=='Financial Stress Index':
        a='https://fred.stlouisfed.org/graph/graph-landing.php?g=1jfDG' 
    elif button.text=='Consumer Sentiment':
        a='https://fred.stlouisfed.org/graph/graph-landing.php?g=1jaRa' 
    elif button.text=='10-Year - Federal Fund':
        a='https://fred.stlouisfed.org/graph/graph-landing.php?g=1jsr9' 
    elif button.text=='New Housing Permits':
        a='https://fred.stlouisfed.org/graph/graph-landing.php?g=1jiYM' 
    elif button.text=='New Orders: Capital Goods':
        a='https://fred.stlouisfed.org/graph/graph-landing.php?g=1jj0T' 
    link=a+b
    iframe = jQuery(b).attr("src",a)
    iframe.appendTo(get_dom_node(self.graph))
    