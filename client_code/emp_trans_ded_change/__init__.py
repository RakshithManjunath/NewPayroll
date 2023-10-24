from ._anvil_designer import emp_trans_ded_changeTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class emp_trans_ded_change(emp_trans_ded_changeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    comp_details = anvil.server.call('comp_get_details', gvarb.g_comcode)

    self.label_1.text = comp_details['comp_ded1']
    self.label_2.text = comp_details['comp_ded2']
    self.label_3.text = comp_details['comp_ded3']
    self.label_4.text = comp_details['comp_ded4']

    self.label_5.text = comp_details['comp_loan_head1']
    self.label_6.text = comp_details['comp_loan_head2']
