from ._anvil_designer import update_trans_dateTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import calendar
from datetime import datetime
from .. import gvarb

class update_trans_date(update_trans_dateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    if (gvarb.g_curmonyear == False):
      self.label_2.foreground = "#FF0000"
    self.label_2.text = gvarb.g_comname+' '+(gvarb.g_mode+" for the month of "+gvarb.g_transdate.strftime("%B %Y")).upper()

   # cur_trans_date = anvil.server.call('cur_trans_date')
    cur_trans_date = anvil.server.call('cur_trans_date',gvarb.g_comcode)

    month_names_alphabets = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    month_names_numeric = ["01","02","03","04","05","06","07","08","09","10","11","12"]

    if cur_trans_date[0].month <=9:
      month = str(cur_trans_date[0].month).zfill(2)
    else:
      month = str(cur_trans_date[0].month)
      
    month_name = month_names_alphabets[month_names_numeric.index(month)]

    self.trans_info_lbl.text = "Current transaction month "+month_name+" "+str(cur_trans_date[0].year)

  def update(self, initial_date):
    # Get the current month and year
    current_month = initial_date.month
    current_year = initial_date.year

    # Move to the next month
    next_month = current_month + 1 if current_month < 12 else 1
    next_year = current_year if current_month < 12 else current_year + 1

    # Calculate the initial date of the next month
    next_initial_date = datetime(next_year, next_month, 1).date()

    # Calculate the number of days in the next month
    if next_month == 2 and calendar.isleap(next_year):
        next_days = 29
    else:
        next_days = calendar.monthrange(next_year, next_month)[1]

    # Calculate the number of Sundays in the next month
    next_num_of_sundays = sum(
        1 for day in range(1, next_days + 1) if datetime(next_year, next_month, day).weekday() == 6
    )

    # Calculate the end date of the next month
    next_end_date = datetime(next_year, next_month, next_days).date()

    return next_initial_date, next_days, next_num_of_sundays, next_end_date

  def update_btn_click(self, **event_args):
    """This method is called when the button is clicked"""
    result = confirm("Do you really want to proceed ?", buttons=["Yes", "No"])
    if result == "Yes":
        initial_date = anvil.server.call('cur_trans_date',gvarb.g_comcode)
        next_initial_date, next_days, next_num_of_sundays, next_end_date = self.update(initial_date[0])
        anvil.server.call('cur_trans_date_update', next_initial_date, next_days, next_num_of_sundays, next_end_date)
        open_form('logform')
    else:
        open_form('menu')

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('update_trans_date')

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    #print(gvarb.g_curmonyear)
    if (gvarb.g_curmonyear == False):
      #print('you can not update')
      result = confirm("You can update to next month only from current month ! ok", buttons=["Yes"])
      open_form('menu')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    value,row = anvil.server.call('check_username_and_password', gvarb.g_username, self.text_box_1.text)
    if value == True:
      self.label_3.visible = False
      self.text_box_1.visible = False
      self.button_2.visible = False
      self.button_3.visible = False
      
      self.trans_info_lbl.visible = True
      self.update_btn.visible = True
      self.button_1.visible = True
    else:
      result = confirm("Invalid crdentials, login again !", buttons=["Yes"])
      if result == "Yes":
        open_form('update_trans_date')

  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if self.text_box_1.text == "":
      Notification("login password cannot be blank").show()
      self.button_2.enabled = False
    else:
      self.button_2.enabled = True

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('update_trans_date')



