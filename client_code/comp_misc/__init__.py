from ._anvil_designer import comp_miscTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class comp_misc(comp_miscTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.refresh()

    # Any code you write here will run before the form opens.

  def refresh(self):
    comp_details = anvil.server.call('comp_get_details', gvarb.g_comcode)
    self.text_box_1.text = comp_details['comp_leave_head1']
    self.text_box_2.text = comp_details['comp_leave_head2']
    self.text_box_3.text = comp_details['comp_leave_head3']
    self.text_box_4.text = comp_details['comp_loan_head1']
    self.text_box_5.text = comp_details['comp_loan_head2']
    self.date_picker_1.date = comp_details['comp_pay_date']
    
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('comp_misc_leave_loan_update', gvarb.g_comcode, self.text_box_1.text,
                     self.text_box_2.text, self.text_box_3.text, self.text_box_4.text,
                     self.text_box_5.text,self.date_picker_1.date)

    self.refresh()

  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.text_box_1.text = self.text_box_1.text.upper()

  def text_box_2_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.text_box_2.text = self.text_box_2.text.upper()

  def text_box_3_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.text_box_3.text = self.text_box_3.text.upper()

  def text_box_4_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.text_box_4.text = self.text_box_4.text.upper()

  def text_box_5_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.text_box_5.text = self.text_box_5.text.upper()












