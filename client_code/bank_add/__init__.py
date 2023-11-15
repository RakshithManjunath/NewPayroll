from ._anvil_designer import bank_addTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class bank_add(bank_addTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if (gvarb.g_curmonyear == False):
      result = confirm("You can add bank in current month only ! ok", buttons=["Yes"])
      open_form('bank_add_change')
    else:
      if self.text_box_1.text == "":
        Notification("Bank name cannot be blank").show()
      else:
        #bank_name_exists = anvil.server.call('bank_name_exists', self.text_box_1.text,gvarb.g_comcode)
        bank_name_exists = anvil.server.call('bank_name_exists', self.text_box_5.text,gvarb.g_comcode)
      if bank_name_exists:
          bank_ifsc_exists = anvil.server.call('bank_ifsc_exists', self.text_box_5.text)
          if not bank_ifsc_exists:
            self.value= anvil.server.call('bank_get_next_string_value')
            bank_id= anvil.server.call('next_bank_id_value')
            row = anvil.server.call('bank_add',self.value,bank_id, self.text_box_1.text,
                    self.text_box_2.text,self.text_box_3.text,self.text_box_4.text,
                    self.text_box_5.text,gvarb.g_comcode)
            anvil.server.call('bank_default_values',row)
            Notification(self.text_box_1.text + " data added successfully").show()
            self.button_1.enabled = False
            self.clear_inputs()
          else:
            alert(f"{self.text_box_5.text} ifsc code already exists,data not saved ")
            open_form('bank_add_change')
      else:
          alert(f"{self.text_box_5.text} already exists,data not saved ")
          open_form('bank_add_change')
        
  def clear_inputs(self):
    # Clear our three text boxes
    self.text_box_1.text = ""
    self.text_box_2.text = ""
    self.text_box_3.text = ""
    self.text_box_4.text = ""
    self.text_box_5.text = ""

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('bank_add_change')

  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.text_box_1.text = self.text_box_1.text.upper()
    if ((self.text_box_1.text) and (self.text_box_5.text)):
      self.button_1.enabled = True 
    else:
      self.button_1.enabled = False  

  def text_box_5_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.text_box_5.text = self.text_box_5.text.upper()
    if ((self.text_box_1.text) and (self.text_box_5.text)):
      self.button_1.enabled = True 
    else:
      self.button_1.enabled = False  




