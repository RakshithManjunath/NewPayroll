from ._anvil_designer import comp_addTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class comp_add(comp_addTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_box_1.text == "":
      Notification("Company name cannot be blank").show()
    else:
      id= anvil.server.call('comp_get_next_string_value')
      compcode= anvil.server.call('next_comp_id_value')
      row = anvil.server.call('comp_add',id,compcode, self.text_box_1.text,
                        self.text_box_2.text,self.text_box_3.text,self.text_box_4.text,
                        self.text_box_5.text,self.text_box_6.text,
                        self.text_box_7.text)
      anvil.server.call('comp_default_values',row)
      result = confirm(self.text_box_1.text+" added successfully ! continue to login  ?", buttons=["Yes"])
      if result == "Yes":
        #Notification(self.text_box_1.text + " data added successfully").show()
        self.clear_inputs()
        open_form('logform')
    
  def clear_inputs(self):
    # Clear our three text boxes
    self.text_box_1.text = ""
    self.text_box_2.text = ""
    self.text_box_3.text = ""
    self.text_box_4.text = ""
    self.text_box_5.text = ""
    self.text_box_6.text = ""
    self.text_box_7.text = ""

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('comp_add')

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')

  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.text_box_1.text = self.text_box_1.text.upper()
    if (self.text_box_1.text):
      self.button_1.enabled = True 
    else:
      self.button_1.enabled = False  

