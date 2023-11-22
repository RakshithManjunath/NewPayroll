import anvil.files
from anvil.files import data_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from jinja2 import Template

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

@anvil.server.callable
def pf_recovery_report(trans_comp_code):
  # rows = app_tables.transaction.get(trans_comp_code=trans_comp_code)
  # app_tables.transaction.list_columns()
  filtered_columns = [{'id': 'trans_empid', 'title': 'Employee code', 'data_key': 'trans_empid', 'width': 100},
                      {'id': 'trans_empname', 'title': 'Employee name', 'data_key': 'trans_empname', 'width': 200},
                      {'id': 'trans_emppfno', 'title': 'Employee pf number', 'data_key': 'trans_emppfno', 'width': 100},
                      {'id': 'trans_emp_pfuan', 'title': 'Employee pf uan', 'data_key': 'trans_emp_pfuan', 'width': 100},
                      {'id': 'earn_pf_salary', 'title': 'Employee pf sal', 'data_key': 'earn_pf_salary', 'width': 100},
                      {'id': 'pf_amt', 'title': 'Employee pf amount', 'data_key': 'pf_amt', 'width': 100}]
  return filtered_columns

  
  # return rows['trans_empid'], rows['trans_empname'], rows['trans_emppfno'], rows['trans_emp_pfuan'], rows['earn_pf_salary'],rows['pf_amt']

@anvil.server.callable
def pf_recovery_html(html_template,grid_cols):
  template = Template(html_template)
    
  # Provide data to fill the placeholders
  data = {'grid_cols':grid_cols}
  
  # Render the HTML with the data
  html_content = template.render(data)
  print("html content",html_content)
  return html_content