from ._anvil_designer import comp_moreTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class comp_more(comp_moreTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    if (gvarb.g_curmonyear == False):
      self.label_2.foreground = "#FF0000"
    self.label_2.text = gvarb.g_comname+' '+(gvarb.g_mode+" for the month of "+gvarb.g_transdate.strftime("%B %Y")).upper()

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_1.visible = not self.custom_1.visible
    self.custom_2.visible = False
    self.custom_3.visible = False
    self.button_1.enabled = True
    self.button_2.enabled = True

    self.custom_1.refresh()

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_1.visible = False
    self.custom_2.visible = not self.custom_2.visible
    self.custom_3.visible = False
    self.button_1.enabled = True
    self.button_2.enabled = True

    self.custom_2.refresh()

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.custom_1.visible = False
    self.custom_2.visible = False
    self.custom_3.visible = not self.custom_3.visible
    self.button_1.enabled = True
    self.button_2.enabled = True

    self.custom_3.refresh()

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if (gvarb.g_curmonyear == False):
      result = confirm("You can do company modification in current month only ! ok", buttons=["Yes"])
      open_form('comp_more')
    else:    
      anvil.server.call('comp_more_update_earnhead', gvarb.g_comcode,
                      self.custom_1.text_box_1.text,
                      self.custom_1.text_box_3.text,
                      self.custom_1.text_box_5.text,
                      self.custom_1.text_box_7.text,
                      self.custom_1.text_box_9.text,
                      self.custom_1.text_box_11.text,
                      self.custom_1.text_box_13.text,
                      self.custom_1.text_box_15.text,
                      self.custom_1.text_box_17.text,
                      self.custom_1.text_box_19.text)

      anvil.server.call('comp_earnhead1',gvarb.g_comcode,self.custom_2.check_box_1.checked,
                      self.custom_2.check_box_2.checked,self.custom_2.check_box_3.checked,
                      self.custom_2.check_box_4.checked,self.custom_2.check_box_5.checked,
                      self.custom_2.check_box_6.checked,self.custom_2.check_box_7.checked,
                      self.custom_2.check_box_8.checked,self.custom_2.check_box_9.checked,
                      self.custom_2.check_box_10.checked,self.custom_2.check_box_11.checked,
                      self.custom_2.check_box_12.checked,self.custom_2.check_box_13.checked,
                      self.custom_2.check_box_14.checked,self.custom_2.check_box_15.checked,
                      self.custom_2.check_box_16.checked,self.custom_2.check_box_17.checked,
                      self.custom_2.check_box_18.checked,self.custom_2.check_box_19.checked,
                      self.custom_2.check_box_20.checked,self.custom_2.check_box_21.checked,
                      self.custom_2.check_box_22.checked,self.custom_2.check_box_23.checked,
                      self.custom_2.check_box_24.checked,self.custom_2.check_box_25.checked,
                      self.custom_2.check_box_26.checked,self.custom_2.check_box_27.checked,
                      self.custom_2.check_box_28.checked,self.custom_2.check_box_29.checked,
                      self.custom_2.check_box_30.checked,self.custom_2.check_box_31.checked,
                      self.custom_2.check_box_32.checked,self.custom_2.check_box_33.checked,
                      self.custom_2.check_box_34.checked,self.custom_2.check_box_35.checked,
                      self.custom_2.check_box_36.checked,self.custom_2.check_box_37.checked,
                      self.custom_2.check_box_38.checked,self.custom_2.check_box_39.checked,
                      self.custom_2.check_box_40.checked,self.custom_2.check_box_41.checked,
                      self.custom_2.check_box_42.checked,self.custom_2.check_box_43.checked,
                      self.custom_2.check_box_44.checked,self.custom_2.check_box_45.checked,
                      self.custom_2.check_box_46.checked,self.custom_2.check_box_47.checked,
                      self.custom_2.check_box_48.checked,self.custom_2.check_box_49.checked,
                      self.custom_2.check_box_50.checked,self.custom_2.check_box_51.checked,
                      self.custom_2.check_box_52.checked,self.custom_2.check_box_53.checked,
                      self.custom_2.check_box_54.checked,self.custom_2.check_box_55.checked,
                      self.custom_2.check_box_56.checked,self.custom_2.check_box_57.checked,
                      self.custom_2.check_box_58.checked,self.custom_2.check_box_59.checked,
                      self.custom_2.check_box_60.checked)

      anvil.server.call('comp_misc_leave_loan_update', gvarb.g_comcode, 
                      self.custom_3.text_box_1.text,
                      self.custom_3.text_box_2.text, 
                      self.custom_3.text_box_3.text, 
                      self.custom_3.text_box_4.text,
                      self.custom_3.text_box_5.text,
                      self.custom_3.date_picker_1.date)

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('comp_more')









