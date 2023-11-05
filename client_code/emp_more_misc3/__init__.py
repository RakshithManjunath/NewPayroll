from ._anvil_designer import emp_more_misc3Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class emp_more_misc3(emp_more_misc3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    # split_list_emp = dropdowns[0].selected_value.split("|")
    # split_list_emp = [ele.strip() for ele in split_list_emp] 
    # emp_code,emp_name = split_list_emp[0],split_list_emp[1]
    # anvil.server.call('emp_update_misc3',emp_code,self.image_1.source) 