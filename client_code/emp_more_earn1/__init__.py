from ._anvil_designer import emp_more_earn1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class emp_more_earn1(emp_more_earn1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.refresh()
  
    # Any code you write here will run before the form opens.

  def refresh(self):
    comp_details = anvil.server.call('comp_get_details', gvarb.g_comcode)

    ## HEAD1 ######
    if comp_details['comp_earn_head1']!="":          
      self.label_1.text = comp_details['comp_earn_head1']
    else:
      self.text_box_1.enabled = False           

    ## HEAD2 ######
    if comp_details['comp_earn_head2']!="":      
      self.label_2.text = comp_details['comp_earn_head2']
    else:
      self.text_box_2.enabled = False     
      
    ## HEAD3 ###### 
    if comp_details['comp_earn_head3']!="":    
      self.label_3.text = comp_details['comp_earn_head3']
    else:
      self.text_box_3.enabled = False     
      
    ## HEAD4 ######
    if comp_details['comp_earn_head4']!="":    
      self.label_4.text = comp_details['comp_earn_head4']
    else:
      self.text_box_4.enabled = False     
    
    ## HEAD5 ######
    if comp_details['comp_earn_head5']!="":    
      self.label_5.text = comp_details['comp_earn_head5']
    else:
      self.text_box_5.enabled = False 
      
    ## HEAD6 ######
    if comp_details['comp_earn_head6']!="":    
      self.label_6.text = comp_details['comp_earn_head6']
    else:
      self.text_box_6.enabled = False 
      
    ## HEAD7 ######
    if comp_details['comp_earn_head7']!="":    
      self.label_7.text = comp_details['comp_earn_head7']
    else:
      self.text_box_7.enabled = False 
      
    ## HEAD8 ###### 
    if comp_details['comp_earn_head8']!="":
      self.label_8.text = comp_details['comp_earn_head8']
    else:
      self.text_box_8.enabled = False 
      
    ## HEAD9 ###### 
    if comp_details['comp_earn_head9']!="":
      self.label_9.text = comp_details['comp_earn_head9'] 
    else:
      self.text_box_9.enabled = False
      
    ## HEAD10 ###### 
    if comp_details['comp_earn_head10']!="":
      self.label_10.text = comp_details['comp_earn_head10']
    else:
      self.text_box_10.enabled = False
      
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    # split_list_emp = parent_form.drop_down_1.selected_value.split("|")
    #print(self.parent, self.parent.parent, self.parent.parent.parent)
    parent = self.parent.parent.get_components()
    dropdowns = [component for component in parent if isinstance(component, anvil.DropDown)]

    split_list_emp = dropdowns[0].selected_value.split("|")
    split_list_emp = [ele.strip() for ele in split_list_emp] 
    emp_code,emp_name = split_list_emp[0],split_list_emp[1]
    anvil.server.call('emp_update_earn',emp_code,self.text_box_1.text,
                     self.text_box_2.text,self.text_box_3.text,
                     self.text_box_4.text,self.text_box_5.text,
                     self.text_box_6.text,self.text_box_7.text,
                     self.text_box_8.text,self.text_box_9.text,
                     self.text_box_10.text,self.text_box_11.text)
    self.refresh()

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('emp_more_earn1')

  def sum_tb_values(self):
    self.text_box_11.text = float(self.text_box_1.text) + float(self.text_box_2.text) + float(self.text_box_3.text) 
    self.text_box_11.text = float(self.text_box_11.text) + float(self.text_box_4.text) + float(self.text_box_5.text)
    self.text_box_11.text = float(self.text_box_11.text) + float(self.text_box_6.text) + float(self.text_box_7.text) 
    self.text_box_11.text = float(self.text_box_11.text) + float(self.text_box_8.text)+ float(self.text_box_9.text)
    self.text_box_11.text = float(self.text_box_11.text) + float(self.text_box_10.text)
    
  def text_box_1_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.sum_tb_values()

  def text_box_2_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.sum_tb_values()

  def text_box_3_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.sum_tb_values()

  def text_box_4_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.sum_tb_values()

  def text_box_5_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.sum_tb_values()

  def text_box_6_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.sum_tb_values()

  def text_box_7_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.sum_tb_values()

  def text_box_8_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.sum_tb_values()

  def text_box_9_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.sum_tb_values()

  def text_box_10_lost_focus(self, **event_args):
    """This method is called when the TextBox loses focus"""
    self.sum_tb_values()










