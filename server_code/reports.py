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
  # filtered_columns = [{'id': 'Sl no', 'title': 'Sl no', 'data_key': 'Sl no', 'width': 100},
  #                     {'id': 'trans_empid', 'title': 'Employee code', 'data_key': 'trans_empid', 'width': 100},
  #                     {'id': 'trans_empname', 'title': 'Employee name', 'data_key': 'trans_empname', 'width': 200},
  #                     {'id': 'trans_emppfno', 'title': 'PF number', 'data_key': 'trans_emppfno', 'width': 100},
  #                     {'id': 'trans_emp_pfuan', 'title': 'PF UAN', 'data_key': 'trans_emp_pfuan', 'width': 100},
  #                     {'id': 'earn_pf_salary', 'title': 'PF salary [ ₹ ]', 'data_key': 'earn_pf_salary', 'width': 100},
  #                     {'id': 'pf_amt', 'title': 'Employeee PF Amt [ ₹ ]', 'data_key': 'pf_amt', 'width': 100},
  #                     {'id': 'emp_pf_amt', 'title': 'Employeee FPF Amt [ ₹ ]', 'data_key': 'emp_pf_amt', 'width': 100}, 
  #                     {'id': 'empr_pf_amt', 'title': 'Employer PF Amt [ ₹ ]', 'data_key': 'empr_pf_amt', 'width': 100},
  #                     {'id': 'fpf_amt', 'title': 'Employer FPF Amt [ ₹ ]', 'data_key': 'fpf_amt', 'width': 100},   
  #                     {'id': 'trans_pfvol', 'title': 'Employeee PF Voluntary Amt [ ₹ ]', 'data_key': 'trans_pfvol', 'width': 100},                      
  #                     {'id': 'Total', 'title': 'Total Amount [ ₹ ]', 'data_key': 'Total', 'width': 100}]

  filtered_columns = [{'id': 'Sl no', 'title': 'Sl no', 'data_key': 'Sl no'},
                      {'id': 'trans_empid', 'title': 'Employee code', 'data_key': 'trans_empid'},
                      {'id': 'trans_empname', 'title': 'Employee name', 'data_key': 'trans_empname'},
                      {'id': 'trans_emppfno', 'title': 'PF number', 'data_key': 'trans_emppfno'},
                      {'id': 'trans_emp_pfuan', 'title': 'PF UAN', 'data_key': 'trans_emp_pfuan'},
                      {'id': 'earn_pf_salary', 'title': 'PF salary [ ₹ ]', 'data_key': 'earn_pf_salary'},
                      {'id': 'pf_amt', 'title': 'Employeee PF Amt [ ₹ ]', 'data_key': 'pf_amt'},
                      {'id': 'emp_pf_amt', 'title': 'Employeee FPF Amt [ ₹ ]', 'data_key': 'emp_pf_amt'}, 
                      {'id': 'empr_pf_amt', 'title': 'Employer PF Amt [ ₹ ]', 'data_key': 'empr_pf_amt'},
                      {'id': 'fpf_amt', 'title': 'Employer FPF Amt [ ₹ ]', 'data_key': 'fpf_amt'},   
                      {'id': 'trans_pfvol', 'title': 'Employeee PF Voluntary Amt [ ₹ ]', 'data_key': 'trans_pfvol'},                      
                      {'id': 'Total', 'title': 'Total Amount [ ₹ ]', 'data_key': 'Total'}]

  
  rows = app_tables.transaction.search(trans_comp_code=trans_comp_code)
  filtered_rows = []
  for count,row in enumerate(rows):
    new_dict = {'Sl no':count +1,
                'trans_empid':row['trans_empid'],
                'trans_empname':row['trans_empname'],
                'trans_emppfno':row['trans_emppfno'],
                'trans_emp_pfuan': row['trans_emp_pfuan'],
                'earn_pf_salary':"{:,.2f}".format(row['earn_pf_salary']),
                'pf_amt':"{:,.2f}".format(row['pf_amt']),
                'fpf_amt':"{:,.2f}".format(row['fpf_amt']),
                'Total':"{:,.2f}".format(row['pf_amt'] +row['fpf_amt'])}
    filtered_rows.append(new_dict)
  
  # Grid rows and columns [{'trans_empid': '001', 'trans_empname': 'RAKS', 'Sl no': 1}, {'trans_empid': '002', 'trans_empname': 'MANJU', 'Sl no': 2}] [{'id': 'Sl no', 'title': 'SL NO', 'data_key': 'Sl no', 'width': 75}, {'id': 'trans_empid', 'title': 'EMP CODE', 'data_key': 'trans_empid', 'width': 150}, {'id': 'trans_empname', 'title': 'EMP NAME', 'data_key': 'trans_empname', 'width': 250}]
  return filtered_rows,filtered_columns

  
  # return rows['trans_empid'], rows['trans_empname'], rows['trans_emppfno'], rows['trans_emp_pfuan'], rows['earn_pf_salary'],rows['pf_amt']

@anvil.server.callable
def pf_recovery_html(html_template,grid_rows,grid_cols,
                     report_head,company_name,
                     addr_line1,addr_line2,addr_line3,
                    summary_heading):
  template = Template(html_template)
    
  # Provide data to fill the placeholders
  data = {'grid_rows':grid_rows,'grid_cols':grid_cols,
          'report_head':report_head,'company_name':company_name,
          'addr_line1':addr_line1,'addr_line2':addr_line2,'addr_line3':addr_line3,
         'summary_heading':summary_heading}
  
  # Render the HTML with the data
  html_content = template.render(data)
  print("html content",html_content)
  return html_content