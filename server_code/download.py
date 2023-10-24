import anvil.files
from anvil.files import data_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd
import file_path
import io
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
def get_all_companies_download():
  data_table = app_tables.company.search()
  csv_rows = []
  
  earnhead1_pf = None
  earnhead1_esi = None
  earnhead1_pt = None
  earnhead1_it = None
  earnhead1_ot = None
  earnhead1_bonus = None

  earnhead2_pf = None
  earnhead2_esi = None
  earnhead2_pt = None
  earnhead2_it = None
  earnhead2_ot = None
  earnhead2_bonus = None

  earnhead3_pf = None
  earnhead3_esi = None
  earnhead3_pt = None
  earnhead3_it = None
  earnhead3_ot = None
  earnhead3_bonus = None

  earnhead4_pf = None
  earnhead4_esi = None
  earnhead4_pt = None
  earnhead4_it = None
  earnhead4_ot = None
  earnhead4_bonus = None

  earnhead5_pf = None
  earnhead5_esi = None
  earnhead5_pt = None
  earnhead5_it = None
  earnhead5_ot = None
  earnhead5_bonus = None

  earnhead6_pf = None
  earnhead6_esi = None
  earnhead6_pt = None
  earnhead6_it = None
  earnhead6_ot = None
  earnhead6_bonus = None

  earnhead7_pf = None
  earnhead7_esi = None
  earnhead7_pt = None
  earnhead7_it = None
  earnhead7_ot = None
  earnhead7_bonus = None

  earnhead8_pf = None
  earnhead8_esi = None
  earnhead8_pt = None
  earnhead8_it = None
  earnhead8_ot = None
  earnhead8_bonus = None

  earnhead9_pf = None
  earnhead9_esi = None
  earnhead9_pt = None
  earnhead9_it = None
  earnhead9_ot = None
  earnhead9_bonus = None

  earnhead10_pf = None
  earnhead10_esi = None
  earnhead10_pt = None
  earnhead10_it = None
  earnhead10_ot = None
  earnhead10_bonus = None
  
  bonus_pt_included = None
 
  for row in data_table:
    if row['comp_earnhead1_pf'] == False:
      ehead1_pf = 0
    elif row['comp_earnhead1_pf'] == True:
      ehead1_pf = 1
    elif row['comp_earnhead1_pf'] == None:
      ehead1_pf = 0
      
    if row['comp_earnhead1_esi'] == False:
      ehead1_esi = 0
    elif row['comp_earnhead1_esi'] == True:
      ehead1_esi = 1
    elif row['comp_earnhead1_esi'] == None:
      ehead1_esi = 0  

    if row['comp_earnhead1_pt'] == False:
      ehead1_pt = 0
    elif row['comp_earnhead1_pt'] == True:
      ehead1_pt = 1
    elif row['comp_earnhead1_pt'] == None:
      ehead1_pt = 0 
      
    if row['comp_earnhead1_it'] == False:
      ehead1_it = 0
    elif row['comp_earnhead1_it'] == True:
      ehead1_it = 1
    elif row['comp_earnhead1_it'] == None:
      ehead1_it = 0

    if row['comp_earnhead1_ot'] == False:
      ehead1_ot = 0
    elif row['comp_earnhead1_ot'] == True:
      ehead1_ot = 1
    elif row['comp_earnhead1_ot'] == None:
      ehead1_ot = 0   

    if row['comp_earnhead1_bonus'] == False:
      ehead1_bonus = 0
    elif row['comp_earnhead1_bonus'] == True:
      ehead1_bonus = 1
    elif row['comp_earnhead1_bonus'] == None:
      ehead1_bonus = 0    


    if row['comp_earnhead2_pf'] == False:
      ehead2_pf = 0
    elif row['comp_earnhead2_pf'] == True:
      ehead2_pf = 1
    elif row['comp_earnhead2_pf'] == None:
      ehead2_pf = 0
      
    if row['comp_earnhead2_esi'] == False:
      ehead2_esi = 0
    elif row['comp_earnhead2_esi'] == True:
      ehead2_esi = 1
    elif row['comp_earnhead2_esi'] == None:
      ehead2_esi = 0  

    if row['comp_earnhead2_pt'] == False:
      ehead2_pt = 0
    elif row['comp_earnhead2_pt'] == True:
      ehead2_pt = 1
    elif row['comp_earnhead2_pt'] == None:
      ehead2_pt = 0 
      
    if row['comp_earnhead2_it'] == False:
      ehead2_it = 0
    elif row['comp_earnhead2_it'] == True:
      ehead2_it = 1
    elif row['comp_earnhead2_it'] == None:
      ehead2_it = 0

    if row['comp_earnhead2_ot'] == False:
      ehead2_ot = 0
    elif row['comp_earnhead2_ot'] == True:
      ehead2_ot = 1
    elif row['comp_earnhead2_ot'] == None:
      ehead2_ot = 0   

    if row['comp_earnhead2_bonus'] == False:
      ehead2_bonus = 0
    elif row['comp_earnhead2_bonus'] == True:
      ehead2_bonus = 1
    elif row['comp_earnhead2_bonus'] == None:
      ehead2_bonus = 0    


    if row['comp_earnhead3_pf'] == False:
      ehead3_pf = 0
    elif row['comp_earnhead3_pf'] == True:
      ehead3_pf = 1
    elif row['comp_earnhead3_pf'] == None:
      ehead3_pf = 0
      
    if row['comp_earnhead3_esi'] == False:
      ehead3_esi = 0
    elif row['comp_earnhead3_esi'] == True:
      ehead3_esi = 1
    elif row['comp_earnhead3_esi'] == None:
      ehead3_esi = 0  

    if row['comp_earnhead3_pt'] == False:
      ehead3_pt = 0
    elif row['comp_earnhead3_pt'] == True:
      ehead3_pt = 1
    elif row['comp_earnhead3_pt'] == None:
      ehead3_pt = 0 
      
    if row['comp_earnhead3_it'] == False:
      ehead3_it = 0
    elif row['comp_earnhead3_it'] == True:
      ehead3_it = 1
    elif row['comp_earnhead3_it'] == None:
      ehead3_it = 0

    if row['comp_earnhead3_ot'] == False:
      ehead3_ot = 0
    elif row['comp_earnhead3_ot'] == True:
      ehead3_ot = 1
    elif row['comp_earnhead3_ot'] == None:
      ehead3_ot = 0   

    if row['comp_earnhead3_bonus'] == False:
      ehead3_bonus = 0
    elif row['comp_earnhead3_bonus'] == True:
      ehead3_bonus = 1
    elif row['comp_earnhead3_bonus'] == None:
      ehead3_bonus = 0    


    if row['comp_earnhead4_pf'] == False:
      ehead4_pf = 0
    elif row['comp_earnhead4_pf'] == True:
      ehead4_pf = 1
    elif row['comp_earnhead4_pf'] == None:
      ehead4_pf = 0
      
    if row['comp_earnhead4_esi'] == False:
      ehead4_esi = 0
    elif row['comp_earnhead4_esi'] == True:
      ehead4_esi = 1
    elif row['comp_earnhead4_esi'] == None:
      ehead4_esi = 0  

    if row['comp_earnhead4_pt'] == False:
      ehead4_pt = 0
    elif row['comp_earnhead4_pt'] == True:
      ehead4_pt = 1
    elif row['comp_earnhead4_pt'] == None:
      ehead4_pt = 0 
      
    if row['comp_earnhead4_it'] == False:
      ehead4_it = 0
    elif row['comp_earnhead4_it'] == True:
      ehead4_it = 1
    elif row['comp_earnhead4_it'] == None:
      ehead4_it = 0

    if row['comp_earnhead4_ot'] == False:
      ehead4_ot = 0
    elif row['comp_earnhead4_ot'] == True:
      ehead4_ot = 1
    elif row['comp_earnhead4_ot'] == None:
      ehead4_ot = 0   

    if row['comp_earnhead4_bonus'] == False:
      ehead4_bonus = 0
    elif row['comp_earnhead4_bonus'] == True:
      ehead4_bonus = 1
    elif row['comp_earnhead4_bonus'] == None:
      ehead4_bonus = 0    

    if row['comp_earnhead5_pf'] == False:
      ehead5_pf = 0
    elif row['comp_earnhead5_pf'] == True:
      ehead5_pf = 1
    elif row['comp_earnhead5_pf'] == None:
      ehead5_pf = 0
      
    if row['comp_earnhead5_esi'] == False:
      ehead5_esi = 0
    elif row['comp_earnhead5_esi'] == True:
      ehead5_esi = 1
    elif row['comp_earnhead5_esi'] == None:
      ehead5_esi = 0  

    if row['comp_earnhead5_pt'] == False:
      ehead5_pt = 0
    elif row['comp_earnhead5_pt'] == True:
      ehead5_pt = 1
    elif row['comp_earnhead5_pt'] == None:
      ehead5_pt = 0 
      
    if row['comp_earnhead5_it'] == False:
      ehead5_it = 0
    elif row['comp_earnhead5_it'] == True:
      ehead5_it = 1
    elif row['comp_earnhead5_it'] == None:
      ehead5_it = 0

    if row['comp_earnhead5_ot'] == False:
      ehead5_ot = 0
    elif row['comp_earnhead5_ot'] == True:
      ehead5_ot = 1
    elif row['comp_earnhead5_ot'] == None:
      ehead5_ot = 0   

    if row['comp_earnhead5_bonus'] == False:
      ehead5_bonus = 0
    elif row['comp_earnhead5_bonus'] == True:
      ehead5_bonus = 1
    elif row['comp_earnhead5_bonus'] == None:
      ehead5_bonus = 0    


    if row['comp_earnhead6_pf'] == False:
      ehead6_pf = 0
    elif row['comp_earnhead6_pf'] == True:
      ehead6_pf = 1
    elif row['comp_earnhead6_pf'] == None:
      ehead6_pf = 0
      
    if row['comp_earnhead6_esi'] == False:
      ehead6_esi = 0
    elif row['comp_earnhead6_esi'] == True:
      ehead6_esi = 1
    elif row['comp_earnhead6_esi'] == None:
      ehead6_esi = 0  

    if row['comp_earnhead6_pt'] == False:
      ehead6_pt = 0
    elif row['comp_earnhead6_pt'] == True:
      ehead6_pt = 1
    elif row['comp_earnhead6_pt'] == None:
      ehead6_pt = 0 
      
    if row['comp_earnhead6_it'] == False:
      ehead6_it = 0
    elif row['comp_earnhead6_it'] == True:
      ehead6_it = 1
    elif row['comp_earnhead6_it'] == None:
      ehead6_it = 0

    if row['comp_earnhead6_ot'] == False:
      ehead6_ot = 0
    elif row['comp_earnhead6_ot'] == True:
      ehead6_ot = 1
    elif row['comp_earnhead6_ot'] == None:
      ehead6_ot = 0   

    if row['comp_earnhead6_bonus'] == False:
      ehead6_bonus = 0
    elif row['comp_earnhead6_bonus'] == True:
      ehead6_bonus = 1
    elif row['comp_earnhead6_bonus'] == None:
      ehead6_bonus = 0    

    if row['comp_earnhead7_pf'] == False:
      ehead7_pf = 0
    elif row['comp_earnhead7_pf'] == True:
      ehead7_pf = 1
    elif row['comp_earnhead7_pf'] == None:
      ehead7_pf = 0
      
    if row['comp_earnhead7_esi'] == False:
      ehead7_esi = 0
    elif row['comp_earnhead7_esi'] == True:
      ehead7_esi = 1
    elif row['comp_earnhead7_esi'] == None:
      ehead7_esi = 0  

    if row['comp_earnhead7_pt'] == False:
      ehead7_pt = 0
    elif row['comp_earnhead7_pt'] == True:
      ehead7_pt = 1
    elif row['comp_earnhead7_pt'] == None:
      ehead7_pt = 0 
      
    if row['comp_earnhead7_it'] == False:
      ehead7_it = 0
    elif row['comp_earnhead7_it'] == True:
      ehead7_it = 1
    elif row['comp_earnhead7_it'] == None:
      ehead7_it = 0

    if row['comp_earnhead7_ot'] == False:
      ehead7_ot = 0
    elif row['comp_earnhead7_ot'] == True:
      ehead7_ot = 1
    elif row['comp_earnhead7_ot'] == None:
      ehead7_ot = 0   

    if row['comp_earnhead7_bonus'] == False:
      ehead7_bonus = 0
    elif row['comp_earnhead7_bonus'] == True:
      ehead7_bonus = 1
    elif row['comp_earnhead7_bonus'] == None:
      ehead7_bonus = 0 

    if row['comp_earnhead8_pf'] == False:
      ehead8_pf = 0
    elif row['comp_earnhead8_pf'] == True:
      ehead8_pf = 1
    elif row['comp_earnhead8_pf'] == None:
      ehead8_pf = 0
      
    if row['comp_earnhead8_esi'] == False:
      ehead8_esi = 0
    elif row['comp_earnhead8_esi'] == True:
      ehead8_esi = 1
    elif row['comp_earnhead8_esi'] == None:
      ehead8_esi = 0  

    if row['comp_earnhead8_pt'] == False:
      ehead8_pt = 0
    elif row['comp_earnhead8_pt'] == True:
      ehead8_pt = 1
    elif row['comp_earnhead8_pt'] == None:
      ehead8_pt = 0 
      
    if row['comp_earnhead8_it'] == False:
      ehead8_it = 0
    elif row['comp_earnhead8_it'] == True:
      ehead8_it = 1
    elif row['comp_earnhead8_it'] == None:
      ehead8_it = 0

    if row['comp_earnhead8_ot'] == False:
      ehead8_ot = 0
    elif row['comp_earnhead8_ot'] == True:
      ehead8_ot = 1
    elif row['comp_earnhead8_ot'] == None:
      ehead8_ot = 0   

    if row['comp_earnhead8_bonus'] == False:
      ehead8_bonus = 0
    elif row['comp_earnhead8_bonus'] == True:
      ehead8_bonus = 1
    elif row['comp_earnhead8_bonus'] == None:
      ehead8_bonus = 0 

    if row['comp_earnhead9_pf'] == False:
      ehead9_pf = 0
    elif row['comp_earnhead9_pf'] == True:
      ehead9_pf = 1
    elif row['comp_earnhead9_pf'] == None:
      ehead9_pf = 0
      
    if row['comp_earnhead9_esi'] == False:
      ehead9_esi = 0
    elif row['comp_earnhead9_esi'] == True:
      ehead9_esi = 1
    elif row['comp_earnhead9_esi'] == None:
      ehead9_esi = 0  

    if row['comp_earnhead9_pt'] == False:
      ehead9_pt = 0
    elif row['comp_earnhead9_pt'] == True:
      ehead9_pt = 1
    elif row['comp_earnhead9_pt'] == None:
      ehead9_pt = 0 
      
    if row['comp_earnhead9_it'] == False:
      ehead9_it = 0
    elif row['comp_earnhead9_it'] == True:
      ehead9_it = 1
    elif row['comp_earnhead9_it'] == None:
      ehead9_it = 0

    if row['comp_earnhead9_ot'] == False:
      ehead9_ot = 0
    elif row['comp_earnhead9_ot'] == True:
      ehead9_ot = 1
    elif row['comp_earnhead9_ot'] == None:
      ehead9_ot = 0   

    if row['comp_earnhead9_bonus'] == False:
      ehead9_bonus = 0
    elif row['comp_earnhead9_bonus'] == True:
      ehead9_bonus = 1
    elif row['comp_earnhead9_bonus'] == None:
      ehead9_bonus = 0 

    if row['comp_earnhead10_pf'] == False:
      ehead10_pf = 0
    elif row['comp_earnhead10_pf'] == True:
      ehead10_pf = 1
    elif row['comp_earnhead10_pf'] == None:
      ehead10_pf = 0
      
    if row['comp_earnhead10_esi'] == False:
      ehead10_esi = 0
    elif row['comp_earnhead10_esi'] == True:
      ehead10_esi = 1
    elif row['comp_earnhead10_esi'] == None:
      ehead10_esi = 0  

    if row['comp_earnhead10_pt'] == False:
      ehead10_pt = 0
    elif row['comp_earnhead10_pt'] == True:
      ehead10_pt = 1
    elif row['comp_earnhead10_pt'] == None:
      ehead10_pt = 0 
      
    if row['comp_earnhead10_it'] == False:
      ehead10_it = 0
    elif row['comp_earnhead10_it'] == True:
      ehead10_it = 1
    elif row['comp_earnhead10_it'] == None:
      ehead10_it = 0

    if row['comp_earnhead10_ot'] == False:
      ehead10_ot = 0
    elif row['comp_earnhead10_ot'] == True:
      ehead10_ot = 1
    elif row['comp_earnhead10_ot'] == None:
      ehead10_ot = 0   

    if row['comp_earnhead10_bonus'] == False:
      ehead10_bonus = 0
    elif row['comp_earnhead10_bonus'] == True:
      ehead10_bonus = 1
    elif row['comp_earnhead10_bonus'] == None:
      ehead10_bonus = 0

    if row['comp_bonus_pt_included'] == False:
      bonus_pt_included = 0
    elif row['comp_bonus_pt_included'] == True:
      bonus_pt_included = 1
    elif row['comp_bonus_pt_included'] == None:
      bonus_pt_included = 0
    
    csv_row = ["[496577,781197072]",row["comp_id"], row["comp_code"], row["comp_name"], row["comp_addr1"],
              row["comp_addr2"], row["comp_pf_number"], row["comp_addr3"],row["comp_esi_number"],row["comp_pto_circle"],
              row["comp_emp_pfrate"],row["comp_empr_fpfrate"],row["comp_pf_admin"],row["comp_pf_edli"],
              row["comp_mgmt_pf_lt"],row["comp_mgmt_fpf_lt"],row["comp_esi_sal_lt"],row["comp_pts1_from"],
              row["comp_pts1_to"],row["comp_pts1_pt"],row["comp_pts2_from"],row["comp_pts2_to"],row["comp_pts2_pt"],
              row["comp_pts3_from"],row["comp_pts3_to"],row["comp_pts3_pt"],row["comp_ded1"],row["comp_ded2"],
              row["comp_ded3"],row["comp_ded4"],row["comp_earn_head1"],ehead1_pf,ehead1_pt,
              ehead1_it,ehead1_ot,ehead1_bonus,row["comp_earn_head2"],
              ehead2_pf,ehead2_esi,ehead2_pt,ehead2_it,
              ehead2_ot,ehead2_bonus,row["comp_earn_head3"],ehead3_pf,
              ehead3_esi,ehead3_pt,ehead3_it,ehead3_ot,
              ehead3_bonus,row["comp_earn_head4"],ehead4_pf,ehead4_esi,
              ehead4_pt,ehead4_it,ehead4_ot,ehead4_bonus,
              row["comp_earn_head5"],ehead5_pf,ehead5_esi,ehead5_pt,
              ehead5_it,ehead5_ot,ehead5_bonus,row["comp_earn_head6"],
              ehead6_pf,ehead6_esi,ehead6_pt,ehead6_it,
              ehead6_ot,ehead6_bonus,row["comp_earn_head7"],ehead7_pf,
              ehead7_esi,ehead7_pt,ehead7_it,ehead7_ot,
              ehead7_bonus,row["comp_earn_head8"],ehead8_pf,ehead8_esi,
              ehead8_pt,ehead8_it,ehead8_ot,ehead8_bonus,
              row["comp_earn_head9"],ehead9_pf,ehead9_esi,ehead9_pt,
              ehead9_it,ehead9_ot,ehead9_bonus,row["comp_earn_head10"],
              ehead10_pf,ehead10_esi,ehead10_pt,ehead10_ot,
              ehead10_it,ehead10_bonus,ehead1_esi,row["comp_bonus_from"],
              row["comp_bonus_to"],row["comp_bonus_percentage"],row["comp_bonus_limit"],bonus_pt_included,
              row["comp_leave_head1"],row["comp_leave_head2"],row["comp_leave_head3"],row["comp_loan_head1"],
              row["comp_loan_head2"],row["comp_pay_date"]]  
    csv_rows.append(csv_row)

  df = pd.DataFrame(csv_rows, columns=["ID","comp_id","comp_code","comp_name","comp_addr1","comp_addr2",
            "comp_pf_number","comp_addr3","comp_esi_number","comp_pto_circle",
            "comp_emp_pfrate","comp_empr_fpfrate","comp_pf_admin","comp_pf_edli",
            "comp_mgmt_pf_lt","comp_mgmt_fpf_lt","comp_esi_sal_lt","comp_pts1_from",
            "comp_pts1_to","comp_pts1_pt","comp_pts2_from","comp_pts2_to","comp_pts2_pt",
            "comp_pts3_from","comp_pts3_to","comp_pts3_pt","comp_ded1","comp_ded2",
            "comp_ded3","comp_ded4","comp_earn_head1","comp_earnhead1_pf","comp_earnhead1_pt",
            "comp_earnhead1_it","comp_earnhead1_ot","comp_earnhead1_bonus","comp_earn_head2",
            "comp_earnhead2_pf","comp_earnhead2_esi","comp_earnhead2_pt","comp_earnhead2_it",
            "comp_earnhead2_ot","comp_earnhead2_bonus","comp_earn_head3","comp_earnhead3_pf",
            "comp_earnhead3_esi","comp_earnhead3_pt","comp_earnhead3_it","comp_earnhead3_ot",
            "comp_earnhead3_bonus","comp_earn_head4","comp_earnhead4_pf","comp_earnhead4_esi",
            "comp_earnhead4_pt","comp_earnhead4_it","comp_earnhead4_ot","comp_earnhead4_bonus",
            "comp_earn_head5","comp_earnhead5_pf","comp_earnhead5_esi","comp_earnhead5_pt",
            "comp_earnhead5_it","comp_earnhead5_ot","comp_earnhead5_bonus","comp_earn_head6",
            "comp_earnhead6_pf","comp_earnhead6_esi","comp_earnhead6_pt","comp_earnhead6_it",
            "comp_earnhead6_ot","comp_earnhead6_bonus","comp_earn_head7","comp_earnhead7_pf",
            "comp_earnhead7_esi","comp_earnhead7_pt","comp_earnhead7_it","comp_earnhead7_ot",
            "comp_earnhead7_bonus","comp_earn_head8","comp_earnhead8_pf","comp_earnhead8_esi",
            "comp_earnhead8_pt","comp_earnhead8_it","comp_earnhead8_ot","comp_earnhead8_bonus",
            "comp_earn_head9","comp_earnhead9_pf","comp_earnhead9_esi","comp_earnhead9_pt",
            "comp_earnhead9_it","comp_earnhead9_ot","comp_earnhead9_bonus","comp_earn_head10",
            "comp_earnhead10_pf","comp_earnhead10_esi","comp_earnhead10_pt","comp_earnhead10_ot",
            "comp_earnhead10_it","comp_earnhead10_bonus","comp_earnhead1_esi","comp_bonus_from",
            "comp_bonus_to","comp_bonus_percentage","comp_bonus_limit","comp_bonus_pt_included",
            "comp_leave_head1","comp_leave_head2","comp_leave_head3","comp_loan_head1",
            "comp_loan_head2","comp_pay_date"])
  df.to_csv('company.csv',index=False)
  df_media = anvil.media.from_file('company.csv', 'csv', 'company.csv')
  return df_media


@anvil.server.callable
def get_all_password_download():
  data_table = app_tables.password.search()
  csv_rows = []
  un = None
  pw = None
  
  for row in data_table:
    csv_row = [row["pass_id"],row["pass_code"], row["pass_comp_code"], row["username"], row["password"]]
    csv_rows.append(csv_row)
  df = pd.DataFrame(csv_rows, columns=["pass_id","pass_code","pass_comp_code","username","password"])
  df.to_csv('password.csv',index=False)
  df_media = anvil.media.from_file('password.csv', 'csv', 'password.csv')
  return df_media

@anvil.server.callable
def get_all_trans_date_download():
  data_table = app_tables.trans_date.search()
  csv_rows = []
  
  for row in data_table:
    csv_row = [row["trdate_comp_code"], row["tr_date"], row["tr_days"], row['tr_sundays'], row['tr_end_date'], row['tr_id']]
    csv_rows.append(csv_row)
  df = pd.DataFrame(csv_rows, columns=["trdate_comp_code","tr_date","tr_days",'tr_sundays','tr_end_date','tr_id'])
  df.to_csv('trans_date.csv',index=False)
  df_media = anvil.media.from_file('trans_date.csv', 'csv', 'trans_date.csv')
  return df_media

@anvil.server.callable
def get_all_employee_download():
  data_table = app_tables.employee.search()
  csv_rows = []
  
  pf_contribution  = None
  esi_contribution  = None
  pt_contribution  = None
  it_contribution  = None
  
  for row in data_table:

    if row['emp_pf_contribution'] == False:
      pf_contribution = 0
    elif row['emp_pf_contribution'] == True:
      pf_contribution = 1
    elif row['emp_pf_contribution'] == None:
      pf_contribution = 0

    if row['emp_esi_contribution'] == False:
      esi_contribution = 0
    elif row['emp_esi_contribution'] == True:
      esi_contribution = 1
    elif row['emp_esi_contribution'] == None:
      esi_contribution = 0

    if row['emp_pt_contribution'] == False:
      pt_contribution = 0
    elif row['emp_pt_contribution'] == True:
      pt_contribution = 1
    elif row['emp_pt_contribution'] == None:
      pt_contribution = 0

    if row['emp_it_contribution'] == False:
      it_contribution = 0
    elif row['emp_it_contribution'] == True:
      it_contribution = 1
    elif row['emp_it_contribution'] == None:
      it_contribution = 0    

    photo_bytes = get_media_bytes(row['emp_photo'])
    # pdf_bytes = get_media_bytes(row['emp_pdf_docu1'])
      
    csv_row = [row["id"], row["emp_comp_code"], row["emp_code"], row["emp_name"], row["emp_hus_name"],
              row["emp_dob"], row["emp_doj"], row["emp_sex"], row["emp_type"],
              pf_contribution, row["emp_pf_number"],
              row["emp_pf_uan"], esi_contribution ,
              row["emp_esi_number"], 
              row["emp_esi_dispensary"], pt_contribution,
              row["emp_dept_code"], row["emp_dept_name"],row["emp_desi_code"],
              row["emp_desi_name"], it_contribution, row["emp_pan_number"],
              row["earn1"], row["earn2"], row["earn3"], row["earn4"], row["earn5"],
              row["earn6"], row["earn7"], row["earn8"], row["earn9"], row["earn10"],
              row["phone_number"], row["alt_phone_number"],row["email_address"],
              row["aadhar_number"],row["attn_bonus"],photo_bytes,row["total_fxd_salary"]]
    csv_rows.append(csv_row)
    
  df = pd.DataFrame(csv_rows, columns=["id", "emp_comp_code", "emp_code", "emp_name", "emp_hus_name",
              "emp_dob", "emp_doj", "emp_sex", "emp_type",
              "emp_pf_contribution", "emp_pf_number",
              "emp_pf_uan", "emp_esi_contribution" ,
              "emp_esi_number", 
              "emp_esi_dispensary", "emp_pt_contribution",
              "emp_dept_code", "emp_dept_name","emp_desi_code",
              "emp_desi_name", "emp_it_contribution", "emp_pan_number",
              "earn1", "earn2", "earn3", "earn4", "earn5",
              "earn6", "earn7", "earn8", "earn9", "earn10",
              "phone_number", "alt_phone_number","email_address",
              "aadhar_number","attn_bonus","emp_photo","total_fxd_salary"])
  
  df.to_csv('employee.csv',index=False)
  df_media = anvil.media.from_file('employee.csv', 'csv', 'employee.csv')
  return df_media

@anvil.server.callable
def get_all_department_download():
  data_table = app_tables.department.search()
  csv_rows = []
  
  for row in data_table:
    csv_row = [row["dept_id"], row["dept_code"], row["dept_comp_code"], row['dept_name']]
    csv_rows.append(csv_row)
  df = pd.DataFrame(csv_rows, columns=["dept_id","dept_comp_code","dept_code","dept_name"])
  df.to_csv('department.csv',index=False)
  df_media = anvil.media.from_file('department.csv', 'csv', 'department.csv')
  return df_media

@anvil.server.callable
def get_all_designation_download():
  data_table = app_tables.designation.search()
  csv_rows = []
  
  for row in data_table:
    csv_row = [row["desi_id"], row["desi_comp_code"], row["desi_code"], row['desi_name']]
    csv_rows.append(csv_row)
  df = pd.DataFrame(csv_rows, columns=["desi_id","desi_comp_code","desi_code","desi_name"])
  df.to_csv('designation.csv',index=False)
  df_media = anvil.media.from_file('designation.csv', 'csv', 'designation.csv')
  return df_media

@anvil.server.callable
def get_all_transaction_download():
  data_table = app_tables.transaction.search()
  csv_rows = []
  
  emppfc = None
  empesic = None
  empptc = None
  empitc = None
  
  for row in data_table:

    if row['trans_emppfc'] == False:
      emppfc = 0
    elif row['trans_emppfc'] == True:
      emppfc = 1
    elif row['trans_emppfc'] == None:
      emppfc = 0

    if row['trans_empesic'] == False:
      empesic = 0
    elif row['trans_empesic'] == True:
      empesic = 1
    elif row['trans_empesic'] == None:
     empesic = 0

    if row['trans_empptc'] == False:
      empptc = 0
    elif row['trans_empptc'] == True:
      empptc = 1
    elif row['trans_empptc'] == None:
     empptc = 0

    if row['trans_empitc'] == False:
      empitc = 0
    elif row['trans_empitc'] == True:
      empitc = 1
    elif row['trans_empitc'] == None:
     empitc = 0
    
    csv_row = [row["id"], row["trans_date"], row["trans_comp_code"], row['trans_empid'], row['trans_empname'],
              row["trans_father_husband"], row["trans_empsex"], row["trans_empdob"],
              row["trans_empdoj"], row["trans_emptype"], row["trans_deptcode"],
              row["trans_deptname"], row["trans_desicode"], row["trans_desiname"],
              emppfc, row["trans_emppfno"], row["trans_emp_pfuan"],
              empesic, row["trans_empesino"],row["trans_empdispensary"],
              empptc, empitc, row["trans_emppan"],
              row["trans_mandays"], row["trans_wo"], row["trans_ph"],
              row["trans_layoff"], row["trans_absent"], row["trans_leave1"],
              row["trans_leave2"], row["trans_leave3"], row["trans_othrs"],
              row["trans_inchrs"], row["trans_ded1"], row["trans_ded2"],
              row["trans_ded3"], row["trans_ded4"], row["trans_loan1"],
              row["trans_loan2"], row["trans_adv"], row["trans_tds"],
              row["trans_pfvol"], row["trans_lic"], row["trans_arr_pf"],
              row["trans_earn1"], row["trans_earn2"], row["trans_earn3"],
              row["trans_earn4"], row["trans_earn5"], row["trans_earn6"],
              row["trans_earn7"], row["trans_earn8"], row["trans_earn9"],
              row["trans_earn10"], row["trans_earn_earn1"],row["trans_earn_earn2"],
              row["trans_earn_earn3"], row["trans_earn_earn4"], row["trans_earn_earn5"],
              row["trans_earn_earn6"], row["trans_earn_earn7"], row["trans_earn_earn8"],
              row["trans_earn_earn9"], row["trans_earn_earn10"], row["trans_phone_number"],
              row["trans_alt_phone_number"], row["trans_email_address"], row["trans_aadhar_number"],
              row["trans_attn_bonus"], row["fxd_earn_gross"], row["earn_pf_salary"], row["earn_fpf_salary"],
              row["earn_esi_salary"], row["earn_pt_salary"], row["earn_ot_salary"], row["earn_it_salary"],
              row["earn_bonus_salary"], row["pf_amt"], row["fpf_amt"], row["esi_amt"],
              row["pt_amt"],  row["ot_amt"], row["it_or_tds_amt"], row["bonus_amt"], row["trans_paid_days"],
              row["trans_earn_attn_bonus"]]
    csv_rows.append(csv_row)
  df = pd.DataFrame(csv_rows, columns=["id", "trans_date","trans_comp_code",'trans_empid', 'trans_empname',
              "trans_father_husband", "trans_empsex", "trans_empdob",
              "trans_empdoj", "trans_emptype", "trans_deptcode",
              "trans_deptname", "trans_desicode", "trans_desiname",
              "trans_emppfc", "trans_emppfno", "trans_emp_pfuan",
              "trans_empesic", "trans_empesino","trans_empdispensary",
              "trans_empptc", "trans_empitc", "trans_emppan",
              "trans_mandays", "trans_wo", "trans_ph",
              "trans_layoff", "trans_absent", "trans_leave1",
              "trans_leave2", "trans_leave3", "trans_othrs",
              "trans_inchrs", "trans_ded1", "trans_ded2",
              "trans_ded3", "trans_ded4", "trans_loan1",
              "trans_loan2", "trans_adv", "trans_tds",
              "trans_pfvol", "trans_lic", "trans_arr_pf",
              "trans_earn1", "trans_earn2", "trans_earn3",
              "trans_earn4", "trans_earn5", "trans_earn6",
              "trans_earn7", "trans_earn8", "trans_earn9",
              "trans_earn10", "trans_earn_earn1","trans_earn_earn2",
              "trans_earn_earn3", "trans_earn_earn4", "trans_earn_earn5",
              "trans_earn_earn6", "trans_earn_earn7", "trans_earn_earn8",
              "trans_earn_earn9", "trans_earn_earn10", "trans_phone_number",
              "trans_alt_phone_number", "trans_email_address", "trans_aadhar_number",
              "trans_attn_bonus", "fxd_earn_gross", "earn_pf_salary", "earn_fpf_salary",
              "earn_esi_salary", "earn_pt_salary", "earn_ot_salary", "earn_it_salary",
              "earn_bonus_salary", "pf_amt", "fpf_amt", "esi_amt",
              "pt_amt",  "ot_amt", "it_or_tds_amt", "bonus_amt","trans_paid_days",
              "trans_earn_attn_bonus"])
  
  df.to_csv('transaction.csv',index=False)
  df_media = anvil.media.from_file('transaction.csv', 'csv', 'transaction.csv')
  return df_media

@anvil.server.callable
def get_all_bank_download():
  data_table = app_tables.bank.search()
  csv_rows = []
  
  for row in data_table:
    csv_row = [row["bank_id"],row["bank_comp_code"], row["bank_code"], row['bank_name'],row['bank_addr1'],
              row['bank_addr2'], row['bank_addr3'], row['bank_ifsc']]
    csv_rows.append(csv_row)
  df = pd.DataFrame(csv_rows, columns=["bank_id","bank_comp_code", "bank_code", 'bank_name','bank_addr1',
              'bank_addr2', 'bank_addr3', 'bank_ifsc'])
  df.to_csv('bank.csv',index=False)
  df_media = anvil.media.from_file('bank.csv', 'csv', 'bank.csv')
  return df_media


def get_media_bytes(media_object):
  if media_object:
    return base64.b64encode(media_object.get_bytes()).decode('utf-8')
  else:
    return None

