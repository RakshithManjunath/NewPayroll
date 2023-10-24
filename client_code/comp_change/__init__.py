from ._anvil_designer import comp_changeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb
from datetime import datetime

class comp_change(comp_changeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.label_7.text = gvarb.g_comname+' '+(gvarb.g_mode+" for the month of "+gvarb.g_transdate.strftime("%B %Y")).upper()
    comp_details = anvil.server.call('comp_get_details', gvarb.g_comcode)
    
    self.text_box_7.text = comp_details['comp_name']
    self.text_box_1.text = comp_details['comp_addr1']
    self.text_box_2.text = comp_details['comp_addr2']
    self.text_box_3.text = comp_details['comp_addr3']
    self.text_box_4.text = comp_details['comp_pf_number']
    self.text_box_5.text = comp_details['comp_esi_number']
    self.text_box_6.text = comp_details['comp_pto_circle']
  
  #self.drop_down_1.items = anvil.server.call('comp_change_name_and_code')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_box_7.text == "":
      Notification("Company name cannot be blank").show()
    else:
      anvil.server.call('comp_update',gvarb.g_comcode,
      self.text_box_1.text, self.text_box_2.text,
      self.text_box_3.text,self.text_box_4.text,
      self.text_box_5.text,self.text_box_6.text,self.text_box_7.text)
      result = confirm(self.text_box_7.text+" modified successfully ! to continue relogin  ?", buttons=["Yes"])
      if result == "Yes":
         open_form('logform')
      
  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('comp_change')

  def text_box_7_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.text_box_7.text = self.text_box_7.text.upper()
    if (self.text_box_7.text):
      self.button_1.enabled = True 
    else:
      self.button_1.enabled = False  




