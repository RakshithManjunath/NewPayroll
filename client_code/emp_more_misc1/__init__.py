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
    self.drop_down_1.items = anvil.server.call('bank_change_name_and_code',gvarb.g_comcode)
  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    #print(self.parent, self.parent.parent, self.parent.parent.parent)
    parent = self.parent.parent.get_components()
    dropdowns = [component for component in parent if isinstance(component, anvil.DropDown)]

    split_list_emp = dropdowns[0].selected_value.split("|")
    split_list_emp = [ele.strip() for ele in split_list_emp] 
    emp_code,emp_name = split_list_emp[0],split_list_emp[1]
    anvil.server.call('emp_update_misc1',emp_code,self.text_box_1.text,
                     self.text_box_2.text,self.text_box_3.text,
                     self.text_box_4.text,self.text_box_5.text)

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('emp_more_misc1')