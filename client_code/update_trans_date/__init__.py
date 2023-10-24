from ._anvil_designer import update_trans_dateTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import calendar
from datetime import datetime

class update_trans_date(update_trans_dateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.label_2.text = gvarb.g_comname+' '+gvarb.g_mode+" for the month of "+gvarb.g_transdate.strftime("%B %Y")

    cur_trans_date = anvil.server.call('cur_trans_date')

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
        initial_date = anvil.server.call('cur_trans_date')
        next_initial_date, next_days, next_num_of_sundays, next_end_date = self.update(initial_date[0])
        anvil.server.call('cur_trans_date_update', next_initial_date, next_days, next_num_of_sundays, next_end_date)
        anvil.users.logout()
        open_form('menu')
    else:
        open_form('menu')

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('update_trans_date')



