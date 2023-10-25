from ._anvil_designer import esi_form_add1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class esi_form_add1(esi_form_add1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def text_box_2_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.text_box_2.text = self.text_box_2.text.upper()

