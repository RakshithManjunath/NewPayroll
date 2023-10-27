from ._anvil_designer import mode_selectTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class mode_select(mode_selectTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.label_1.text = gvarb.g_comname.upper()

  
  def exit_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.users.logout()
    alert(f"You have logged out  successfully...!")
    open_form('company_select')

  def payroll_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    gvarb.g_mode = "Payroll "
    open_form('month_and_year_select')



