from ._anvil_designer import pass_addTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class pass_add(pass_addTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  
    # Any code you write here will run before the form opens.
    self.label_5.text = gvarb.g_comname+' '+(gvarb.g_mode+" for the month of "+gvarb.g_transdate.strftime("%B %Y")).upper()
  
    
  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('pass_add')

  def button_1_click(self, **event_args):
    is_duplicate = anvil.server.call('duplicate_username_password_check', self.text_box_1.text,self.text_box_2.text)
    if is_duplicate:
      # Handle duplicate case (e.g., show an error message)
      print("Username and password exists")
      is_duplicate = confirm(" Username and password already exist, try different username and password  ! ok ", buttons=["Yes"])
      if is_duplicate == "Yes":
        open_form('pass_add')
    else:
      # Add the new record to the database
      print("Username and password doesnt exist")
    # """This method is called when the button is clicked"""
    # if self.text_box_1.text == "":
    #   Notification("User name cannot be blank").show()
    # else:
    #   id= anvil.server.call('pass_get_next_string_value')
    #   passcode= anvil.server.call('next_pass_code_value')
    #   row = anvil.server.call('pass_add',id,passcode, self.text_box_1.text,
    #                     self.text_box_2.text,gvarb.g_comcode)
    #   #anvil.server.call('comp_default_values',row)
    #   if  ((self.text_box_2.text ) == (self.text_box_3.text )):
    #     result = confirm(self.text_box_1.text+" user successfully added ! continue to login  ?", buttons=["Yes"])
    #     if result == "Yes":
    #       self.clear_inputs()
    #       open_form('logform')
    #   else:
    #     result = confirm(" Password re-confirmation failed !  ", buttons=["Yes"])
    #     if result == "Yes":
    #       self.clear_inputs()
    #       open_form('logform')
    
  def clear_inputs(self):
    # Clear our three text boxes
    self.text_box_1.text = ""
    self.text_box_2.text = ""
    self.text_box_3.text = ""

  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.text_box_1.text = self.text_box_1.text.upper()
    if ((self.text_box_1.text) and (self.text_box_2.text ) and (self.text_box_3.text )):
      self.button_1.enabled = True 
    else:
      self.button_1.enabled = False  

  def text_box_2_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if ((self.text_box_1.text) and (self.text_box_2.text ) and (self.text_box_3.text )):
      self.button_1.enabled = True 
    else:
      self.button_1.enabled = False  

  def text_box_3_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if ((self.text_box_1.text) and (self.text_box_2.text ) and (self.text_box_3.text )):
      self.button_1.enabled = True 
    else:
      self.button_1.enabled = False  

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.label_6.visible = True
    self.text_box_4.visible = True
    self.button_5.visible = True    
    self.button_2.visible = True
    self.button_3.visible = False
    self.button_4.visible = False

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('comp_new')

  def text_box_4_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if self.text_box_4.text == "":
      Notification("login password cannot be blank").show()
      self.button_5.enabled = False
    else:
      self.button_5.enabled = True

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    value,row = anvil.server.call('check_username_and_password', gvarb.g_username, self.text_box_4.text)
    if value == True:
      self.label_6.visible = False
      self.text_box_4.visible = False
      self.button_5.visible = False  
      
      self.label_2.visible = True
      self.label_3.visible = True
      self.label_4.visible = True
  
      self.text_box_1.visible = True
      self.text_box_2.visible = True
      self.text_box_3.visible = True
  
      self.button_1.visible = True
    else:
      result = confirm("Invalid crdentials, login again !", buttons=["Yes"])
      if result == "Yes":
        open_form('logform')



    

    



