from ._anvil_designer import month_and_year_selectTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb
from datetime import date,datetime

class month_and_year_select(month_and_year_selectTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.month = ""
    self.year = ""
    self.encoded_month = ""

    self.label_2.text = (gvarb.g_comname+' '+gvarb.g_mode).upper()

    self.cur_trans_date = anvil.server.call('cur_trans_date')

    self.month_names_alphabets = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    self.month_names_numeric = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    self.year_names = ["2023", "2024", "2025", "2026"]

    if self.cur_trans_date[0].month <=9:
      month = str(self.cur_trans_date[0].month).zfill(2)
    else:
      month = str(self.cur_trans_date[0].month)
      
    self.month_db_lbl.text = self.month_names_alphabets[self.month_names_numeric.index(month)]
    self.year_db_lbl.text = self.cur_trans_date[0].year

    self.month_select_dp.items = self.month_names_alphabets
    self.year_select_dp.items = self.year_names

  def submit_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.format_date_and_save()
    open_form('menu')

  def month_select_dp_change(self, **event_args):
    """This method is called when an item is selected"""
    self.month = self.month_select_dp.selected_value
    self.encoded_month = self.month_names_numeric[self.month_names_alphabets.index(self.month)]
    self.month_db_lbl.text = self.month

  def year_select_dp_change(self, **event_args):
    """This method is called when an item is selected"""
    self.year = self.year_select_dp.selected_value
    self.year_db_lbl.text = self.year

  def format_date_and_save(self):
    if self.year !="" and self.month !="":
      date_str = "01" + "/" + self.encoded_month + "/" + self.year
      date_obj = datetime.strptime(date_str, "%d/%m/%Y")
      gvarb.g_transdate = date_obj.date()
      #print(gvarb.g_transdate)
    elif self.year !="":
      date_str = "01" + "/" + str(self.cur_trans_date[0].month) + "/" + self.year
      date_obj = datetime.strptime(date_str, "%d/%m/%Y")
      gvarb.g_transdate = date_obj.date()
      #print(gvarb.g_transdate)
    elif self.month != "":
      date_str = "01" + "/" + self.encoded_month + "/" + str(self.cur_trans_date[0].year)
      date_obj = datetime.strptime(date_str, "%d/%m/%Y")
      gvarb.g_transdate = date_obj.date()
      #print(gvarb.g_transdate)
    else:
      gvarb.g_transdate = self.cur_trans_date[0]
      #print(gvarb.g_transdate)





    
