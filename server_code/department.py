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
############### Add department ############
######### auto increment 'dept_id' column ###########
@anvil.server.callable
def next_dept_id_value():
  # Get the last row of the data table
  next_value = '0000000001'
  try:
    dept_id_list = [(r["dept_id"]) for r in app_tables.department.search()]
    last_row = dept_id_list[-1]
    last_string_value = last_row
    next_value = str(int(last_string_value) + 1).zfill(10)
  except IndexError:
    next_value == '0000000001'
  return next_value

@anvil.server.callable
def dept_get_next_string_value():
  # Get the last row of the data table
  next_value = '001'
  try:
    dept_code_list = [(r["dept_code"]) for r in app_tables.department.search()]
    last_row = dept_code_list[-1]
    last_string_value = last_row
    next_value = str(int(last_string_value) + 1).zfill(3)
  except IndexError:
    next_value == '001'
  return next_value

@anvil.server.callable
def dept_add(dept_id,deptcode,deptname,comcode):
  app_tables.department.add_row(dept_id=dept_id,dept_code=deptcode,
                          dept_name=deptname,dept_comp_code=comcode)

#################### Department Change #################################
#################### same function is used also in emp_add #############
@anvil.server.callable
def dept_change_name_and_code(dept_comp_code):
  dept_details = []
  for r in app_tables.department.search(dept_comp_code=dept_comp_code):
    dept_details.append(r['dept_code'] + " | "  +r['dept_name'])
  return dept_details

@anvil.server.callable
def dept_update_row(deptcode,deptname):
  row = app_tables.department.get(dept_code=deptcode)
  row.update(dept_name=deptname)

@anvil.server.callable
def dept_name_exists(dept_name,dept_comp_code):
  row = app_tables.department.search(dept_name=dept_name,dept_comp_code=dept_comp_code)
  if any(row):
    return False
  else:
    return True
  
