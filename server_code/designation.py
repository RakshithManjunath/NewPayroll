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
#
############### Add designation ############
######### auto increment 'desi_id' column ###########
@anvil.server.callable
def next_desi_id_value():
  # Get the last row of the data table
  next_value = '0000000001'
  try:
    desi_id_list = [(r["desi_id"]) for r in app_tables.designation.search()]
    last_row = desi_id_list[-1]
    last_string_value = last_row
    next_value = str(int(last_string_value) + 1).zfill(10)
  except IndexError:
    next_value == '0000000001'
  return next_value

@anvil.server.callable
def desi_get_next_string_value():
  # Get the last row of the data table
  next_value = '001'
  try:
    desi_code_list = [(r["desi_code"]) for r in app_tables.designation.search()]
    last_row = desi_code_list[-1]
    last_string_value = last_row
    next_value = str(int(last_string_value) + 1).zfill(3)
  except IndexError:
    next_value == '001'
  return next_value

@anvil.server.callable
def desi_add(desi_id,desicode,desiname,comcode):
  app_tables.designation.add_row(desi_id=desi_id,desi_code=desicode,
                          desi_name=desiname,desi_comp_code=comcode)

#################### Designation Change #################################
#################### same function is used also in emp_add #############
@anvil.server.callable
def desi_change_name_and_code(desi_comp_code):
  desi_details = []
  for r in app_tables.designation.search(desi_comp_code=desi_comp_code):
    desi_details.append(r['desi_code'] + " | "  +r['desi_name'])
  return desi_details

@anvil.server.callable
def desi_update_row(desicode,desiname):
  row = app_tables.designation.get(desi_code=desicode)
  row.update(desi_name=desiname)

@anvil.server.callable
def desi_name_exists(desi_name,desi_comp_code):
  row = app_tables.designation.search(desi_name=desi_name,desi_comp_code=desi_comp_code)
  if any(row):
    return False
  else:
    return True