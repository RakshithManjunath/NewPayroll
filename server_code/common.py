import anvil.files
from anvil.files import data_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd
from datetime import datetime,date
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
def get_transaction_columns(comp_details, comp_code):
  columns_and_type = app_tables.transaction.list_columns()
  #########################################################
  #company_data = app_tables.company.search(comp_code='002')
  #########################################################
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
                           'pf_amt', 'fpf_amt', 'esi_amt', 'pt_amt', 'ot_amt', 'it_or_tds_amt', 'bonus_amt','trans_empbank_code',
                           'trans_empbank','trans_empbank_acno','trans_empbank_ifsc','trans_emp_otc','trans_emp_otrate',
                           'trans_emp_incrate']
  
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

  emp_details_list = []
  general_details_list = []
  earnings_list = []
  attendance_list = []
  extra_hours_list = []
  deductions_list = []
  for index,row in enumerate(columns_after_modifying):
    if row == 'trans_empid':
      columns_after_modifying[index] = 'Emp code'
      emp_details_list.append('Emp code')
    elif row == 'trans_empname':
      columns_after_modifying[index] = 'Emp name'
      emp_details_list.append('Emp name')
      
    elif row == 'trans_father_husband':
      columns_after_modifying[index] = 'Father/Husband name'
      general_details_list.append('Father/Husband name')
    elif row == 'trans_empsex':
      columns_after_modifying[index] = 'Gender'
      general_details_list.append('Gender')
    elif row == 'trans_empdob':
      columns_after_modifying[index] = 'Date of birth'
      general_details_list.append('Date of birth')
    elif row == 'trans_empdoj':
      columns_after_modifying[index] = 'Date join'
      general_details_list.append('Date join')
    elif row == 'trans_emptype':
      columns_after_modifying[index] = 'Emp type'
      general_details_list.append('Emp type')  
    elif row == 'trans_deptname':
      columns_after_modifying[index] = 'Department'
      general_details_list.append('Department')  
    elif row == 'trans_desiname':
      columns_after_modifying[index] = 'Designation'
      general_details_list.append('Designation')  
    elif row == 'trans_emppfc':
      columns_after_modifying[index] = 'PF contri' 
      general_details_list.append('PF contri')  
    elif row == 'trans_emppfno':
      columns_after_modifying[index] = 'PF No' 
      general_details_list.append('PF No')  
    elif row == 'trans_emp_pfuan':
      columns_after_modifying[index] = 'PF UAN' 
      general_details_list.append('PF UAN')  
    elif row == 'trans_empesic':
      columns_after_modifying[index] = 'ESI contri' 
      general_details_list.append('ESI contri')  
    elif row == 'trans_empesino':
      columns_after_modifying[index] = 'ESI number' 
      general_details_list.append('ESI contri')  
    elif row == 'trans_empdispensary':
      columns_after_modifying[index] = 'Dispensary name'
      general_details_list.append('Dispensary name')  
    elif row == 'trans_empptc':
      columns_after_modifying[index] = 'PT contri' 
      general_details_list.append('PT contri')  
    elif row == 'trans_empitc':
      columns_after_modifying[index] = 'IT contri'
      general_details_list.append('IT contri')  
    elif row == 'trans_emppan':
      columns_after_modifying[index] = 'PAN'
      general_details_list.append('PAN')  
    elif row == 'trans_phone_number':
      columns_after_modifying[index] = 'Phone number' 
      general_details_list.append('Phone number')  
    elif row == 'trans_alt_phone_number':
      columns_after_modifying[index] = 'Alt Phone number' 
      general_details_list.append('Alt Phone number')  
    elif row == 'trans_email_address':
      columns_after_modifying[index] = 'Email address' 
      general_details_list.append('Email address')  
    elif row == 'trans_aadhar_number':
      columns_after_modifying[index] = 'Aadhar number' 
      general_details_list.append('PAN')  
    elif row == 'trans_empbank':
      columns_after_modifying[index] = 'Bank'
      general_details_list.append('Bank')  
    elif row == 'trans_empbank_ifsc':
      columns_after_modifying[index] = 'IFSC'
      general_details_list.append('IFSC')  
    elif row == 'trans_empbank_acno':
      columns_after_modifying[index] = 'Account no'
      general_details_list.append('Account no')  
    elif row == 'trans_emp_otc':
      columns_after_modifying[index] = 'OT eligibility'
      general_details_list.append('OT eligibility')  
    elif row == 'trans_emp_otrate':
      columns_after_modifying[index] = 'OT rate'
      general_details_list.append('OT rate')  
    elif row == 'trans_emp_incrate':
      columns_after_modifying[index] = 'Incentive rate'     
      general_details_list.append('Incentive rate')  
    elif row == 'trans_attn_bonus':
      columns_after_modifying[index] = 'Attn bonus rate' 
      general_details_list.append('Attn bonus rate')  

    elif row == 'trans_mandays':
      columns_after_modifying[index] = 'Mandays'
      attendance_list.append('Mandays')      
    elif row == 'trans_wo':
      columns_after_modifying[index] = 'Weekly Off' 
      attendance_list.append('Weekly Off')
    elif row == 'trans_ph':
      columns_after_modifying[index] = 'Paid Holiday' 
      attendance_list.append('Paid Holiday')      
    elif row == 'trans_layoff':
      columns_after_modifying[index] = 'Lay Off'
      attendance_list.append('Lay Off')
    elif row == 'trans_absent':
      columns_after_modifying[index] = 'Absent'
      attendance_list.append('Absent')
    elif row == 'trans_paid_days':
      columns_after_modifying[index] = 'Paid days' 
      attendance_list.append('Paid days')
    elif row == 'trans_othrs':
      columns_after_modifying[index] = 'OT Hrs'
      attendance_list.append('OT Hrs')
    elif row == 'trans_inchrs':
      columns_after_modifying[index] = 'Incentive Hrs' 
      attendance_list.append('Incentive Hrs')

    elif row == 'pf_amt':
      columns_after_modifying[index] = 'PF Amt'
      deductions_list.append('PF Amt')
    elif row == 'fpf_amt':
      columns_after_modifying[index] = 'FPF Amt' 
      deductions_list.append('FPF Amt')      
    elif row == 'esi_amt':
      columns_after_modifying[index] = 'ESI Amt'
      deductions_list.append('ESI Amt')
    elif row == 'pt_amt':
      columns_after_modifying[index] = 'PT Amt'   
      deductions_list.append('PT Amt')     
    elif row == 'trans_adv':
      columns_after_modifying[index] = 'Advance'
      deductions_list.append('Advance')
    elif row == 'trans_tds':
      columns_after_modifying[index] = 'TDS' 
      deductions_list.append('TDS')
    elif row == 'trans_pfvol':
      columns_after_modifying[index] = 'PF Voluantary' 
      deductions_list.append('PF Voluantary')
    elif row == 'trans_lic':
      columns_after_modifying[index] = 'LIC'
      deductions_list.append('LIC')

    elif row == 'trans_arr_esipt':
      columns_after_modifying[index] = 'Arrears esi pt' 
      earnings_list .append('Arrears esi pt')
    elif row == 'trans_arr_pf':
      columns_after_modifying[index] = 'Arrears pf' 
      earnings_list .append('Arrears pf')
    elif row == 'trans_earn_attn_bonus':
      columns_after_modifying[index] = 'Attn bonus earned' 
      earnings_list .append('Attn bonus earned')  
    elif row == 'fxd_earn_gross':
      columns_after_modifying[index] = 'Fixed Gross'  
      earnings_list .append('Fixed Gross')  
    elif row == 'earn_pf_salary':
      columns_after_modifying[index] = 'PF salary'
      earnings_list .append('PF salary')  
    elif row == 'earn_fpf_salary':
      columns_after_modifying[index] = 'FPF salary'
      earnings_list .append('FPF salary')  
    elif row == 'earn_esi_salary':
      columns_after_modifying[index] = 'ESI salary'
      earnings_list .append('ESI salary')  
    elif row == 'earn_esi_salary':
      columns_after_modifying[index] = 'ESI salary' 
      earnings_list .append('ESI salary')  
    elif row == 'earn_pt_salary':
      columns_after_modifying[index] = 'PT salary'
      earnings_list .append('PT salary')  
    elif row == 'earn_ot_salary':
      columns_after_modifying[index] = 'OT salary' 
      earnings_list .append('OT salary')  
    elif row == 'earn_it_salary':
      columns_after_modifying[index] = 'IT salary' 
      earnings_list .append('IT salary')  
    elif row == 'earn_bonus_salary':
      columns_after_modifying[index] = 'Bonus salary' 
      earnings_list .append('Bonus salary')  
    elif row == 'ot_amt':
      columns_after_modifying[index] = 'OT Amt' 
      earnings_list .append('OT Amt')  
    elif row == 'bonus_amt':
      columns_after_modifying[index] = 'Bonus Amt' 
      earnings_list .append('Bonus Amt')  

    
    elif row == 'it_or_tds_amt':
      columns_after_modifying[index] = 'TDS repeated'   

  # column_names.insert(0,'Sl no')
  unmodified_cols.insert(0,'Sl no')

  columns_after_modifying.insert(0, 'Sl no')

  emp_details_list.insert(0, 'Sl no')

  extra_attendance_cols = ['trans_leave1', 'trans_leave2', 'trans_leave3']
  index_of_extra_attendance_cols = [unmodified_cols.index(element) for element in extra_attendance_cols]
  extra_attendance_cols_tbd = [columns_after_modifying[index] for index in index_of_extra_attendance_cols]
  attendance_list.extend(extra_attendance_cols_tbd)

  extra_ded_cols = ['trans_ded1', 'trans_ded2', 'trans_ded3', 'trans_ded4', 'trans_loan1', 'trans_loan2']
  index_of_extra_ded_cols = [unmodified_cols.index(element) for element in extra_ded_cols]
  index_of_extra_ded_cols_tbd = [columns_after_modifying[index] for index in index_of_extra_ded_cols]
  deductions_list.extend(index_of_extra_ded_cols_tbd)

  extra_earning_cols = ['trans_earn1', 'trans_earn2', 'trans_earn3', 'trans_earn4', 'trans_earn5', 
                    'trans_earn6', 'trans_earn7', 'trans_earn8', 'trans_earn9', 'trans_earn10', 
                    'trans_earn_earn1', 'trans_earn_earn2', 'trans_earn_earn3', 'trans_earn_earn4', 
                    'trans_earn_earn5', 'trans_earn_earn6', 'trans_earn_earn7', 'trans_earn_earn8', 
                    'trans_earn_earn9', 'trans_earn_earn10']
  index_of_extra_earning_cols = [unmodified_cols.index(element) for element in extra_earning_cols]
  index_of_extra_earning_cols_tbd = [columns_after_modifying[index] for index in index_of_extra_earning_cols]
  earnings_list.extend(index_of_extra_earning_cols_tbd)

  return columns_after_modifying,unmodified_cols, emp_details_list, general_details_list, attendance_list, earnings_list, deductions_list
  
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
        if record[selected_col].strftime("%d/%m/%Y") != "01/01/2000":
          print("Date is not 1752")
          filtered_row[selected_col] = record[selected_col].strftime("%d/%m/%Y")
      elif selected_col == "trans_empdoj":
        print("converted_date",record[selected_col].strftime("%d/%m/%Y"))
        if record[selected_col].strftime("%d/%m/%Y") != "01/01/2000":
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
def report_recovery_html_report(html_template,grid_rows,grid_cols,g_comname,g_transdate):
  template = Template(html_template)
    
  # Provide data to fill the placeholders
  data = {'grid_rows':grid_rows, 'grid_cols':grid_cols, 'company_name':g_comname, 'trans_date':g_transdate}
  
  # Render the HTML with the data
  html_content = template.render(data)
  print("html content",html_content)
  return html_content

@anvil.server.callable
def download_report_recovery_pdf(html_content):
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
def download_report_recovery_excel(html_content,company_name,date):
  # Parse the HTML content
  soup = BeautifulSoup(html_content, 'html.parser')
  
  # Extract content within the <div class="content"> tag
  content_div = soup.find('div', class_='content')
  
  # Extract the date
  date = content_div.find('p').get_text(strip=True)
  
  # Extract the company name
  company_name = content_div.find_all('h1')[1].get_text(strip=True)
  
  # Extract data from the HTML table
  data = []
  for row in soup.find_all(['tr']):
      columns = row.find_all(['th', 'td'])
      data.append([column.get_text(strip=True) for column in columns])
  
  # Create a pandas DataFrame for the table data
  table_df = pd.DataFrame(data)
  
  # Create a DataFrame for Date and Company Name
  header_data = {
      'Date': [date],
      'Company Name': [company_name],
  }
  
  # Concatenate the DataFrames
  combined_df = pd.concat([pd.DataFrame(header_data), table_df], ignore_index=True)
  
  # Export the combined DataFrame to an Excel file
  combined_df.to_excel('output.xlsx', index=False, header=False)

  pdf_media = anvil.media.from_file('output.xlsx', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'output.xlsx')
  return pdf_media

@anvil.server.callable
def download_report_recovery_csv(html_content):
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
  df.to_csv('output.csv', index=False, header=False)

  pdf_media = anvil.media.from_file('output.csv', 'csv', 'output.csv')
  return pdf_media