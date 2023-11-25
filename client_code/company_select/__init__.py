from ._anvil_designer import company_selectTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users
from .. import gvarb

class company_select(company_selectTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # after login, populate dropdown 
    self.company_select_dp.items = anvil.server.call('company_select_code_and_name',gvarb.g_comcode)

  def submit_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.company_select_dp.selected_value!=None:
      split_list_comp = self.company_select_dp.selected_value.split("|")
      split_list_comp = [ele.strip() for ele in split_list_comp] 
      gvarb.g_comcode,gvarb.g_comname = split_list_comp[0],split_list_comp[1]
      company_row = anvil.server.call('comp_get_details',gvarb.g_comcode)
      company_row[]
      open_form('mode_select')
    else:
      Notification("Pls select company").show()

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('logform')
    #anvil.users.login_with_form()

  def company_select_dp_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.company_select_dp.selected_value!=None:
      self.submit_btn.enabled = True
    else:
      self.submit_btn.enabled = False
    
      














    
