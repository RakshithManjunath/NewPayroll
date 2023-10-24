import anvil.files
from anvil.files import data_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd
import file_path
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

@anvil.server.callable
def import_company_csv():
  with open(file_path.company_path, "r") as f:
    dtype_mapping = {
    'comp_id': str,  
    'comp_code': str,
    'comp_name': str,
    'comp_addr1':str,  
    'comp_addr2':str,  
    'comp_addr3':str,
    'comp_pf_number': str,
    'comp_esi_number': str,
    'comp_pto_circle': str, 
    'comp_emp_pfrate': float, 
    'comp_empr_fpfrate': float, 
    'comp_pf_admin': float, 
    'comp_pf_edli': float, 
    'comp_mgmt_pf_lt': float, 
    'comp_mgmt_fpf_lt': float, 
    'comp_esi_sal_lt': float, 
    'comp_pts1_from': float, 
    'comp_pts1_to': float, 
    'comp_pts1_pt': float, 
    'comp_pts2_from': float, 
    'comp_pts2_to': float, 
    'comp_pts2_pt': float, 
    'comp_pts3_from': float, 
    'comp_pts3_to': float, 
    'comp_pts3_pt': float, 
    'comp_ded1': str, 
    'comp_ded2': str,
    'comp_ded3': str, 
    'comp_ded4': str,
    'comp_earn_head1': str, 
    'comp_earnhead1_pf': bool,
    'comp_earnhead1_esi': bool,
    'comp_earnhead1_pt': bool, 
    'comp_earnhead1_it': bool, 
    'comp_earnhead1_ot': bool, 
    'comp_earnhead1_bonus': bool, 
    'comp_earn_head2': str, 
    'comp_earnhead2_pf': bool, 
    'comp_earnhead2_esi': bool, 
    'comp_earnhead2_pt': bool, 
    'comp_earnhead2_it': bool, 
    'comp_earnhead2_ot': bool, 
    'comp_earnhead2_bonus': bool, 
    'comp_earn_head3': str, 
    'comp_earnhead3_pf': bool,
    'comp_earnhead3_esi': bool, 
    'comp_earnhead3_pt': bool, 
    'comp_earnhead3_it': bool, 
    'comp_earnhead3_ot': bool, 
    'comp_earnhead3_bonus': bool, 
    'comp_earn_head4': str, 
    'comp_earnhead4_pf': bool, 
    'comp_earnhead4_esi': bool, 
    'comp_earnhead4_pt': bool, 
    'comp_earnhead4_it': bool, 
    'comp_earnhead4_ot': bool, 
    'comp_earnhead4_bonus': bool, 
    'comp_earn_head5': str, 
    'comp_earnhead5_pf': bool,
    'comp_earnhead5_esi': bool,
    'comp_earnhead5_pt': bool, 
    'comp_earnhead5_it': bool, 
    'comp_earnhead5_ot': bool, 
    'comp_earnhead5_bonus': bool, 
    'comp_earn_head6': str, 
    'comp_earnhead6_pf': bool, 
    'comp_earnhead6_esi': bool, 
    'comp_earnhead6_pt': bool, 
    'comp_earnhead6_it': bool, 
    'comp_earnhead6_ot': bool, 
    'comp_earnhead6_bonus': bool, 
    'comp_earn_head7': str, 
    'comp_earnhead7_pf': bool,
    'comp_earnhead7_esi': bool,
    'comp_earnhead7_pt': bool, 
    'comp_earnhead7_it': bool, 
    'comp_earnhead7_ot': bool, 
    'comp_earnhead7_bonus': bool, 
    'comp_earn_head8': str, 
    'comp_earnhead8_pf': bool, 
    'comp_earnhead8_esi': bool, 
    'comp_earnhead8_pt': bool, 
    'comp_earnhead8_it': bool, 
    'comp_earnhead8_ot': bool, 
    'comp_earnhead8_bonus': bool,
    'comp_earn_head9': str, 
    'comp_earnhead9_pf': bool, 
    'comp_earnhead9_esi': bool, 
    'comp_earnhead9_pt': bool, 
    'comp_earnhead9_it': bool, 
    'comp_earnhead9_ot': bool, 
    'comp_earnhead9_bonus': bool, 
    'comp_earn_head10': str, 
    'comp_earnhead10_pf': bool, 
    'comp_earnhead10_esi': bool, 
    'comp_earnhead10_pt': bool, 
    'comp_earnhead10_it': bool, 
    'comp_earnhead10_ot': bool, 
    'comp_earnhead10_bonus': bool,
    'comp_bonus_from': str, 
    'comp_bonus_to': str, 
    'comp_bonus_percentage': float,
    'comp_bonus_limit': float,
    'comp_bonus_pt_included': bool, 
    'comp_leave_head1': str,
    'comp_leave_head2': str,
    'comp_leave_head3': str,
    'comp_loan_head1': str,
    'comp_loan_head2': str
    }
    df = pd.read_csv(f, dtype=dtype_mapping,keep_default_na=False)
    df['comp_pay_date'] = pd.to_datetime(df['comp_pay_date']).dt.date
    key_to_ignore = 'ID'
    ignored_dict = {key: value for key, value in df.items() if key != key_to_ignore}
    ignored_dict = pd.DataFrame(ignored_dict)
    print(ignored_dict)
    ignored_dict = pd.DataFrame(ignored_dict)
    for d in ignored_dict.to_dict(orient="records"):
      print(d)
      app_tables.company.add_row(**d)

@anvil.server.callable
def import_password_csv():
  with open(file_path.password_path, "r") as f:
    dtype_mapping = {
    'pass_id': str,
    'pass_code': str,
    'pass_comp_code': str,
    'username': str,  
    'password': str
    }
    df = pd.read_csv(f, dtype=dtype_mapping,keep_default_na=False)
    key_to_ignore = 'ID'
    ignored_dict = {key: value for key, value in df.items() if key != key_to_ignore}
    ignored_dict = pd.DataFrame(ignored_dict)
    for d in ignored_dict.to_dict(orient="records"):
      print(d)
      app_tables.password.add_row(**d)

@anvil.server.callable
def import_trans_date_csv():
  with open(file_path.trans_date_path, "r") as f:
    dtype_mapping = { 
    'trdate_comp_code': str,
    'tr_days': int,
    'tr_sundays': int,
    'tr_id': int
    }
    df = pd.read_csv(f, dtype=dtype_mapping,keep_default_na=False)
    df['tr_date'] = pd.to_datetime(df['tr_date']).dt.date
    df['tr_end_date'] = pd.to_datetime(df['tr_end_date']).dt.date
    key_to_ignore = 'ID'
    ignored_dict = {key: value for key, value in df.items() if key != key_to_ignore}
    ignored_dict = pd.DataFrame(ignored_dict)
    for d in ignored_dict.to_dict(orient="records"):
      print(d)
      app_tables.trans_date.add_row(**d)

@anvil.server.callable
def import_department_csv():
  with open(file_path.department_path, "r") as f:
    dtype_mapping = { 
    'dept_id': str, 
    'dept_comp_code': str,
    'dept_code': str,
    'dept_name': str
    }
    df = pd.read_csv(f, dtype=dtype_mapping,keep_default_na=False)
    key_to_ignore = 'ID'
    ignored_dict = {key: value for key, value in df.items() if key != key_to_ignore}
    ignored_dict = pd.DataFrame(ignored_dict)
    for d in ignored_dict.to_dict(orient="records"):
      print(d)
      app_tables.department.add_row(**d)

@anvil.server.callable
def import_designation_csv():
  with open(file_path.designation_path, "r") as f:
    dtype_mapping = { 
    'desi_id': str, 
    'desi_comp_code': str,
    'desi_code': str,
    'desi_name': str
    }
    df = pd.read_csv(f, dtype=dtype_mapping,keep_default_na=False)
    key_to_ignore = 'ID'
    ignored_dict = {key: value for key, value in df.items() if key != key_to_ignore}
    ignored_dict = pd.DataFrame(ignored_dict)
    for d in ignored_dict.to_dict(orient="records"):
      print(d)
      app_tables.designation.add_row(**d)

@anvil.server.callable
def import_bank_csv():
  with open(file_path.bank_path, "r") as f:
    dtype_mapping = { 
    'bank_id': str, 
    'bank_comp_code': str, 
    'bank_code': str,
    'bank_name': str,
    'bank_addr1': str,
    'bank_addr2': str,
    'bank_addr3': str,
    'bank_ifsc': str          
    }
    df = pd.read_csv(f, dtype=dtype_mapping,keep_default_na=False)
    key_to_ignore = 'ID'
    ignored_dict = {key: value for key, value in df.items() if key != key_to_ignore}
    ignored_dict = pd.DataFrame(ignored_dict)
    for d in ignored_dict.to_dict(orient="records"):
      print(d)
      app_tables.bank.add_row(**d)

@anvil.server.callable
def import_employee_csv():
  with open(file_path.employee_path, "r") as f:
    dtype_mapping = { 
    'id': str, 
    'emp_comp_code': str,
    'emp_code': str,
    'emp_name': str,
    'emp_hus_name': str,
    'emp_sex': str, 
    'emp_type': str,      
    'emp_pf_contribution': bool,      
    'emp_pf_number': int,
    'emp_pf_uan': str,  
    'emp_esi_contribution': bool,
    'emp_esi_number': int,
    'emp_esi_dispensary': str,   
    'emp_pt_contribution': bool,
    'emp_dept_code': str,  
    'emp_dept_name': str, 
    'emp_desi_code': str, 
    'emp_desi_name': str, 
    'emp_it_contribution': bool,
    'emp_pan_number': str,
    'earn1': float,
    'earn2': float,
    'earn3': float,
    'earn4': float,
    'earn5': float,  
    'earn6': float, 
    'earn7': float,
    'earn8': float,
    'earn9': float, 
    'earn10': float,
    'phone_number': int,
    'alt_phone_number': int,
    'email_address': str,
    'aadhar_number': int,
    'attn_bonus': float,
    'total_fxd_salary': float
    }
    df = pd.read_csv(f, dtype=dtype_mapping,keep_default_na=False)
    columns_to_exclude = ['emp_dob', 'emp_doj','emp_photo']  # Columns to exclude
    for _, row in df.iterrows():
      print(row, row['emp_photo'])
      # Create a media object from the 'photo_bytes' column
      photo_media = get_media_from_bytes_image(row['emp_photo'],row['emp_code'])  # Replace with the actual function
      print(photo_media)
      # pdf_media = get_media_from_bytes_pdf(row['emp_pdf_docu1'],row['emp_code'])
      
      # Remove the 'photo_bytes' column from the row
      row = row.drop('emp_photo')
      # row = row.drop('emp_pdf_docu1')
      
      emp_dob = pd.to_datetime(row['emp_dob']).date()
      emp_doj = pd.to_datetime(row['emp_doj']).date()

      data_dict = {col: row[col] for col in df.columns if col not in columns_to_exclude}

      data_dict.update({
        'emp_dob': emp_dob,
        'emp_doj': emp_doj,
        'emp_photo': photo_media
      })

      app_tables.employee.add_row(**data_dict)
      
@anvil.server.callable
def import_transaction_csv():
  with open(file_path.transaction_path, "r") as f:
    dtype_mapping = { 
    'id': str,     
    'trans_comp_code': str,
    'trans_empid': str,
    'trans_empname': str,
    'trans_father_husband': str,
    'trans_empsex': str,
    'trans_emptype': str,
    'trans_deptcode': str,  
    'trans_deptname': str,
    'trans_desicode': str,
    'trans_desiname': str,
    'trans_emppfc': bool,
    'trans_emppfno': int,
    'trans_emp_pfuan': str,
    'trans_empesic': bool,
    'trans_empesino': int,
    'trans_empdispensary': str, 
    'trans_empptc': bool,
    'trans_empitc': bool,
    'trans_emppan': str,
    'trans_mandays': float,
    'trans_wo': float, 
    'trans_ph': float, 
    'trans_layoff': float, 
    'trans_absent': float,
    'trans_leave1': float,
    'trans_leave2': float,      
    'trans_leave3': float,      
    'trans_othrs': float,
    'trans_inchrs': float,
    'trans_ded1': float,
    'trans_ded2': float, 
    'trans_ded3': float,
    'trans_ded4': float,
    'trans_loan1': float,
    'trans_loan2': float,
    'trans_adv': float,
    'trans_tds': float,
    'trans_pfvol': float,
    'trans_lic': float,
    'trans_arr_esipt': float,
    'trans_arr_pf': float,
    'trans_earn1': float,
    'trans_earn2': float,
    'trans_earn3': float,
    'trans_earn4': float,
    'trans_earn5': float,
    'trans_earn6': float,
    'trans_earn7': float,
    'trans_earn8': float,
    'trans_earn9': float,
    'trans_earn10': float,
    'trans_earn_earn1': float,  
    'trans_earn_earn2': float, 
    'trans_earn_earn3': float,
    'trans_earn_earn4': float,
    'trans_earn_earn5': float,
    'trans_earn_earn6': float,
    'trans_earn_earn7': float,
    'trans_earn_earn8': float,
    'trans_earn_earn9': float,
    'trans_earn_earn10': float,
    'trans_phone_number': int,
    'trans_alt_phone_number': int,
    'trans_email_address': str,
    'trans_aadhar_number': int,
    'trans_attn_bonus': float,
    'fxd_earn_gross': float,
    'earn_pf_salary': float,
    'earn_fpf_salary': float,
    'earn_esi_salary': float,
    'earn_pt_salary': float,
    'earn_ot_salary': float,
    'earn_it_salary': float,
    'earn_bonus_salary': float,
    'pf_amt': float,
    'fpf_amt': float,
    'esi_amt': float,
    'pt_amt': float,
    'ot_amt': float,
    'it_or_tds_amt': float,
    'bonus_amt': float,
    'trans_paid_days': float,
    'trans_earn_attn_bonus': float
    }
    df = pd.read_csv(f, dtype=dtype_mapping,keep_default_na=False)
    df['trans_date'] = pd.to_datetime(df['trans_date']).dt.date 
    df['trans_empdob'] = pd.to_datetime(df['trans_empdob']).dt.date    
    df['trans_empdoj'] = pd.to_datetime(df['trans_empdoj']).dt.date    
    key_to_ignore = 'ID'
    ignored_dict = {key: value for key, value in df.items() if key != key_to_ignore}
    ignored_dict = pd.DataFrame(ignored_dict)
    for d in ignored_dict.to_dict(orient="records"):
      print(d)
      app_tables.transaction.add_row(**d)

# def get_media_from_bytes_pdf(bytes_data,filename):
#   if bytes_data:
#     media_bytes = base64.b64decode(bytes_data)
#     return anvil.BlobMedia('application/pdf', media_bytes, name=filename + ".pdf")
#   else:
#     return None

def get_media_from_bytes_image(bytes_data,filename):
  if bytes_data:
    media_bytes = base64.b64decode(bytes_data)
    return anvil.BlobMedia('image/jpeg', media_bytes, name=filename + ".png")
  else:
    return None

@anvil.server.callable
def get_media_from_bytes_image_emp_add(bytes_data,filename):
  if bytes_data:
    media_bytes = base64.b64decode(bytes_data)
    return anvil.BlobMedia('image/jpeg', media_bytes, name=filename + ".png")
  else:
    return None



# @anvil.server.callable
# def import_all_csv():
#   upload.import_department_csv()
#   upload.import_designation_csv()
#   upload.import_bank_csv()
#   upload.import_password_csv()
#   upload.import_trans_date_csv()
#   upload.import_company_csv()
#   upload.import_employee_csv()
#   upload.import_transaction_csv()

@anvil.server.callable
def import_all_csv():
  import_department_csv()
  import_designation_csv()
  import_bank_csv()
  import_password_csv()
  import_trans_date_csv()
  import_company_csv()
  import_employee_csv()
  import_transaction_csv()