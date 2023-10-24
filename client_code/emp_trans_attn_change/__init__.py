from ._anvil_designer import emp_trans_attn_changeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class emp_trans_attn_change(emp_trans_attn_changeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    comp_details = anvil.server.call('comp_get_details', gvarb.g_comcode)

    self.label_6.text = comp_details['comp_leave_head1']
    self.label_7.text = comp_details['comp_leave_head2']
    self.label_8.text = comp_details['comp_leave_head3']

    self.text_box_1.text = self.text_box_2.text = self.text_box_3.text = self.text_box_4.text = self.text_box_5.text = \
    self.text_box_6.text = self.text_box_7.text = self.text_box_8.text = 0.0

  def sum_tb_values(self):
    self.text_box_11.text = float(self.text_box_1.text) + float(self.text_box_2.text) + float(self.text_box_3.text) 
    self.text_box_11.text = float(self.text_box_11.text) + float(self.text_box_4.text) + float(self.text_box_5.text)
    self.text_box_11.text = float(self.text_box_11.text) + float(self.text_box_6.text) + float(self.text_box_7.text) 
    self.text_box_11.text = float(self.text_box_11.text) + float(self.text_box_8.text)

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








