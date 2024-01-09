from ._anvil_designer import day_selectTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class day_select(day_selectTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.label_2.text = (gvarb.g_comname+' '+gvarb.g_mode).upper()

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
  open_form('logform')
