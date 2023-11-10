from ._anvil_designer import comp_newTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime,date
import calendar

class comp_new(comp_newTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def update(self, initial_date):
    # Get the current month and year
    current_month = initial_date.month
    current_year = initial_date.year

    # Calculate the number of days in the next month
    if current_month == 2 and calendar.isleap(current_year):
        current_days = 29
    else:
        current_days = calendar.monthrange(current_year, current_month)[1]

    # Calculate the number of Sundays in the next month
    num_of_sundays = sum(
        1 for day in range(1, current_days + 1) if datetime(current_year, current_month, day).weekday() == 6
    )

    # Calculate the end date of the next month
    end_date = datetime(current_year, current_month, current_days).date()

    return current_days, num_of_sundays, end_date

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    #anvil.users.login_with_form()
    open_form('pass_add')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.text_box_1.text == "":
      Notification("Company name cannot be blank").show()
    else:
      # id= anvil.server.call('comp_get_next_string_value')
      # compcode= anvil.server.call('next_comp_id_value')
      # row = anvil.server.call('new_comp_add',id,compcode, self.text_box_1.text)
      # anvil.server.call('comp_default_values',row)
      # Notification(self.text_box_1.text + " data added successfully").show()
      self.clear_inputs() 

    newdate = self.date_picker_1.date
    modified_new_date = date(newdate.year,newdate.month, 1)
    
    start_date = modified_new_date
    print("start date: ", start_date)

    current_days, num_of_sundays, end_date = self.update(start_date)
    print("current days: " + str(current_days))
    print("Num of sundays: " + str(num_of_sundays))
    print("end date: ", end_date)
    anvil.server.call('new_trans_date', start_date,current_days,num_of_sundays,end_date,compcode)
    #open_form('logform')
###########################################################################
###########################################################################
###########################################################################
    if self.text_box_2.text == "":
      Notification("User name cannot be blank").show()
    else:
      self.passid= anvil.server.call('pass_get_next_string_value')
      self.passcode= anvil.server.call('next_pass_code_value')
      
      is_duplicate = anvil.server.call('duplicate_username_password_check', self.text_box_2.text,self.text_box_3.text)
      if is_duplicate:  
        print("Username and password exists")
        is_duplicate = confirm(" Username and password already exist, try different username and password  ! ok ", buttons=["Yes"])
        if is_duplicate == "Yes":
            open_form('comp_new')
      else:
        print("Username and password doesnt exist")
        self.passbool = True
        # row = anvil.server.call('pass_add',id,passcode, self.text_box_2.text,
        #                 self.text_box_3.text,compcode)
        #anvil.server.call('comp_default_values',row)
        if  ((self.text_box_3.text ) == (self.text_box_4.text )):
          result = confirm(self.text_box_1.text+"Company added successfully ! continue to login  ?", buttons=["Yes"])
          if result == "Yes":
            self.clear_inputs()
            open_form('logform')
        else:
          result = confirm(" Password re-confirmation failed !  ", buttons=["Yes"])
          if result == "Yes":
            self.clear_inputs()
            open_form('logform')

  
    
  def clear_inputs(self):
    # Clear our three text boxes
    self.text_box_2.text = ""
    self.text_box_3.text = ""
    self.text_box_4.text = ""
###########################################################################
###########################################################################
###########################################################################
  
  def clear_inputs(self):
    # Clear our three text boxes
    self.text_box_1.text = ""

  def text_box_1_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.text_box_1.text = self.text_box_1.text.upper()
    if ((self.text_box_1.text) and (self.text_box_2.text ) and (self.text_box_3.text ) and (self.text_box_4.text )):
      self.button_1.enabled = True 
    else:
      self.button_1.enabled = False  

  def text_box_2_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.text_box_2.text = self.text_box_2.text.upper()
    if ((self.text_box_1.text) and (self.text_box_2.text ) and (self.text_box_3.text ) and (self.text_box_4.text )):
      self.button_1.enabled = True 
    else:
      self.button_1.enabled = False  

  def text_box_4_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if ((self.text_box_1.text) and (self.text_box_2.text ) and (self.text_box_3.text ) and (self.text_box_4.text )):
      self.button_1.enabled = True 
    else:
      self.button_1.enabled = False  

  def text_box_3_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    if ((self.text_box_1.text) and (self.text_box_2.text ) and (self.text_box_3.text ) and (self.text_box_4.text )):
      self.button_1.enabled = True 
    else:
      self.button_1.enabled = False  

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')

  def date_picker_1_change(self, **event_args):
    """This method is called when the selected date changes"""
    newdate = self.date_picker_1.date
    print(newdate)
    newmonth= newdate.strftime("%B").upper()
    newyear= newdate.strftime("%Y")    
    print(newmonth)
    print(newyear)
    print(newdate, type(newdate))
    modified_new_date = date(newdate.year,newdate.month, 1)
    print(modified_new_date)










