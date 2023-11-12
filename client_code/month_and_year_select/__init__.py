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

    self.cur_trans_date = anvil.server.call('cur_trans_date',gvarb.g_comcode)
    
    self.month_names_alphabets = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    self.month_names_numeric = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    self.year_names = ["2023", "2024", "2025", "2026"]

    if self.cur_trans_date[0].month <=9:
      month = str(self.cur_trans_date[0].month).zfill(2)
    else:
      month = str(self.cur_trans_date[0].month)
      
    self.month_db_lbl.text = self.month_names_alphabets[self.month_names_numeric.index(month)]
    self.year_db_lbl.text = self.cur_trans_date[0].year

  def submit_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    month = self.month_names_numeric[self.month_names_alphabets.index(self.month_db_lbl.text)]
    if month[0] == '0':
      month_in_int = int(month[-1])
    else:
      month_in_int = int(month)
    gvarb.g_transdate = date(self.year_db_lbl.text, month_in_int, 1)
    #print("gvarb transdate", gvarb.g_transdate)

    print(self.cur_trans_date[0])
    print(gvarb.g_transdate)
    
    if (self.cur_trans_date[0] != gvarb.g_transdate):
      print('date changed')
      gvarb.g_curmonyear = False
    else:
      print('same date')
      gvarb.g_curmonyear = True
    
    open_form('menu')
     
  def date_picker_1_change(self, **event_args):
    """This method is called when the selected date changes"""
    newdate = self.date_picker_1.date
    #print(newdate)
    if (newdate >= self.cur_trans_date[0]):
      #print('you cant set future or same transaction date than current transaction date')
      result = confirm(" you can not select future month & year than current transaction month & year  ! ok  ", buttons=["Yes"])
      if result == "Yes":
          open_form('month_and_year_select')
    else:
      modified_new_date = date(newdate.year,newdate.month, 1)
      #print(modified_new_date)
      month = str(modified_new_date.month)
      if modified_new_date.month <=9:
        month = str(modified_new_date.month).zfill(2)
        self.month_db_lbl.text = self.month_names_alphabets[self.month_names_numeric.index(str(month))]
        self.year_db_lbl.text = modified_new_date.year

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('logform')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.date_picker_1.visible = True
    self.button_2.visible = False
    self.date_picker_1.date = self.cur_trans_date[0]
