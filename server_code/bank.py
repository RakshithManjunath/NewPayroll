import anvil.files
from anvil.files import data_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
############### Add Bank ############
######### auto increment 'bank_id' column ###########
@anvil.server.callable
def bank_get_next_string_value():
  # Get the last row of the data table
  next_value = '0000000001'
  try:
    bank_id_list = [(r["bank_id"]) for r in app_tables.bank.search()]
    last_row = bank_id_list[-1]
    last_string_value = last_row
    next_value = str(int(last_string_value) + 1).zfill(10)
  except IndexError:
    next_value == '0000000001'
  return next_value

@anvil.server.callable
def next_bank_id_value():
  # Get the last row of the data table
  next_value = '001'
  try:
    bank_code_list = [(r["bank_code"]) for r in app_tables.bank.search()]
    last_row = bank_code_list[-1]
    last_string_value = last_row
    next_value = str(int(last_string_value) + 1).zfill(3)
  except IndexError:
    next_value == '001'
  return next_value

@anvil.server.callable
def bank_add(bank_id,bankcode,bankname,bankadd1,bankadd2,bankadd3,bankifsc,comcode):
  return app_tables.bank.add_row(bank_id=bank_id,bank_code=bankcode,
                          bank_name=bankname,bank_addr1=bankadd1,bank_addr2=bankadd2,
                         bank_addr3=bankadd3,bank_ifsc=bankifsc,bank_comp_code=comcode)

def get_default_value_for_type(column_type):
  # Define default values based on column types (you can customize this)
  if column_type == 'text':
      return ''
  elif column_type == 'number':
      return 0
  elif column_type == 'date':
      return date(2000, 1, 1)  # Current UTC date and time
  elif column_type == 'true/false':
      return False
  return None

@anvil.server.callable
def bank_default_values(row):
  columns_and_types = {
  'bank_addr1':'text',  
  'bank_addr2':'text',  
  'bank_addr3':'text',
  'bank_ifsc': 'text',
  }

  for column_name, column_type in columns_and_types.items():
    print(column_name, column_type)
    if row[column_name] is None:
      print(row[column_name])
      default_value = get_default_value_for_type(column_type)
      row[column_name] = default_value
      
#################### Bank Change #################################
#################### same function is used also in emp_bank_add #############
@anvil.server.callable
def bank_change_name_and_code(bank_comp_code):
  bank_details = []
  for r in app_tables.bank.search(bank_comp_code=bank_comp_code):
    bank_details.append(r['bank_code'] + " | "  +r['bank_name'])
  return bank_details

@anvil.server.callable
def bank_get_details(bankcode):
  row = app_tables.bank.get(bank_code=bankcode)
  return row

@anvil.server.callable
def bank_update(bank_code, bank_addr1,bank_addr2,bank_addr3,bank_ifsc,bank_name):
  row = app_tables.bank.get(bank_code=bank_code)
  row.update(bank_addr1=bank_addr1,
             bank_addr2=bank_addr2,
             bank_addr3=bank_addr3,
             bank_ifsc=bank_ifsc,
             bank_name=bank_name)


@anvil.server.callable
def bank_ifsc_exists(bank_ifsc):
  bank_ifsc_list = [(r["bank_ifsc"]) for r in app_tables.bank.search()]
  if bank_ifsc in bank_ifsc_list:
    return True
  else:
    return False

@anvil.server.callable
def bank_name_exists(bank_name,bank_comp_code):
  row = app_tables.bank.search(bank_name=bank_name,bank_comp_code=bank_comp_code)
  if any(row):
    return False
  else:
    return True