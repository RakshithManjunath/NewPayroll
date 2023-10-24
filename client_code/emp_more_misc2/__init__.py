from ._anvil_designer import emp_more_misc2Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class emp_more_misc2(emp_more_misc2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
   # self.image_1.source = anvil.server.call('emp_cur_photo',self.cur_empcode)


  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    self.image_1.source = file

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    parent = self.parent.parent.get_components()
    dropdowns = [component for component in parent if isinstance(component, anvil.DropDown)]

    split_list_emp = dropdowns[0].selected_value.split("|")
    split_list_emp = [ele.strip() for ele in split_list_emp] 
    emp_code,emp_name = split_list_emp[0],split_list_emp[1]
    anvil.server.call('emp_update_misc2',emp_code,self.image_1.source) 
  

