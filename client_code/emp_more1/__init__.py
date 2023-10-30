from ._anvil_designer import emp_more1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class emp_more1(emp_more1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.label_9.text = gvarb.g_comname+' '+(gvarb.g_mode+" for the month of "+gvarb.g_transdate.strftime("%B %Y")).upper()
    self.drop_down_1.items = anvil.server.call('comp_wise_emp_code_and_name', gvarb.g_comcode)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_1.visible = not self.custom_1.visible
    self.custom_2.visible = False
    self.custom_3.visible = False
    self.refresh()

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_1.visible = False
    self.custom_2.visible = not self.custom_2.visible
    self.custom_3.visible = False
    self.refresh()

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_1.visible = False
    self.custom_2.visible = False
    self.custom_3.visible = not self.custom_3.visible

  def refresh(self):
    split_list_emp = self.drop_down_1.selected_value.split("|")
    split_list_emp = [ele.strip() for ele in split_list_emp] 
    self.emp_code,self.emp_name = split_list_emp[0],split_list_emp[1]
 
    self.row = anvil.server.call('emp_get_details',self.emp_code,gvarb.g_comcode)
    self.label_2.text = "Father / Husband name - "+self.row['emp_hus_name']
    self.label_3.text = self.row['emp_sex']
    self.label_4.text = self.row['emp_type']
    self.label_5.text = "Date of birth - "+ self.row['emp_dob'].strftime("%d/%m/%Y")
    self.label_6.text = "Date of Joining - "+ self.row['emp_doj'].strftime("%d/%m/%Y")
    self.label_7.text = self.row['emp_dept_name']
    self.label_8.text = self.row['emp_desi_name']    
    
    self.custom_1.text_box_1.text = self.row['earn1']
    self.custom_1.text_box_2.text = self.row['earn2']
    self.custom_1.text_box_3.text = self.row['earn3']
    self.custom_1.text_box_4.text = self.row['earn4']
    self.custom_1.text_box_5.text = self.row['earn5']
    self.custom_1.text_box_6.text = self.row['earn6']
    self.custom_1.text_box_7.text = self.row['earn7']
    self.custom_1.text_box_8.text = self.row['earn8']
    self.custom_1.text_box_9.text = self.row['earn9']
    self.custom_1.text_box_10.text = self.row['earn10']
    self.custom_1.text_box_11.text = self.row['total_fxd_salary']

    self.custom_2.text_box_1.text = self.row['phone_number']
    self.custom_2.text_box_2.text = self.row['alt_phone_number']
    self.custom_2.text_box_3.text = self.row['email_address']
    self.custom_2.text_box_4.text = self.row['aadhar_number']
    self.custom_2.text_box_5.text = self.row['attn_bonus']
    #self.custom_2.text_box_6.text = self.row['emp_bank']
    self.custom_2.text_box_6.text =  self.row['emp_bank_code']+ " | " +self.row['emp_bank'] 
    self.custom_2.drop_down_1.items = anvil.server.call('bank_change_name_and_code',gvarb.g_comcode)

    self.custom_3.image_1.source = self.row['emp_photo']
    self.button_1.enabled = True
    self.button_2.enabled = True
  
  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    self.link_1.visible = True
    self.link_2.visible = True
    self.link_3.visible = True
    self.refresh()
    self.custom_1.refresh()

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    split_list_emp = self.drop_down_1.selected_value.split("|")
    split_list_emp = [ele.strip() for ele in split_list_emp] 
    self.emp_code,self.emp_name = split_list_emp[0],split_list_emp[1]

    anvil.server.call('emp_update_earn',self.emp_code,self.custom_1.text_box_1.text,
                      self.custom_1.text_box_2.text,
                      self.custom_1.text_box_3.text,
                      self.custom_1.text_box_4.text,
                      self.custom_1.text_box_5.text,
                      self.custom_1.text_box_6.text,
                      self.custom_1.text_box_7.text,
                      self.custom_1.text_box_8.text,
                      self.custom_1.text_box_9.text,
                      self.custom_1.text_box_10.text,
                      self.custom_1.text_box_11.text)

    anvil.server.call('emp_update_misc1',self.emp_code,self.custom_2.text_box_1.text,
                      self.custom_2.text_box_2.text,
                      self.custom_2.text_box_3.text,
                      self.custom_2.text_box_4.text,
                      self.custom_2.text_box_5.text,
                      self.custom_2.text_box_6.text)

    #anvil.server.call('emp_update_misc2',self.emp_code,self.custom_3.image_1.source)   ## to be tested
    #anvil.server.call('emp_update_misc2b',self.emp_code,self.custom_3.image_1.source)   ## to be tested
    self.button_1.enabled = False
    Notification(self.emp_name+' [ '+self.emp_code+' ]' + " data saved successfully").show()


 