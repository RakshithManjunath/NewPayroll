import anvil.files
from anvil.files import data_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd
from datetime import datetime,date
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4
from temp_invoice import my_temp # import the template
from invoice_data import *  # get all data required for invoice

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

############ trans change #############
@anvil.server.callable
def trans_change_update(trans_empid,trans_mandays,trans_wo,trans_ph,trans_layoff,trans_absent,
                        trans_leave1,trans_leave2,trans_leave3,trans_othrs,trans_inchrs,
                        trans_ded1,trans_ded2,trans_ded3,trans_ded4,
                        trans_loan1,trans_loan2,
                        trans_adv,trans_tds,trans_pfvol,trans_lic,
                        trans_arr_esipt,trans_arr_pf,trans_paid_days):
  row = app_tables.transaction.get(trans_empid=trans_empid)
  row.update(trans_mandays=trans_mandays,
            trans_wo=trans_wo,
            trans_ph=trans_ph,
            trans_layoff=trans_layoff,
            trans_absent=trans_absent,
            trans_leave1=trans_leave1,
            trans_leave2=trans_leave2,
            trans_leave3=trans_leave3,
            trans_othrs=trans_othrs,
            trans_inchrs=trans_inchrs,
            trans_ded1=trans_ded1,
            trans_ded2=trans_ded2,
            trans_ded3=trans_ded3,
            trans_ded4=trans_ded4,
            trans_loan1=trans_loan1,
            trans_loan2=trans_loan2,
            trans_adv=trans_adv,
            trans_tds=trans_tds,
            trans_pfvol=trans_pfvol,
            trans_lic=trans_lic,
            trans_arr_esipt=trans_arr_esipt,
            trans_arr_pf=trans_arr_pf,
            trans_paid_days=trans_paid_days
            )

@anvil.server.callable
def trans_emp_name_and_code(trans_comp_code):
  emp_details = []
  for r in app_tables.transaction.search(trans_comp_code=trans_comp_code):
    emp_details.append(r['trans_empid'] + " | "  +r['trans_empname'])
  return emp_details

@anvil.server.callable
def trans_emp_get_details(trans_empid):
  row = app_tables.transaction.get(trans_empid=trans_empid)
  return row

@anvil.server.callable
def trans_emp_delete_row(trans_empid,trans_comp_code):
  row = app_tables.transaction.search(trans_empid=trans_empid,trans_comp_code=trans_comp_code)
  row[0].delete()

@anvil.server.callable
def trans_get_all_details(trans_comp_code):
  trans_all_data = app_tables.transaction.search(trans_comp_code=trans_comp_code)
  # df = pd.DataFrame(trans_all_data)
  # columns_and_type = app_tables.transaction.list_columns()
  # column_names = []
  # for column in columns_and_type:
  #   column_names.append(column['name'])
  # df.columns = column_names
  # formatted_date_column = []
  # for record in trans_all_data:
  #   formatted_date = record['trans_empdob'].strftime('%d/%m/%Y')
  #   formatted_date_column.append(formatted_date)
  # df['trans_empdob'] = formatted_date_column
  # print(df, type(trans_all_data))
  # data = df.to_dict(orient='records')
  # return data
  return app_tables.transaction.search(trans_comp_code=trans_comp_code)

@anvil.server.callable
def get_all_companies():
  return app_tables.company.search()

@anvil.server.callable
def get_all_password():
  return app_tables.password.search()

@anvil.server.callable
def get_reportlab_pdf():
  my_path='my_pdf.pdf' 
  c = canvas.Canvas(my_path,pagesize=letter)
  c=my_temp(c) # run the template
  
  c.setFillColorRGB(0,0,1) # font colour
  c.setFont("Helvetica", 20)
  row_gap=0.6 # gap between each row
  line_y=7.9 # location of fist Y position 
  total=0
  employee_data = app_tables.employee.search()
  for row in employee_data:
    c.drawString(0.1*inch,line_y*inch,row['emp_code']) # p Name
    c.drawRightString(2.9*inch,line_y*inch,row['emp_name']) # p Price
    # c.drawRightString(6.7*inch,line_y*inch,str(my_sale[items])) # p Qunt 
    line_y=line_y-row_gap
  
  c.showPage()
  c.save()
  pdf_media = anvil.media.from_file(my_path, 'application/pdf', 'my_pdf.pdf')
  return pdf_media

@anvil.server.callable
def get_transaction_columns(comp_details, comp_code):
  columns_and_type = app_tables.transaction.list_columns()
  # company_data = app_tables.company.search(comp_code='002')
  company_data = app_tables.company.search(comp_code=comp_code)
  company_columns_to_include = ['comp_earn_head1','comp_earn_head2','comp_earn_head3','comp_earn_head4','comp_earn_head5',
                                'comp_earn_head6', 'comp_earn_head7', 'comp_earn_head8', 'comp_earn_head9', 'comp_earn_head10',
                               'comp_ded1','comp_ded2','comp_ded3','comp_ded4',
                                'comp_leave_head1','comp_leave_head2','comp_leave_head3',
                               'comp_loan_head1','comp_loan_head2']
  selected_company_col_data = ['trans_earn1', 'trans_earn2', 'trans_earn3', 'trans_earn4', 'trans_earn5',
                              'trans_earn6', 'trans_earn7', 'trans_earn8', 'trans_earn9', 'trans_earn10',
                              'trans_ded1','trans_ded2','trans_ded3','trans_ded4',
                              'trans_leave1','trans_leave2','trans_leave3',
                              'trans_loan1','trans_loan2']
  final_selected_records = []
  for record in company_data:
    filtered_row = {}
    for row,columns_to_include in enumerate(company_columns_to_include):
      filtered_row[selected_company_col_data[row]] = record[columns_to_include]
    final_selected_records.append(filtered_row)
  print("Final selected records: ",final_selected_records)
  
  column_names = []
  columns_to_exclude = ['id','trans_date', 'trans_comp_code', 'trans_deptcode', 'trans_desicode','emp_photo']
  for column in columns_and_type:
    if column['name'] not in columns_to_exclude:
      column_names.append(column['name'])
  unmodified_cols = column_names.copy()
  
  for key,val in final_selected_records[0].items():
    if val == "":
      new_val = key.split('_')[-1]
      pos = column_names.index(key)
      del key
      column_names[pos] = new_val
    else:
      pos = column_names.index(key)
      column_names[pos] = val

  filtered_columns_for_renaming = {}
  for key, value in final_selected_records[0].items():
    if 'earn' in key:
      filtered_columns_for_renaming[key] = value
  for key, val in filtered_columns_for_renaming.items():
    if val == "":
      new_val = key.split('_')[-1]
      filtered_columns_for_renaming[key] = new_val

  updated_columns = {}
  for key, val in filtered_columns_for_renaming.items():
    key_split_list = key.split('_')
    print("key split list", key_split_list)
    new_key = key_split_list[0] + '_earn_' + key_split_list[-1]
    print("New key", new_key)
    updated_columns[new_key] = "earned" + "_" + val
    
  print("filtered columns after renaming: ",updated_columns)

  for column in column_names:
    for key,val in updated_columns.items():
      if column == key:
        column_names[column_names.index(column)] = val 
  
  return column_names, unmodified_cols

@anvil.server.callable
def get_only_selected_trans_values(trans_comp_code,selected_list,modified_col_names):
  trans_records = app_tables.transaction.search(trans_comp_code=trans_comp_code)
  final_filter_records = []
  for record in trans_records:
    filtered_row = {}
    for selected_col in selected_list:
      filtered_row[selected_col] = record[selected_col]
    final_filter_records.append(filtered_row)
  print("final filer records: ",final_filter_records)

  final_filtered_cols_modified = []
  for selected_col in selected_list:
    index = selected_list.index(selected_col)
    print(index, selected_col)
    print(index, modified_col_names[index])
    filtered_col = {}
    filtered_col['id'] =  selected_col
    filtered_col['title'] = modified_col_names[index].capitalize()
    filtered_col['data_key'] = selected_col
    filtered_col['width'] = 150
    final_filtered_cols_modified.append(filtered_col)

  print("final filtered cols modified: ", final_filtered_cols_modified)
  
  # return final_filter_records,final_filtered_cols
  return final_filter_records,final_filtered_cols_modified

