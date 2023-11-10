from ._anvil_designer import bank_add_changeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class bank_add_change(bank_add_changeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    if (gvarb.g_curmonyear == False):
      self.label_2.foreground = "#FF0000"
    self.label_2.text = gvarb.g_comname+' '+(gvarb.g_mode+" for the month of "+gvarb.g_transdate.strftime("%B %Y")).upper()
       
  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_1.visible = not self.custom_1.visible
    self.custom_2.visible = False

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_1.visible = False
    self.custom_2.visible = not self.custom_2.visible
    # after dept add to check added company
    self.custom_2.drop_down_1.items = anvil.server.call('bank_change_name_and_code',gvarb.g_comcode)

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')




