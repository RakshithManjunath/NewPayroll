from ._anvil_designer import dept_addTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class dept_add(dept_addTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if (gvarb.g_curmonyear == False):
      result = confirm("You can add department in current month only ! ok", buttons=["Yes"])
      open_form('dept')
    else:
      if self.text_box_1.text == "":
        Notification("Department name cannot be blank").show()
      else:
        dept_name_exists = anvil.server.call('dept_name_exists', self.text_box_1.text,gvarb.g_comcode)
        if dept_name_exists:
          self.value= anvil.server.call('dept_get_next_string_value')
          dept_id= anvil.server.call('next_dept_id_value')
          anvil.server.call('dept_add',dept_id,self.value, self.text_box_1.text,gvarb.g_comcode)
          Notification(self.text_box_1.text + " data added successfully").show()
          self.button_1.enabled = False
          self.clear_inputs()
        else:
          alert(f"{self.text_box_1.text} already exists,data not saved ")
          open_form('dept')
        
  def clear_inputs(self):
    # Clear our three text boxes
    self.text_box_1.text = None

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('dept')

  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.text_box_1.text = self.text_box_1.text.upper()
    if (self.text_box_1.text):
      self.button_1.enabled = True 
    else:
      self.button_1.enabled = False  



  