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

#### anvil file paths ####
department_path = data_files['department.csv'] 
designation_path = data_files['designation.csv']
bank_path = data_files['bank.csv']
password_path = data_files['password.csv']
trans_date_path = data_files['trans_date.csv']
company_path = data_files['company.csv']
employee_path = data_files['employee.csv']
transaction_path = data_files['transaction.csv']
### Other files #######

#### local file paths ####
# department_path = "C:/SALUSER/SQLDATA/department.csv"
# designation_path = "C:/SALUSER/SQLDATA/designation.csv"
# bank_path = "C:/SALUSER/SQLDATA/bank.csv"
# password_path = "C:/SALUSER/SQLDATA/password.csv"
# trans_date_path = "C:/SALUSER/SQLDATA/trans_date.csv"
# company_path = "C:/SALUSER/SQLDATA/company.csv"
# employee_path = "C:/SALUSER/SQLDATA/employee.csv"
# transaction_path = "C:/SALUSER/SQLDATA/transaction.csv"
### Other files #######
