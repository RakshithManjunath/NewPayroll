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


######### auto increment 'id' column ###########
@anvil.server.callable
def emp_get_next_id_value():
  # Get the last row of the data table
  next_value = '0000000001'
  try:
    trans_code_list = [(r["id"]) for r in app_tables.employee.search()]
    last_row = trans_code_list[-1]
    last_string_value = last_row
    next_value = str(int(last_string_value) + 1).zfill(10)
  except IndexError:
    next_value == '0000000001'
  return next_value


######## add employee #########
@anvil.server.callable
def emp_add(id,emp_code,emp_name,emp_hus_name,emp_dob,emp_doj,
            emp_sex,emp_type,emp_pf_contribution,emp_pf_number,
            emp_pf_uan,emp_esi_contribution,emp_esi_number, 
            emp_esi_dispensary,emp_pt_contribution,emp_it_contribution,
            emp_pan_number,emp_dept_code,emp_dept_name,emp_desi_code,
            emp_desi_name,photo,emp_comp_code):
  return app_tables.employee.add_row(id=id,
                              emp_code=emp_code,
                              emp_name=emp_name,
                              emp_hus_name=emp_hus_name,
                              emp_dob=emp_dob,
                              emp_doj=emp_doj,
                              emp_sex=emp_sex,
                              emp_type=emp_type,
                              emp_pf_contribution=emp_pf_contribution,
                              emp_pf_number=emp_pf_number,
                              emp_pf_uan=emp_pf_uan,
                              emp_esi_contribution=emp_esi_contribution,
                              emp_esi_number=emp_esi_number,
                              emp_esi_dispensary=emp_esi_dispensary,
                              emp_pt_contribution=emp_pt_contribution,
                              emp_it_contribution=emp_it_contribution,
                              emp_pan_number=emp_pan_number,
                              emp_dept_code=emp_dept_code,
                              emp_dept_name=emp_dept_name,
                              emp_desi_code=emp_desi_code,
                              emp_desi_name=emp_desi_name,
                              emp_photo=photo,
                              emp_comp_code=emp_comp_code
                              )

@anvil.server.callable
def emp_default_values(row):
  columns_and_types = {
    'emp_hus_name': 'text', 
    'emp_dob': 'date',
    'emp_doj' : 'date',
    'emp_sex': 'text',
    'emp_type': 'text',
    'emp_pf_contribution': 'true/false',
    'emp_pf_number': 'number',
    'emp_pf_uan': 'text',
    'emp_esi_contribution': 'true/false',
    'emp_esi_number': 'number',
    'emp_esi_dispensary': 'text',
    'emp_pt_contribution': 'true/false',
    'emp_dept_code': 'text',
    'emp_dept_name': 'text',
    'emp_desi_code': 'text',
    'emp_desi_name': 'text',
    'emp_it_contribution': 'true/false',
    'emp_pan_number': 'text',
    'earn1': 'number',
    'earn2': 'number',
    'earn3': 'number',
    'earn4': 'number',
    'earn5': 'number',
    'earn6': 'number',
    'earn7': 'number',
    'earn8': 'number',
    'earn9': 'number',
    'earn10': 'number',
    'phone_number': 'number',
    'alt_phone_number': 'number',
    'email_address': 'text',
    'aadhar_number': 'number',
    'attn_bonus': 'number',
    'total_fxd_salary': 'number'
   }
  for column_name, column_type in columns_and_types.items():
    print(column_name, column_type)
    if row[column_name] is None:
      print(row[column_name])
      default_value = get_default_value_for_type(column_type)
      row[column_name] = default_value

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
def comp_wise_emp_code_and_name(emp_comp_code):
  emp_comp_details = []
  for r in app_tables.employee.search(emp_comp_code=emp_comp_code):
    emp_comp_details.append(r['emp_code'] + " | " + r['emp_name'])
  return emp_comp_details

######## change employee #########
@anvil.server.callable
def emp_update_row(emp_code,emp_name,emp_hus_name,emp_dob,emp_doj,
            emp_sex,emp_type,emp_pf_contribution,emp_pf_number,
            emp_pf_uan,emp_esi_contribution,emp_esi_number, 
            emp_esi_dispensary,emp_pt_contribution,emp_it_contribution,
            emp_pan_number,emp_dept_code,emp_dept_name,emp_desi_code,
            emp_desi_name):
  # rows = anvil.server.call('emp_change_name_and_code',emp_comp_code)
  row = app_tables.employee.get(emp_code=emp_code)
  row.update(emp_name=emp_name,
            emp_hus_name=emp_hus_name,
            emp_dob=emp_dob,
            emp_doj=emp_doj,
            emp_sex=emp_sex,
            emp_type=emp_type,
            emp_pf_contribution=emp_pf_contribution,
            emp_pf_number=emp_pf_number,
            emp_pf_uan=emp_pf_uan,
            emp_esi_contribution=emp_esi_contribution,
            emp_esi_number=emp_esi_number,
            emp_esi_dispensary=emp_esi_dispensary,
            emp_pt_contribution=emp_pt_contribution,
            emp_it_contribution=emp_it_contribution,
            emp_pan_number=emp_pan_number,
            emp_dept_code=emp_dept_code,
            emp_dept_name=emp_dept_name,
            emp_desi_code=emp_desi_code,
            emp_desi_name=emp_desi_name)

@anvil.server.callable
def emp_update2_row(emp_code,emp_name,emp_hus_name,emp_dob,emp_doj,
            emp_sex,emp_type,emp_pf_contribution,emp_pf_number,
            emp_pf_uan,emp_esi_contribution,emp_esi_number, 
            emp_esi_dispensary,emp_pt_contribution,emp_it_contribution,
            emp_pan_number,emp_dept_code,emp_dept_name,emp_desi_code,
            emp_desi_name):

  # print('dept code', emp_dept_code)
  # print('dept name', emp_dept_name)
  # print('desi code', emp_desi_code)
  # print('desi name', emp_desi_name)
  # rows = anvil.server.call('emp_change_name_and_code',emp_comp_code)
  row = app_tables.employee.get(emp_code=emp_code)
  trans_row = app_tables.transaction.get(trans_empid=emp_code)
  if trans_row != None:
    name_flag = False
    hus_flag = False
    gender_flag = False
    dob_flag = False
    doj_flag = False
    emptype_flag = False
    dept_flag = False
    desi_flag = False
  
    pfc_flag = False
    pfno_flag = False
    pfuan_flag = False

    esic_flag = False
    esino_flag = False
    esidisp_flag = False

    ptc_flag = False
    itc_flag = False
    itpan_flag = False
                
    if row['emp_name'] != emp_name:
      name_flag = True
    if row['emp_hus_name'] != emp_hus_name:
      hus_flag = True
    if row['emp_sex'] != emp_sex:
      gender_flag = True
    if row['emp_dob'] != emp_dob:
      dob_flag = True
    if row['emp_doj'] != emp_doj:
      doj_flag = True
    if row['emp_type'] != emp_type:
      emptype_flag = True 
    if row['emp_dept_code'] != emp_dept_code:
      dept_flag = True 
    if row['emp_desi_code'] != emp_desi_code:
      desi_flag = True 
  
    if row['emp_pf_contribution'] != emp_pf_contribution:
      pfc_flag = True               
    if row['emp_pf_number'] != emp_pf_number:
      pfno_flag = True  
    if row['emp_pf_uan'] != emp_pf_uan:
      pfuan_flag = True 

    if row['emp_esi_contribution'] != emp_esi_contribution:
      esic_flag = True 
    if row['emp_esi_number'] != emp_esi_number:
      esino_flag = True  
    if row['emp_esi_dispensary'] != emp_esi_dispensary:
       esidisp_flag = True  

    if row['emp_pt_contribution'] != emp_pt_contribution:
      ptc_flag = True     
    if row['emp_it_contribution'] != emp_it_contribution:
      itc_flag = True  
    if row['emp_pan_number'] != emp_pan_number:
      itpan_flag = True 
  
    if name_flag == True:
      row.update(emp_name=emp_name)
      trans_row.update(trans_empname=emp_name)
  
    if hus_flag == True:
      row.update(emp_hus_name=emp_hus_name)
      trans_row.update(trans_father_husband=emp_hus_name)
  
    if gender_flag == True:
      row.update(emp_sex=emp_sex)
      trans_row.update(trans_empsex=emp_sex)
  
    if dob_flag == True:
      row.update(emp_dob=emp_dob)
      trans_row.update(trans_empdob=emp_dob)    
      
    if doj_flag == True:
      row.update(emp_doj=emp_doj)
      trans_row.update(trans_empdoj=emp_doj)  
  
    if emptype_flag == True:
      row.update(emp_type=emp_type)
      trans_row.update(trans_emptype=emp_type)  
      
    if dept_flag == True:
      row.update(emp_dept_code=emp_dept_code)
      row.update(emp_dept_name=emp_dept_name)    
      trans_row.update(trans_deptcode=emp_dept_code)
      trans_row.update(trans_deptname=emp_dept_name) 
  
    if desi_flag == True:
      row.update(emp_desi_code=emp_desi_code)
      row.update(emp_desi_name=emp_desi_name)    
      trans_row.update(trans_desicode=emp_desi_code) 
      trans_row.update(trans_desiname=emp_desi_name) 
  
    if pfc_flag == True:
      row.update(emp_pf_contribution=emp_pf_contribution)
      trans_row.update(trans_emppfc=emp_pf_contribution)  
    if pfno_flag == True:
      row.update(emp_pf_number=emp_pf_number)
      trans_row.update(trans_emppfno=emp_pf_number)
    if pfuan_flag == True:
      row.update(emp_pf_uan=emp_pf_uan)
      trans_row.update(trans_emp_pfuan=emp_pf_uan)

    if esic_flag == True:
      row.update(emp_esi_contribution=emp_esi_contribution)
      trans_row.update(trans_empesic=emp_esi_contribution)  
    if  esino_flag == True:
      row.update(emp_esi_number=emp_esi_number)
      trans_row.update(trans_empesino=emp_esi_number)  
    if esidisp_flag == True:
      row.update(emp_esi_dispensary=emp_esi_dispensary)
      trans_row.update(trans_empdispensary=emp_esi_dispensary)  

    if ptc_flag == True:
      row.update(emp_pt_contribution=emp_pt_contribution)
      trans_row.update(trans_empptc=emp_pt_contribution) 
    if itc_flag == True:
      row.update(emp_it_contribution=emp_it_contribution)
      trans_row.update(trans_empitc=emp_it_contribution) 
    if itpan_flag == True:
      row.update(emp_pan_number=emp_pan_number)
      trans_row.update(trans_emppan=emp_pan_number)  

####### concatenating emp name and code #########
@anvil.server.callable
def emp_name_and_code():
  emp_details = []
  for r in app_tables.employee.search(tables.order_by("emp_code")):
    emp_details.append(r['emp_code'] + " | "  +r['emp_name'])
  return emp_details


@anvil.server.callable
def emp_get_details(empcode,emp_comp_code):
  # row = app_tables.employee.get(emp_code=empcode)
  row = app_tables.employee.search(emp_code=empcode,emp_comp_code=emp_comp_code)[0]
  return row


################ update emp earning #################
@anvil.server.callable
def emp_update_earn(empcode, earn1,earn2,earn3,earn4,earn5,earn6,earn7,earn8,earn9,earn10,fxd_sal):
  row = app_tables.employee.get(emp_code=empcode)
  row.update(earn1=earn1,earn2=earn2,earn3=earn3,earn4=earn4,earn5=earn5,
            earn6=earn6,earn7=earn7,earn8=earn8,earn9=earn9,earn10=earn10,
            total_fxd_salary=fxd_sal)

  trans_row = app_tables.transaction.get(trans_empid=empcode)
  trans_row.update(trans_earn1=earn1,trans_earn2=earn2,trans_earn3=earn3,trans_earn4=earn4,
                  trans_earn5=earn5,trans_earn6=earn6,trans_earn7=earn7,trans_earn8=earn8,
                  trans_earn9=earn9,trans_earn10=earn10)

############# update emp misc1 ################
@anvil.server.callable
def emp_update_misc1(empcode,phone_number,alt_phone_number,email_address,aadhar_number,
                    attn_bonus,bankcode,empbank,bankifsc,bankacno):
  row = app_tables.employee.get(emp_code=empcode)
  row.update(phone_number=phone_number,alt_phone_number=alt_phone_number,
            email_address=email_address,
            aadhar_number=aadhar_number,
            attn_bonus=attn_bonus,
            emp_bank_code = bankcode,
            emp_bank = empbank,
            emp_bank_ifsc=bankifsc,
            emp_bank_acno = bankacno)

  trans_row = app_tables.transaction.get(trans_empid=empcode)
  trans_row.update(trans_phone_number=phone_number,
                   trans_alt_phone_number=alt_phone_number,
                  trans_email_address=email_address,
                  trans_aadhar_number=aadhar_number,
                  trans_attn_bonus=attn_bonus,
                  trans_empbank_code = bankcode,
                  trans_empbank = empbank,
                  trans_empbank_ifsc = bankifsc,
                  trans_empbank_acno = bankacno)


############# update emp misc2 ################
@anvil.server.callable
def emp_update_misc2(empcode,emp_photo):
  row = app_tables.employee.get(emp_code=empcode)
  row.update(emp_photo = emp_photo)

############# update emp misc2b ################
@anvil.server.callable
def emp_update_misc2b(empcode,emp_photo):
  row = app_tables.transaction.get(trans_empid=empcode)
  row.update(emp_photo = emp_photo)


#### Find Last record in employee table ###########
@anvil.server.callable
def get_last_emp_code(emp_comp_code):
  emp_list = [(r["emp_code"]) for r in app_tables.employee.search(emp_comp_code=emp_comp_code)]
  if len(emp_list) > 0:
    last_row = emp_list[-1]
    last_string_value = last_row
  else:
    last_string_value = "Start"
  return last_string_value


############# update emp misc3 ################
@anvil.server.callable
def emp_update_misc3(empcode,phone_number,alt_phone_number,email_address,aadhar_number,
                    attn_bonus,bankcode,empbank,bankifsc,bankacno):
  row = app_tables.employee.get(emp_code=empcode)
  row.update(phone_number=phone_number,alt_phone_number=alt_phone_number,
            email_address=email_address,
            aadhar_number=aadhar_number,
            attn_bonus=attn_bonus,
            emp_bank_code = bankcode,
            emp_bank = empbank,
            emp_bank_ifsc=bankifsc,
            emp_bank_acno = bankacno)

  trans_row = app_tables.transaction.get(trans_empid=empcode)
  trans_row.update(trans_phone_number=phone_number,
                   trans_alt_phone_number=alt_phone_number,
                  trans_email_address=email_address,
                  trans_aadhar_number=aadhar_number,
                  trans_attn_bonus=attn_bonus,
                  trans_empbank_code = bankcode,
                  trans_empbank = empbank,
                  trans_empbank_ifsc = bankifsc,
                  trans_empbank_acno = bankacno)
