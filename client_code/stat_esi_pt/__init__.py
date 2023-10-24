from ._anvil_designer import stat_esi_ptTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class stat_esi_pt(stat_esi_ptTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.refresh()

    # Any code you write here will run before the form opens.

  def refresh(self):
    comp_details = anvil.server.call('comp_get_details', gvarb.g_comcode)
    self.text_box_1.text = comp_details['comp_esi_sal_lt']
    self.text_box_3.text = comp_details['comp_pts1_from']
    self.text_box_4.text = comp_details['comp_pts1_to']
    self.text_box_5.text = comp_details['comp_pts1_pt']
    
    self.text_box_7.text = comp_details['comp_pts2_from']
    self.text_box_8.text = comp_details['comp_pts2_to']
    self.text_box_9.text = comp_details['comp_pts2_pt']

    self.text_box_11.text = comp_details['comp_pts3_from']
    self.text_box_12.text = comp_details['comp_pts3_to']
    self.text_box_13.text = comp_details['comp_pts3_pt']




