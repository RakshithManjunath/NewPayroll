from ._anvil_designer import bank_changeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class bank_change(bank_changeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.drop_down_1.items = anvil.server.call('bank_change_name_and_code',gvarb.g_comcode)
 
  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    self.text_box_5.visible =True
    if self.drop_down_1.selected_value is not None:
      split_list_bank = self.drop_down_1.selected_value.split("|")
      split_list_bank = [ele.strip() for ele in split_list_bank] 
      self.bank_code,self.bank_name = split_list_bank[0],split_list_bank[1]
  
      self.row = anvil.server.call('bank_get_details',self.bank_code)
  
      self.text_box_1.text = self.row['bank_addr1']
      self.text_box_2.text = self.row['bank_addr2']
      self.text_box_3.text = self.row['bank_addr3']
      self.text_box_4.text = self.row['bank_ifsc']
      self.text_box_5.text = self.bank_name
      self.drop_down_1.visible = False
    else:
      self.button_1.enabled = False

  def text_box_5_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.drop_down_1.visible=True
    self.text_box_5.visible=False

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_box_5.text == "":
      Notification("Bank name cannot be blank").show()
    else:
      # bank_name_exists = anvil.server.call('bank_name_exists', self.text_box_1.text,gvarb.g_comcode)
      bank_name_exists = anvil.server.call('bank_name_exists', self.text_box_5.text,gvarb.g_comcode)
      if bank_name_exists:
        bank_ifsc_exists = anvil.server.call('bank_ifsc_exists', self.text_box_5.text)
        if not bank_ifsc_exists:
          anvil.server.call('bank_update', self.bank_code,
                     self.text_box_1.text, self.text_box_2.text,
                     self.text_box_3.text, self.text_box_4.text,
                     self.text_box_5.text)
          Notification(self.text_box_1.text + " data modified successfully").show()
          self.clear_inputs()
          self.drop_down_1.visible=True
          self.drop_down_1.items = anvil.server.call('bank_change_name_and_code',gvarb.g_comcode)
        else:
          alert(f"{self.text_box_5.text} already exists,data not saved ")
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

  def text_box_5_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.text_box_5.text = self.text_box_5.text.upper()
    if ((self.text_box_5.text) and (self.text_box_4.text)):
      self.button_1.enabled = True 
    else:
      self.button_1.enabled = False  

  def text_box_4_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.text_box_4.text = self.text_box_4.text.upper()
    if ((self.text_box_5.text) and (self.text_box_4.text)):
      self.button_1.enabled = True 
    else:
      self.button_1.enabled = False  




