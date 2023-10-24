from ._anvil_designer import stat_bonusTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class stat_bonus(stat_bonusTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.refresh()

    # Any code you write here will run before the form opens.
  def refresh(self):
    self.drop_down_1.items = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    self.drop_down_2.items = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    comp_details = anvil.server.call('comp_get_details', gvarb.g_comcode)
    # self.drop_down_1.selected_value = comp_details['comp_bonus_from']
    # self.drop_down_2.selected_value = comp_details['comp_bonus_to']
    self.text_box_1.text = comp_details['comp_bonus_percentage']
    self.text_box_2.text = comp_details['comp_bonus_limit']
    self.label_6.text = comp_details['comp_bonus_from']
    self.label_7.text = comp_details['comp_bonus_to']

    pt_bonus_amount_included = comp_details['comp_bonus_pt_included']
    if pt_bonus_amount_included == True:
      self.radio_button_1.selected = True
    else:
      self.radio_button_2.selected = True
      


    


