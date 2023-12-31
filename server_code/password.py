import anvil.files
from anvil.files import data_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import bcrypt 
import base64

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
############### Add password ############
######### auto increment 'pass_id' column ###########
@anvil.server.callable
def pass_get_next_string_value():
  # Get the last row of the data table
  next_value = '0000000001'
  try:
    pass_id_list = [(r["pass_id"]) for r in app_tables.password.search()]
    last_row = pass_id_list[-1]
    last_string_value = last_row
    next_value = str(int(last_string_value) + 1).zfill(10)
  except IndexError:
    next_value == '0000000001'
  return next_value

@anvil.server.callable
def next_pass_code_value():
  # Get the last row of the data table
  next_value = '001'
  try:
    pass_code_list = [(r["pass_code"]) for r in app_tables.password.search()]
    last_row = pass_code_list[-1]
    last_string_value = last_row
    next_value = str(int(last_string_value) + 1).zfill(3)
  except IndexError:
    next_value == '001'
  return next_value

@anvil.server.callable
def pass_add(pass_id,passcode,username,passwrd,comcode):
  hashed_password = bcrypt.hashpw(passwrd.encode('utf-8'), bcrypt.gensalt())
  hashed_password_str = base64.b64encode(hashed_password).decode('utf-8')
  return app_tables.password.add_row(pass_id=pass_id,
                                     pass_code=passcode,
                                    username=username,
                                     password=hashed_password_str,
                                     pass_comp_code=comcode)

@anvil.server.callable
def check_username_and_password(username, password):
  row = app_tables.password.get(username=username)
  if row:
    #print(f"User {username} exists")
    hashed_password = base64.b64decode(row['password'].encode('utf-8'))
    decrypted_password = bcrypt.checkpw(password.encode('utf-8'), hashed_password)
    #print("actual password", password)
    #print("hashed password", hashed_password)
    #print("decrypted password", decrypted_password)
    if decrypted_password:
      #print(f"Correct password for {username}")
      return True, row['pass_comp_code']
    else:
      #print(f"Incorrect password for {username}")
      return False,False
  else:
    #print(f"User {username} doesn't exist")
    return False,False
  # password_table = app_tables.password.search()
  # db_username, db_password = password[username], password_table[password]

@anvil.server.callable
def check_password_and_confirm_password(username, password):
  return app_tables.password.search()

@anvil.server.callable
def duplicate_username_password_check(username,password):
  row = app_tables.password.get(username=username)
  compare_password = False
  if row:
    hashed_password = base64.b64decode(row['password'].encode('utf-8'))
    compare_password = bcrypt.checkpw(password.encode('utf-8'), hashed_password)
    #print("Compare password", compare_password)
    return compare_password
  return compare_password
  # return len(existing_records) > 0