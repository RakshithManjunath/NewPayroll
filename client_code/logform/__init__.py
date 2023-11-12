from ._anvil_designer import logformTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class logform(logformTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
 
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    data = anvil.server.call('get_all_password')
    if len(list(data)) == 0:
        if(self.text_box_1.text== 'user1') and (self.text_box_2.text == '1'):
          self.label_1.visible = False
          self.label_2.visible = False
          self.label_4.visible = False        
          self.text_box_1.visible = False
          self.text_box_2.visible = False
          self.button_1.visible = False  
          self.button_2.visible = False        
          self.button_3.visible = True
          self.button_4.visible = True    
          # self.button_5.visible = True        
    else :
        value,row = anvil.server.call('check_username_and_password', self.text_box_1.text, self.text_box_2.text)
        if value == True:
          gvarb.g_comcode = row
          gvarb.g_username = self.text_box_1.text
          #print(gvarb.g_comcode)
          open_form('company_select')
        else:
          result = confirm("Invalid crdentials, login again !", buttons=["Yes"])
          if result == "Yes":
            open_form('logform')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('import_all_csv')
    open_form('logform')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('logform')

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('logform')

  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.text_box_1.text = self.text_box_1.text.upper()
    if ((self.text_box_1.text) and (self.text_box_2.text )):
      self.button_1.enabled = True 
    else:
      self.button_1.enabled = False  

  def text_box_2_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if ((self.text_box_1.text) and (self.text_box_2.text)):
      self.button_1.enabled = True   
    else:
      self.button_1.enabled = False  

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('comp_new')

