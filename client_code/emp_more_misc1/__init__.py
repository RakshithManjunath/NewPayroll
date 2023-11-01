from ._anvil_designer import emp_more_misc1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb


class emp_more_misc1(emp_more_misc1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.refresh()

  def refresh(self):
    if self.drop_down_1.selected_value !=None:
      self.text_box_6.text = self.drop_down_1.selected_value
      split_list_bank = self.drop_down_1.selected_value.split("|")
      split_list_bank = [ele.strip() for ele in split_list_bank] 
      bank_code,bank_name = split_list_bank[0],split_list_bank[1]
      self.bankrow = anvil.server.call('bank_get_details', bank_code,gvarb.g_comcode)
      self.text_box_7.text = self.bankrow['bank_ifsc']

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    self.refresh()

      
