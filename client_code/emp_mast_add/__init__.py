from ._anvil_designer import emp_mast_addTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class emp_mast_add(emp_mast_addTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.label_4.text = gvarb.g_comname+' '+(gvarb.g_mode+" for the month of "+gvarb.g_transdate.strftime("%B %Y")).upper()
    self.drop_down_1.items = anvil.server.call('dept_change_name_and_code',gvarb.g_comcode)
    self.drop_down_2.items = anvil.server.call('desi_change_name_and_code',gvarb.g_comcode)
    self.label_5.text = anvil.server.call('get_last_emp_code',gvarb.g_comcode)
    
  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_1.visible = not self.custom_1.visible
    self.custom_2.visible = False
    self.custom_3.visible = False

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_1.visible = False
    self.custom_2.visible = not self.custom_2.visible
    self.custom_3.visible = False

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_1.visible = False
    self.custom_2.visible = False
    self.custom_3.visible = not self.custom_3.visible

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('emp_mast_add')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_box_1.text == "" and self.text_box_2.text == "":
      Notification("Employee code & name cannot be blank").show()
    else:
      if self.radio_button_1.selected == True:
        emp_sex = "Male"
      else:
        emp_sex = "Female"

      if self.radio_button_3.selected == True:
        emp_type = "Staff"
      else:
        emp_type = "Worker"

      #######################
      ###      PF Tab     ###
      #######################
      if self.custom_1.radio_button_1.selected == True:
        pf_contribution = True
        # self.custom_1.text_box_1.enabled = True
        # self.custom_1.text_box_2.enabled = True
      else:
        pf_contribution = False
        # self.custom_1.text_box_1.enabled = False
        # self.custom_1.text_box_2.enabled = False

      #######################
      ###     ESI Tab     ###
      #######################
      if self.custom_2.radio_button_1.selected == True:
        esi_contribution = True
      else:
        esi_contribution = False

      #######################
      ###  PT & IT Tab    ###
      #######################
      if self.custom_3.radio_button_1.selected == True:
        pt_contribution = True
      else:
        pt_contribution = False

      if self.custom_3.radio_button_3.selected == True:
        it_contribution = True
      else:
        it_contribution = False

      dept_code,dept_name,desi_code,desi_name = None,None,None,None

      # to check if any option in the dropdown is chosen, if not by default it is none
      if self.drop_down_1.selected_value!=None:
        split_list_dept = self.drop_down_1.selected_value.split("|")
        split_list_dept = [ele.strip() for ele in split_list_dept] 
        dept_code,dept_name = split_list_dept[0],split_list_dept[1]

      # to check if any option in the dropdown is chosen, if not by default it is none
      if self.drop_down_2.selected_value!=None:
        split_list_desi = self.drop_down_2.selected_value.split("|")
        split_list_desi = [ele.strip() for ele in split_list_desi] 
        desi_code,desi_name = split_list_desi[0],split_list_desi[1]
    
      emp_id= anvil.server.call('emp_get_next_id_value')
      default_photo = anvil.server.call('get_media_from_bytes_image_emp_add','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','default')
      row = anvil.server.call('emp_add',emp_id,self.text_box_1.text,self.text_box_2.text,self.text_box_3.text,
                    self.date_picker_1.date,self.date_picker_2.date,emp_sex, emp_type,
                    pf_contribution,self.custom_1.text_box_1.text,self.custom_1.text_box_2.text,
                    esi_contribution,self.custom_2.text_box_1.text,self.custom_2.text_box_2.text,
                    pt_contribution,it_contribution, self.custom_3.text_box_1.text,dept_code,dept_name,
                    desi_code,desi_name,default_photo,gvarb.g_comcode)
      anvil.server.call('emp_default_values',row)
      date = anvil.server.call('cur_trans_date')
      # print(emp_id,date,self.text_box_1.text,self.text_box_2.text,self.text_box_3.text,emp_sex,
      #                  self.date_picker_1.date,self.date_picker_2.date,emp_type,dept_code,dept_name,desi_code,desi_name,
      #                  pf_contribution,self.custom_1.text_box_1.text,self.custom_1.text_box_2.text,
      #                  esi_contribution,self.custom_2.text_box_1.text,self.custom_2.text_box_2.text,
      #                  pt_contribution,it_contribution, self.custom_3.text_box_1.text)
      trans_row = anvil.server.call('emp_to_trans_transfer',emp_id,date[0],self.text_box_1.text,self.text_box_2.text,self.text_box_3.text,emp_sex,
                       self.date_picker_1.date,self.date_picker_2.date,emp_type,dept_code,dept_name,desi_code,desi_name,
                       pf_contribution,self.custom_1.text_box_1.text,self.custom_1.text_box_2.text,
                       esi_contribution,self.custom_2.text_box_1.text,self.custom_2.text_box_2.text,
                       pt_contribution,it_contribution, self.custom_3.text_box_1.text,gvarb.g_comcode,default_photo)

      anvil.server.call('trans_default_values',trans_row)

      Notification(self.text_box_2.text + " data added successfully").show()
      open_form('emp_mast_add')

  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.text_box_1.text = self.text_box_1.text.upper()
    if ((self.text_box_1.text) and (self.text_box_2.text )):
      self.text_box_3.enabled = True
      self.radio_button_1.enabled = True
      self.radio_button_2.enabled = True
      self.date_picker_1.enabled = True
      self.date_picker_2.enabled = True
      self.radio_button_3.enabled = True
      self.radio_button_4.enabled = True
      self.drop_down_1.enabled = True
      self.drop_down_2.enabled = True
      self.link_1.visible = True
      self.link_2.visible = True
      self.link_3.visible = True
      self.button_1.enabled = True
      self.button_2.enabled = True
    else:
      self.text_box_3.enabled = False
      self.radio_button_1.enabled = False
      self.radio_button_2.enabled = False
      self.date_picker_1.enabled = False
      self.date_picker_2.enabled = False
      self.radio_button_3.enabled = False
      self.radio_button_4.enabled = False
      self.drop_down_1.enabled = False
      self.drop_down_2.enabled = False
      self.link_1.visible = False
      self.link_2.visible = False
      self.link_3.visible = False
      self.button_1.enabled = False
      self.button_2.enabled = False

  def text_box_2_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.text_box_2.text = self.text_box_2.text.upper()
    if ((self.text_box_1.text) and (self.text_box_2.text )):
      self.text_box_3.enabled = True
      self.radio_button_1.enabled = True
      self.radio_button_2.enabled = True
      self.date_picker_1.enabled = True
      self.date_picker_2.enabled = True
      self.radio_button_3.enabled = True
      self.radio_button_4.enabled = True
      self.drop_down_1.enabled = True
      self.drop_down_2.enabled = True
      self.link_1.visible = True
      self.link_2.visible = True
      self.link_3.visible = True
      self.button_1.enabled = True
      self.button_2.enabled = True
    else:
      self.text_box_3.enabled = False
      self.radio_button_1.enabled = False
      self.radio_button_2.enabled = False
      self.date_picker_1.enabled = False
      self.date_picker_2.enabled = False
      self.radio_button_3.enabled = False
      self.radio_button_4.enabled = False
      self.drop_down_1.enabled = False
      self.drop_down_2.enabled = False
      self.link_1.visible = False
      self.link_2.visible = False
      self.link_3.visible = False
      self.button_1.enabled = False
      self.button_2.enabled = False

  def text_box_3_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.text_box_3.text = self.text_box_3.text.upper()


      
    
    
    
    










