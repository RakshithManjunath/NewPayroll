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
from jinja2 import Template
from xhtml2pdf import pisa
from io import BytesIO
from bs4 import BeautifulSoup


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
  #########################################################
  company_data = app_tables.company.search(comp_code='002')
  #########################################################
  # company_data = app_tables.company.search(comp_code=comp_code)
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
  actual_column_names = ['slno', 'trans_empid', 'trans_empname', 'trans_father_husband', 'trans_empsex', 
                           'trans_empdob', 'trans_empdoj', 'trans_emptype', 'trans_deptname', 'trans_desiname', 
                           'trans_emppfc', 'trans_emppfno', 'trans_emp_pfuan', 'trans_empesic', 'trans_empesino', 
                           'trans_empdispensary', 'trans_empptc', 'trans_empitc', 'trans_emppan', 'trans_mandays', 
                           'trans_wo', 'trans_ph', 'trans_layoff', 'trans_absent', 'trans_paid_days', 
                           'trans_othrs', 'trans_inchrs', 'trans_adv', 'trans_tds', 
                           'trans_pfvol', 'trans_lic', 'trans_arr_esipt', 'trans_arr_pf', 'trans_phone_number', 
                           'trans_alt_phone_number', 'trans_email_address', 'trans_aadhar_number', 'trans_attn_bonus', 
                           'trans_earn_attn_bonus', 'fxd_earn_gross', 'earn_pf_salary', 'earn_fpf_salary', 
                           'earn_esi_salary', 'earn_pt_salary', 'earn_ot_salary', 'earn_it_salary', 'earn_bonus_salary', 
                           'pf_amt', 'fpf_amt', 'esi_amt', 'pt_amt', 'ot_amt', 'it_or_tds_amt', 'bonus_amt']
  
  final_selected_records = []
  for record in company_data:
    filtered_row = {}
    for row,columns_to_include in enumerate(company_columns_to_include):
      filtered_row[selected_company_col_data[row]] = record[columns_to_include]
    final_selected_records.append(filtered_row)
  print("Final selected records: ",final_selected_records)
  
  column_names = []
  columns_to_exclude = ['id','trans_date', 'trans_comp_code', 'trans_deptcode', 'trans_desicode','emp_photo',
                       'trans_empbank_code']
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

  columns_after_modifying = column_names.copy()
  print("columns after modifying", columns_after_modifying)


  for index,row in enumerate(columns_after_modifying):
    if row == 'trans_empid':
      columns_after_modifying[index] = 'Emp code'
    elif row == 'trans_empname':
      columns_after_modifying[index] = 'Emp name'
    elif row == 'trans_father_husband':
      columns_after_modifying[index] = 'Father/Husband name'
    elif row == 'trans_empsex':
      columns_after_modifying[index] = 'Gender'
    elif row == 'trans_empdob':
      columns_after_modifying[index] = 'Date of birth'
    elif row == 'trans_empdoj':
      columns_after_modifying[index] = 'Date join'
    elif row == 'trans_emptype':
      columns_after_modifying[index] = 'Emp type'
    elif row == 'trans_deptname':
      columns_after_modifying[index] = 'Department' 
    elif row == 'trans_desiname':
      columns_after_modifying[index] = 'Designation' 
    elif row == 'trans_emppfc':
      columns_after_modifying[index] = 'PF contri' 
    elif row == 'trans_emppfno':
      columns_after_modifying[index] = 'PF No' 
    elif row == 'trans_emp_pfuan':
      columns_after_modifying[index] = 'PF UAN' 
    elif row == 'trans_empesic':
      columns_after_modifying[index] = 'ESI contri' 
    elif row == 'trans_empesino':
      columns_after_modifying[index] = 'ESI number' 
    elif row == 'trans_empdispensary':
      columns_after_modifying[index] = 'Dispensary name' 
    elif row == 'trans_empptc':
      columns_after_modifying[index] = 'PT contri' 
    elif row == 'trans_empitc':
      columns_after_modifying[index] = 'IT contri' 
    elif row == 'trans_emppan':
      columns_after_modifying[index] = 'PAN' 
    elif row == 'trans_mandays':
      columns_after_modifying[index] = 'Mandays' 
    elif row == 'trans_wo':
      columns_after_modifying[index] = 'Weekly Off' 
    elif row == 'trans_ph':
      columns_after_modifying[index] = 'Paid Holiday' 
    elif row == 'trans_layoff':
      columns_after_modifying[index] = 'Lay Off' 
    elif row == 'trans_absent':
      columns_after_modifying[index] = 'Absent' 
    elif row == 'trans_paid_days':
      columns_after_modifying[index] = 'Paid days' 
    elif row == 'trans_othrs':
      columns_after_modifying[index] = 'OT Hrs' 
    elif row == 'trans_inchrs':
      columns_after_modifying[index] = 'Incentive Hrs' 
    elif row == 'trans_adv':
      columns_after_modifying[index] = 'Advance' 
    elif row == 'trans_tds':
      columns_after_modifying[index] = 'TDS' 
    elif row == 'trans_pfvol':
      columns_after_modifying[index] = 'PF Voluantary' 
    elif row == 'trans_lic':
      columns_after_modifying[index] = 'LIC' 
    elif row == 'trans_arr_esipt':
      columns_after_modifying[index] = 'Arrears esi pt' 
    elif row == 'trans_arr_pf':
      columns_after_modifying[index] = 'Arrears pf' 
    elif row == 'trans_phone_number':
      columns_after_modifying[index] = 'Phone number' 
    elif row == 'trans_alt_phone_number':
      columns_after_modifying[index] = 'Alt Phone number' 
    elif row == 'trans_email_address':
      columns_after_modifying[index] = 'Email address' 
    elif row == 'trans_aadhar_number':
      columns_after_modifying[index] = 'Aadhar number' 
    elif row == 'trans_attn_bonus':
      columns_after_modifying[index] = 'Attn bonus' 
    elif row == 'trans_earn_attn_bonus':
      columns_after_modifying[index] = 'Attn bonus earned' 
    elif row == 'fxd_earn_gross':
      columns_after_modifying[index] = 'Fixed Gross'   
    elif row == 'earn_pf_salary':
      columns_after_modifying[index] = 'PF salary'   
    elif row == 'earn_fpf_salary':
      columns_after_modifying[index] = 'FPF salary'   
    elif row == 'earn_esi_salary':
      columns_after_modifying[index] = 'ESI salary'   
    elif row == 'earn_esi_salary':
      columns_after_modifying[index] = 'ESI salary'   
    elif row == 'earn_pt_salary':
      columns_after_modifying[index] = 'PT salary'   
    elif row == 'earn_ot_salary':
      columns_after_modifying[index] = 'OT salary'   
    elif row == 'earn_it_salary':
      columns_after_modifying[index] = 'IT salary'   
    elif row == 'earn_bonus_salary':
      columns_after_modifying[index] = 'Bonus salary'   
    elif row == 'pf_amt':
      columns_after_modifying[index] = 'PF Amt'   
    elif row == 'fpf_amt':
      columns_after_modifying[index] = 'FPF Amt'   
    elif row == 'esi_amt':
      columns_after_modifying[index] = 'ESI Amt'   
    elif row == 'pt_amt':
      columns_after_modifying[index] = 'PT Amt'   
    elif row == 'ot_amt':
      columns_after_modifying[index] = 'OT Amt'   
    elif row == 'it_or_tds_amt':
      columns_after_modifying[index] = 'TDS repeated'   
    elif row == 'bonus_amt':
      columns_after_modifying[index] = 'Bonus Amt'   
    elif row == 'trans_empbank':
      columns_after_modifying[index] = 'Bank'
    elif row == 'trans_empbank_ifsc':
      columns_after_modifying[index] = 'IFSC'
    elif row == 'trans_empbank_acno':
      columns_after_modifying[index] = 'Account no'

  
  # column_names.insert(0,'Sl no')
  unmodified_cols.insert(0,'Sl no')

  columns_after_modifying.insert(0, 'Sl no')

  return columns_after_modifying,unmodified_cols
  
  # return column_names, unmodified_cols

@anvil.server.callable
def get_only_selected_trans_values(trans_comp_code,selected_list,modified_col_names):
  trans_records = app_tables.transaction.search(trans_comp_code=trans_comp_code)
  final_filter_records = []
  for record in trans_records:
    filtered_row = {}
    for selected_col in selected_list:
      if selected_col == "trans_earn1":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees
      elif selected_col == "trans_earn2":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees 
      elif selected_col == "trans_earn3":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees
      elif selected_col == "trans_earn4":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees
      elif selected_col == "trans_earn5":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees 
      elif selected_col == "trans_earn6":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees
      elif selected_col == "trans_earn7":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees
      elif selected_col == "trans_earn8":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees
      elif selected_col == "trans_earn9":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees 
      elif selected_col == "trans_earn10":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees   

      elif selected_col == "trans_earn_earn1":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees       
      elif selected_col == "trans_earn_earn2":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees 
      elif selected_col == "trans_earn_earn3":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees
      elif selected_col == "trans_earn_earn4":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees
      elif selected_col == "trans_earn_earn5":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees 
      elif selected_col == "trans_earn_earn6":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees
      elif selected_col == "trans_earn_earn7":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees
      elif selected_col == "trans_earn_earn8":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees
      elif selected_col == "trans_earn_earn9":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees 
      elif selected_col == "trans_earn_earn10":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees 

      elif selected_col == "trans_ded1":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees       
      elif selected_col == "trans_ded2":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees 
      elif selected_col == "trans_ded3":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees
      elif selected_col == "trans_ded4":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees  

      elif selected_col == "trans_loan1":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees       
      elif selected_col == "trans_loan2":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees   

      elif selected_col == "trans_attn_bonus":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees       
      elif selected_col == "trans_earn_attn_bonus":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees  

      elif selected_col == "fxd_earn_gross":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees       
      elif selected_col == "earn_pf_salary":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees 
      elif selected_col == "earn_fpf_salary":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees 
      elif selected_col == "earn_esi_salary":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees
      elif selected_col == "earn_pt_salary":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees      
      elif selected_col == "earn_ot_salary":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees  
      elif selected_col == "earn_it_salary":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees  
      elif selected_col == "earn_bonus_salary":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees  

      elif selected_col == "trans_adv":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees      
      elif selected_col == "trans_tds":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees  
      elif selected_col == "trans_pfvol":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees 
      elif selected_col == "trans_lic":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees
      elif selected_col == "trans_arr_esipt":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees      
      elif selected_col == "trans_arr_pf":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees 

      elif selected_col == "pf_amt":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees
      elif selected_col == "fpf_amt":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees  
      elif selected_col == "esi_amt":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees 
      elif selected_col == "pt_amt":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees 
      elif selected_col == "ot_amt":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees       
      elif selected_col == "it_or_tds_amt":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees 
      elif selected_col == "bonus_amt":
        formatted_rupees = "₹ {:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_rupees        
        
      elif selected_col == "trans_empdob":
        print("converted_date",record[selected_col].strftime("%d/%m/%Y"))
        filtered_row[selected_col] = record[selected_col].strftime("%d/%m/%Y")
      elif selected_col == "trans_empdoj":
        print("converted_date",record[selected_col].strftime("%d/%m/%Y"))
        filtered_row[selected_col] = record[selected_col].strftime("%d/%m/%Y")
        
      elif selected_col == "trans_mandays":
        formatted_only_2decimal = "{:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_only_2decimal  
      elif selected_col == "trans_wo":
        formatted_only_2decimal = "{:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_only_2decimal  
      elif selected_col == "trans_ph":
        formatted_only_2decimal = "{:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_only_2decimal  
      elif selected_col == "trans_layoff":
        formatted_only_2decimal = "{:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_only_2decimal 
      elif selected_col == "trans_absent":
        formatted_only_2decimal = "{:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_only_2decimal 
      elif selected_col == "trans_leave1":
        formatted_only_2decimal = "{:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_only_2decimal 
      elif selected_col == "trans_leave2":
        formatted_only_2decimal = "{:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_only_2decimal 
      elif selected_col == "trans_leave3":
        formatted_only_2decimal = "{:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_only_2decimal         
      elif selected_col == "trans_paid_days":
        formatted_only_2decimal = "{:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_only_2decimal    
      elif selected_col == "trans_othrs":
        formatted_only_2decimal = "{:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_only_2decimal 
      elif selected_col == "trans_inchrs":
        formatted_only_2decimal = "{:,.2f}".format(record[selected_col])
        filtered_row[selected_col] = formatted_only_2decimal 

      elif selected_col == "trans_phone_number":
        formatted_only_nodecimal = " - ".format(record[selected_col])
        filtered_row[selected_col] = formatted_only_nodecimal 
      elif selected_col == "trans_alt_phone_number":
        formatted_only_nodecimal = " - ".format(record[selected_col])
        filtered_row[selected_col] = formatted_only_nodecimal 
      elif selected_col == "trans_email_address":
        formatted_only_nodecimal = " - ".format(record[selected_col])
        filtered_row[selected_col] = formatted_only_nodecimal
      elif selected_col == "trans_aadhar_number":
        formatted_only_nodecimal = " - ".format(record[selected_col])
        filtered_row[selected_col] = formatted_only_nodecimal
      
      elif selected_col == "Sl no":
        pass
      else:
        filtered_row[selected_col] = record[selected_col]
    final_filter_records.append(filtered_row)
  sl_count = 1
  for row in final_filter_records:
    row['Sl no'] = sl_count
    sl_count+=1
  print("final filer records: ",final_filter_records)

  final_filtered_cols_modified = []
  for selected_col in selected_list:
    index = selected_list.index(selected_col)
    print(index, selected_col)
    # print(index, modified_col_names[index])
    filtered_col = {}
    if selected_col == "Sl no":
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 75
      final_filtered_cols_modified.append(filtered_col)
    elif selected_col == "trans_empid":
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 150
      final_filtered_cols_modified.append(filtered_col)
    elif selected_col == 'trans_empname':
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 250
      final_filtered_cols_modified.append(filtered_col)
    elif selected_col == 'trans_father_husband':
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 250
      final_filtered_cols_modified.append(filtered_col)
    elif selected_col == 'trans_empsex':
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 100
      final_filtered_cols_modified.append(filtered_col)
    elif selected_col == 'trans_empdob':
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 125
      final_filtered_cols_modified.append(filtered_col)
    elif selected_col == 'trans_empdoj':
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 125
      final_filtered_cols_modified.append(filtered_col)
    elif selected_col == 'trans_emptype':
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 100
      final_filtered_cols_modified.append(filtered_col)
    elif selected_col == 'trans_deptname':
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 250
      final_filtered_cols_modified.append(filtered_col)
    elif selected_col == 'trans_desiname':
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 250
      final_filtered_cols_modified.append(filtered_col)
    elif selected_col == 'trans_emppfc':
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 75
      final_filtered_cols_modified.append(filtered_col)
    elif selected_col == 'trans_emppfno':
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 100
      final_filtered_cols_modified.append(filtered_col)
    elif selected_col == 'trans_emp_pfuan':
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 100
      final_filtered_cols_modified.append(filtered_col)      
    elif selected_col == 'trans_empesic':
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 75
      final_filtered_cols_modified.append(filtered_col)    
    elif selected_col == 'trans_empesino':
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 100
      final_filtered_cols_modified.append(filtered_col) 
    elif selected_col == 'trans_empdispensary':
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 150
      final_filtered_cols_modified.append(filtered_col) 
    elif selected_col == 'trans_empptc':
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 75
      final_filtered_cols_modified.append(filtered_col)   
    elif selected_col == 'trans_empitc':
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 75
      final_filtered_cols_modified.append(filtered_col)  
    elif selected_col == 'trans_emppan':
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 100
      final_filtered_cols_modified.append(filtered_col)  
    elif selected_col == 'trans_phone_number':
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 150
      final_filtered_cols_modified.append(filtered_col)  
    elif selected_col == 'trans_alt_phone_number':
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 150
      final_filtered_cols_modified.append(filtered_col)  
    elif selected_col == 'trans_email_address':
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 200
      final_filtered_cols_modified.append(filtered_col)
    elif selected_col == 'trans_aadhar_number':
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 200
      final_filtered_cols_modified.append(filtered_col)
    else:
      filtered_col['id'] =  selected_col
      filtered_col['title'] = modified_col_names[index].upper()
      filtered_col['data_key'] = selected_col
      filtered_col['width'] = 150
      final_filtered_cols_modified.append(filtered_col)


  
  print("final filtered cols modified: ", final_filtered_cols_modified)
  
  # return final_filter_records,final_filtered_cols
  return final_filter_records,final_filtered_cols_modified

@anvil.server.callable
def pt_recovery_html_report(html_template,grid_rows,grid_cols):
  template = Template(html_template)
    
  # Provide data to fill the placeholders
  data = {'grid_rows':grid_rows, 'grid_cols':grid_cols}
  
  # Render the HTML with the data
  html_content = template.render(data)
  print("html content",html_content)
  return html_content

@anvil.server.callable
def download_pt_recovery_pdf(html_content):
  # Create a file-like buffer to receive PDF data
  buffer = BytesIO()
  
  # Convert HTML to PDF
  pisa.CreatePDF(html_content, dest=buffer)
  
  # Retrieve the PDF content from the buffer
  pdf_data = buffer.getvalue()
  
  # Close the buffer
  buffer.close()
  
  # Save the PDF to a file or return it as needed
  with open("output.pdf", "wb") as output_file:
      output_file.write(pdf_data)

  pdf_media = anvil.media.from_file('output.pdf', 'application/pdf', 'output.pdf')
  return pdf_media

@anvil.server.callable
def download_pt_recovery_excel(html_content):
  # Parse the HTML content
  soup = BeautifulSoup(html_content, 'html.parser')
  
  # Extract data from the HTML table
  data = []
  table = soup.find('table')
  for row in table.find_all('tr'):
      columns = row.find_all(['th', 'td'])
      data.append([column.get_text(strip=True) for column in columns])
  
  # Create a pandas DataFrame from the extracted data
  df = pd.DataFrame(data)
  
  # Export the DataFrame to an Excel file
  df.to_excel('output.xlsx', index=False, header=False)

  pdf_media = anvil.media.from_file('output.xlsx', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'output.xlsx')
  return pdf_media