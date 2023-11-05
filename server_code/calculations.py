import anvil.files
from anvil.files import data_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import date

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

#### Transaction ###############
####### concatenating emp name and code #########

@anvil.server.callable
def trans_empcode_name():
  emp_details = []
  for r in app_tables.employee.search(tables.order_by("emp_code")):
    emp_details.append(r['emp_code'] + " | "  +r['emp_name'])
  return emp_details

@anvil.server.callable
def trans_get_next_string_value():
  # Get the last row of the data table
  next_value = '0000000001'
  try:
    id_list = [(r["id"]) for r in app_tables.transaction.search()]
    last_row = id_list[-1]
    last_string_value = last_row
    next_value = str(int(last_string_value) + 1).zfill(10)
  except IndexError:
    next_value == '0000000001'
  return next_value

@anvil.server.callable
def emp_to_trans_transfer(id,trans_date,trans_empid,trans_empname,trans_father_husband,
                           trans_empsex,trans_empdob,trans_empdoj,trans_emptype,trans_deptcode,
                           trans_deptname,trans_desicode,trans_desiname,trans_emppfc,
                           trans_emppfno,trans_emp_pfuan,trans_empesic,trans_empesino,
                           trans_empdispensary,trans_empptc,trans_empitc,trans_emppan,trans_comp_code,emp_photo):
  transaction = app_tables.transaction
  return transaction.add_row(
      id=id,
      trans_date=trans_date,
      trans_empid=trans_empid,
      trans_empname=trans_empname,
      trans_father_husband=trans_father_husband,
      trans_empsex = trans_empsex,
      trans_empdob = trans_empdob,
      trans_empdoj = trans_empdoj,
      trans_emptype = trans_emptype,
      trans_deptcode = trans_deptcode,
      trans_deptname = trans_deptname,
      trans_desicode = trans_desicode,
      trans_desiname = trans_desiname,
      trans_emppfc = trans_emppfc,
      trans_emppfno = trans_emppfno,
      trans_emp_pfuan = trans_emp_pfuan,
      trans_empesic = trans_empesic,
      trans_empesino = trans_empesino,
      trans_empdispensary = trans_empdispensary,
      trans_empptc = trans_empptc,
      trans_empitc = trans_empitc,
      trans_emppan = trans_emppan,
      trans_comp_code=trans_comp_code,
      emp_photo=emp_photo)

@anvil.server.callable
def emp_more_update(trans_empid,trans_phone_number,trans_alt_phone_number,trans_email_address,
                           trans_aadhar_number,trans_attn_bonus,
                           trans_earn1,trans_earn2,trans_earn3,trans_earn4,trans_earn5,
                           trans_earn6,trans_earn7,trans_earn8,trans_earn9,trans_earn10,
                           trans_mandays,trans_wo,trans_ph,trans_layoff,trans_absent,
                           trans_leave1,trans_leave2,trans_leave3,trans_othrs,trans_inchrs,
                           trans_ded1,trans_ded2,trans_ded3,trans_ded4,
                           trans_loan1,trans_loan2,
                           trans_adv,trans_tds,trans_pfvol,trans_lic,
                           trans_arr_esipt,trans_arr_pf,trans_paid_days,trans_comp_code):

  row = app_tables.transaction.get(trans_empid=trans_empid)
  row.update(trans_phone_number = trans_phone_number,
  trans_alt_phone_number = trans_alt_phone_number,
  trans_email_address = trans_email_address,
  trans_aadhar_number = trans_aadhar_number,
  trans_attn_bonus = trans_attn_bonus,
  trans_earn1 = trans_earn1,
  trans_earn2 = trans_earn2,
  trans_earn3 = trans_earn3,
  trans_earn4 = trans_earn4,
  trans_earn5 = trans_earn5,
  trans_earn6 = trans_earn6,
  trans_earn7 = trans_earn7,
  trans_earn8 = trans_earn8,
  trans_earn9 = trans_earn9,
  trans_earn10 = trans_earn10,
  trans_mandays=trans_mandays,
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
  trans_paid_days=trans_paid_days,
  trans_comp_code = trans_comp_code)
            

  
    
                             
def get_default_value_for_type(column_type):
  # Define default values based on column types (you can customize this)
  if column_type == 'text':
      return ''
  elif column_type == 'number':
      return 0
  elif column_type == 'date':
      return date(1752, 1, 1)  # Current UTC date and time
  elif column_type == 'true/false':
      return False
  return None
  

@anvil.server.callable
def trans_default_values(row):
  columns_and_types = {
  'trans_mandays': 'number',
  'trans_wo': 'number',
  'trans_ph': 'number',
  'trans_layoff': 'number',
  'trans_absent': 'number',
  'trans_leave1': 'number',
  'trans_leave2': 'number',
  'trans_leave3': 'number',
  'trans_othrs': 'number',
  'trans_inchrs': 'number',
  'trans_ded1': 'number',
  'trans_ded2': 'number',  
  'trans_ded3': 'number', 
  'trans_ded4': 'number',
  'trans_loan1': 'number',
  'trans_loan2': 'number',
  'trans_adv': 'number',
  'trans_tds': 'number',
  'trans_pfvol': 'number',
  'trans_lic': 'number',
  'trans_arr_esipt': 'number',
  'trans_arr_pf': 'number',
  'trans_earn_earn1': 'number', 
  'trans_earn_earn2': 'number', 
  'trans_earn_earn3': 'number', 
  'trans_earn_earn4': 'number', 
  'trans_earn_earn5': 'number', 
  'trans_earn_earn6': 'number', 
  'trans_earn_earn7': 'number', 
  'trans_earn_earn8': 'number', 
  'trans_earn_earn9': 'number', 
  'trans_earn_earn10': 'number',
  'fxd_earn_gross': 'number',
  'earn_pf_salary': 'number',
  'earn_fpf_salary': 'number',
  'earn_esi_salary': 'number',
  'earn_pt_salary': 'number', 
  'earn_ot_salary': 'number',
  'earn_it_salary': 'number', 
  'earn_bonus_salary': 'number',      
  'pf_amt': 'number',
  'fpf_amt': 'number',
  'esi_amt': 'number',
  'pt_amt': 'number',
  'ot_amt': 'number',
  'it_or_tds_amt': 'number',
  'bonus_amt': 'number',  
  'trans_paid_days': 'number',
  'trans_comp_code': 'text',
  'trans_earn_attn_bonus': 'number',
  'trans_empdob': 'date',
  'trans_empdoj': 'date',
  'trans_deptcode': 'text',
  'trans_deptname': 'text',
  'trans_desicode': 'text',
  'trans_desiname': 'text',
  'trans_empesino': 'number',
  'trans_emppfno': 'number',
  'trans_earn1': 'number',
  'trans_earn2': 'number',
  'trans_earn3': 'number',
  'trans_earn4': 'number',
  'trans_earn5': 'number',
  'trans_earn6': 'number',
  'trans_earn7': 'number',
  'trans_earn8': 'number',
  'trans_earn9': 'number',
  'trans_earn10': 'number',
  'trans_phone_number': 'number',
  'trans_alt_phone_number': 'number',
  'trans_email_address': 'text',
  'trans_aadhar_number': 'number',
  'trans_attn_bonus': 'number'}
  
  for column_name, column_type in columns_and_types.items():
    print(column_name, column_type)
    if row[column_name] is None:
      print(row[column_name])
      default_value = get_default_value_for_type(column_type)
      row[column_name] = default_value  

@anvil.server.callable
def trans_earn_earn_calculation(comp_code,trans_empid):
  # trans_row = app_tables.transaction.get(trans_empid=trans_empid)
  # paid_days = trans_row['trans_mandays'] + trans_row['trans_wo'] + trans_row['trans_ph'] + \
  # trans_row['trans_leave1'] + trans_row['trans_leave2'] + trans_row['trans_leave3']

  # print(paid_days)
  
  row = app_tables.company.get(comp_code=comp_code)
  eh1 = eh2 = eh3 = eh4 = eh5 = eh6 = eh7 = eh8 = eh9 = eh10 = False
  if row['comp_earn_head1'] != "":
    eh1 = True
  if row['comp_earn_head2'] != "":
    eh2 = True
  if row['comp_earn_head3'] != "":
    eh3 = True
  if row['comp_earn_head4'] != "":
    eh4 = True
  if row['comp_earn_head5'] != "":
    eh5 = True
  if row['comp_earn_head6'] != "":
    eh6 = True
  if row['comp_earn_head7'] != "":
    eh7 = True
  if row['comp_earn_head8'] != "":
    eh8 = True
  if row['comp_earn_head9'] != "":
    eh9 = True
  if row['comp_earn_head10'] != "":
    eh10 = True

  
    
    # trans_row = app_tables.transaction.get(trans_empid=trans_empid)
    # trans_row['trans_mandays']


