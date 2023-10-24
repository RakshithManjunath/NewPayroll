from ._anvil_designer import stat_pfTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class stat_pf(stat_pfTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.refresh()

    # Any code you write here will run before the form opens.

  def refresh(self):
    comp_details = anvil.server.call('comp_get_details', gvarb.g_comcode)
    self.text_box_2.text = comp_details['comp_emp_pfrate']
    self.text_box_3.text = comp_details['comp_empr_fpfrate']
    self.text_box_4.text = comp_details['comp_pf_admin']
    self.text_box_5.text = comp_details['comp_pf_edli']
    self.text_box_7.text = comp_details['comp_mgmt_pf_lt']
    self.text_box_8.text = comp_details['comp_mgmt_fpf_lt']

