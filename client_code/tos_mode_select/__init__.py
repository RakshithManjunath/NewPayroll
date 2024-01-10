from ._anvil_designer import tos_mode_selectTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class tos_mode_select(tos_mode_selectTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    #self.label_1.text = gvarb.g_comname+' '+(gvarb.g_mode+" for  "+gvarb.g_tosdate.strftime("%B %Y")).upper()
    self.label_1.text = gvarb.g_tosdate.strftime("%B %Y")
