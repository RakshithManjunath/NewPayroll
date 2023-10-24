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

@anvil.server.callable
def earn_cal(trans_comp_code,trans_empid):
  row = app_tables.transaction.search(trans_comp_code=trans_comp_code,trans_empid=trans_empid)[0]
  paid_days = row['trans_paid_days']
  row_trans_date = app_tables.trans_date.search()[0]
  no_of_days_in_month = row_trans_date['tr_days']
  
  earning1 = row['trans_earn1'] 
  ee1 = round(((earning1 / no_of_days_in_month) * paid_days),2)
  earning2 = row['trans_earn2'] 
  ee2 = round(((earning2 / no_of_days_in_month) * paid_days),2)
  earning3 = row['trans_earn3'] 
  ee3 = round(((earning3 / no_of_days_in_month) * paid_days),2) 
  earning4 = row['trans_earn4'] 
  ee4 = round(((earning4 / no_of_days_in_month) * paid_days),2) 
  earning5 = row['trans_earn5'] 
  ee5 = round(((earning5 / no_of_days_in_month) * paid_days),2) 
  earning6 = row['trans_earn6'] 
  ee6 = round(((earning6 / no_of_days_in_month) * paid_days),2)
  earning7 = row['trans_earn7'] 
  ee7 = round(((earning7 / no_of_days_in_month) * paid_days),2)
  earning8 = row['trans_earn8'] 
  ee8 = round(((earning8 / no_of_days_in_month) * paid_days),2) 
  earning9 = row['trans_earn9'] 
  ee9 = round(((earning9 / no_of_days_in_month) * paid_days),2) 
  earning10 = row['trans_earn10'] 
  ee10 = round(((earning10 / no_of_days_in_month) * paid_days),2) 

  return ee1,ee2,ee3,ee4,ee5,ee6,ee7,ee8,ee9,ee10

@anvil.server.callable
def update_earn(trans_comp_code,trans_empid,trans_earn_earn1,trans_earn_earn2,trans_earn_earn3,
                trans_earn_earn4,trans_earn_earn5,trans_earn_earn6,trans_earn_earn7,trans_earn_earn8,
                trans_earn_earn9,trans_earn_earn10):
  row = app_tables.transaction.search(trans_comp_code=trans_comp_code,trans_empid=trans_empid)[0]
  row.update(trans_earn_earn1=trans_earn_earn1)
  row.update(trans_earn_earn2=trans_earn_earn2)
  row.update(trans_earn_earn3=trans_earn_earn3)
  row.update(trans_earn_earn4=trans_earn_earn4)
  row.update(trans_earn_earn5=trans_earn_earn5)
  row.update(trans_earn_earn6=trans_earn_earn6)
  row.update(trans_earn_earn7=trans_earn_earn7)
  row.update(trans_earn_earn8=trans_earn_earn8)
  row.update(trans_earn_earn9=trans_earn_earn9)
  row.update(trans_earn_earn10=trans_earn_earn10)

  ##############################################################################
  ################################ Start Attendeance Bonus #####################
  ##############################################################################
@anvil.server.callable
def attn_bonus(trans_comp_code,trans_empid):
  row = app_tables.transaction.search(trans_comp_code=trans_comp_code,trans_empid=trans_empid)[0]
  staff_worker = row['trans_emptype']
  fxd_attn_bonus = row['trans_attn_bonus']
  mandays = row['trans_mandays']
  weekly_off = row['trans_wo']
  paid_holiday = row['trans_ph']
  layoff = row['trans_layoff']
  absent = row['trans_absent']
  leave1 = row['trans_leave1']
  leave2 = row['trans_leave2']
  leave3 = row['trans_leave3']

  row_trans_date = app_tables.trans_date.search()[0]
  no_of_days_in_month = row_trans_date['tr_days']
  sundays = row_trans_date['tr_sundays']
  if (staff_worker == "Worker") :   ## only workers are eligible for attn bonus
  
    if (mandays + paid_holiday) >= (no_of_days_in_month - weekly_off) :
      ebonus = fxd_attn_bonus
    else:
      ebonus = 0
  else :
      ebonus = 0

  if ((leave1 + leave2 + leave3) > 0) : ## applied leave
    ebonus = 0 

  if (absent) : ## absent days are there
    ebonus = 0 
  
  return ebonus

@anvil.server.callable
def update_earn_att_bonus(trans_comp_code,trans_empid,trans_earn_attn_bonus):
  row = app_tables.transaction.search(trans_comp_code=trans_comp_code,trans_empid=trans_empid)[0]
  row.update(trans_earn_attn_bonus=trans_earn_attn_bonus)
  ##############################################################################
  ################################ End Attendeance Bonus #######################
  ##############################################################################

  ##############################################################################
  ################################ PF Calculation Start #######################
  ##############################################################################
@anvil.server.callable
def pf_calculaton(comp_code,trans_empid):
  row = app_tables.company.get(comp_code=comp_code,)
  eh1_pf = row['comp_earnhead1_pf']
  eh2_pf = row['comp_earnhead2_pf']
  eh3_pf = row['comp_earnhead3_pf']
  eh4_pf = row['comp_earnhead4_pf']
  eh5_pf = row['comp_earnhead5_pf']
  eh6_pf = row['comp_earnhead6_pf']
  eh7_pf = row['comp_earnhead7_pf']
  eh8_pf = row['comp_earnhead8_pf']
  eh9_pf = row['comp_earnhead9_pf']
  eh10_pf = row['comp_earnhead10_pf']
  pf_percentage = row['comp_emp_pfrate']
  fpf_percentage = row['comp_empr_fpfrate']
  comp_pf_limit = row['comp_mgmt_pf_lt']
  comp_fpf_limit = row['comp_mgmt_fpf_lt']
  row = app_tables.transaction.search(trans_comp_code=comp_code,trans_empid=trans_empid)[0]
  if row['trans_emppfc'] == True:
    pfsal = 0
    fxd_pfsal = 0
    pfamt = 0
    fpfamt = 0
    if eh1_pf == True:
      pfsal = row['trans_earn_earn1']
      fxd_pfsal  = row['trans_earn1']
    if eh2_pf == True:
      pfsal = pfsal + row['trans_earn_earn2']
      fxd_pfsal  = fxd_pfsal + row['trans_earn2']
    if eh3_pf == True:
      pfsal = pfsal + row['trans_earn_earn3']
      fxd_pfsal  = fxd_pfsal + row['trans_earn3']
    if eh4_pf == True:
      pfsal = pfsal + row['trans_earn_earn4']
      fxd_pfsal  = fxd_pfsal + row['trans_earn4']
    if eh5_pf == True:
      pfsal = pfsal + row['trans_earn_earn5']
      fxd_pfsal  = fxd_pfsal + row['trans_earn5']
    if eh6_pf == True:
      pfsal = pfsal + row['trans_earn_earn6']
      fxd_pfsal  = fxd_pfsal + row['trans_earn6']
    if eh7_pf == True:
      pfsal = pfsal + row['trans_earn_earn7']
      fxd_pfsal  = fxd_pfsal + row['trans_earn7']
    if eh8_pf == True:
      pfsal = pfsal + row['trans_earn_earn8']
      fxd_pfsal  = fxd_pfsal + row['trans_earn8']
    if eh9_pf == True:
      pfsal = pfsal + row['trans_earn_earn9']
      fxd_pfsal  = fxd_pfsal + row['trans_earn9']
    if eh10_pf == True:
      pfsal = pfsal + row['trans_earn_earn10']
      fxd_pfsal  = fxd_pfsal + row['trans_earn10']
  else:
    pfsal = 0

  pfamt = pfsal * (pf_percentage/100)
  fpfamt = pfsal * (fpf_percentage/100)

  return pfsal,pfamt,fpfamt

@anvil.server.callable
def update_pfsalary(trans_comp_code,trans_empid,earn_pf_salary,pf_amt,fpf_amt):
  row = app_tables.transaction.search(trans_comp_code=trans_comp_code,trans_empid=trans_empid)[0]
  row.update(earn_pf_salary = earn_pf_salary)
  row.update(pf_amt = pf_amt)
  row.update(fpf_amt = fpf_amt)
  ##############################################################################
  ################################ PF Calculation End    #######################
  ##############################################################################


  ##############################################################################
  ################################ ESI Calculation Start #######################
  ##############################################################################
@anvil.server.callable
def esi_calculaton(comp_code,trans_empid):
  row = app_tables.company.get(comp_code=comp_code,)
  eh1_esi = row['comp_earnhead1_esi']
  eh2_esi = row['comp_earnhead2_esi']
  eh3_esi = row['comp_earnhead3_esi']
  eh4_esi = row['comp_earnhead4_esi']
  eh5_esi = row['comp_earnhead5_esi']
  eh6_esi = row['comp_earnhead6_esi']
  eh7_esi = row['comp_earnhead7_esi']
  eh8_esi = row['comp_earnhead8_esi']
  eh9_esi = row['comp_earnhead9_esi']
  eh10_esi = row['comp_earnhead10_esi']
  row = app_tables.transaction.search(trans_comp_code=comp_code,trans_empid=trans_empid)[0]
  if row['trans_empesic'] == True:
    esisal = 0
    if eh1_esi == True:
      esisal = row['trans_earn_earn1']
    if eh2_esi == True:
      esisal = esisal + row['trans_earn_earn2']
    if eh3_esi == True:
      esisal = esisal + row['trans_earn_earn3']
    if eh4_esi == True:
      esisal = esisal + row['trans_earn_earn4']
    if eh5_esi == True:
      esisal = esisal + row['trans_earn_earn5']    
    if eh6_esi == True:
      esisal = esisal + row['trans_earn_earn6']
    if eh7_esi == True:
      esisal = esisal + row['trans_earn_earn7']
    if eh8_esi == True:
      esisal = esisal + row['trans_earn_earn8']
    if eh9_esi == True:
      esisal = esisal + row['trans_earn_earn9']
    if eh10_esi == True:
      esisal = esisal + row['trans_earn_earn10']    
  else:
    esisal = 0
    
  return esisal

@anvil.server.callable
def update_esisalary(trans_comp_code,trans_empid,earn_esi_salary):
  row = app_tables.transaction.search(trans_comp_code=trans_comp_code,trans_empid=trans_empid)[0]
  row.update(earn_esi_salary = earn_esi_salary)
  ##############################################################################
  ################################ ESI Calculation End    #######################
  ##############################################################################

  ##############################################################################
  ################################ PT Calculation Start #######################
  ##############################################################################
@anvil.server.callable
def pt_calculaton(comp_code,trans_empid):
  row = app_tables.company.get(comp_code=comp_code,)
  eh1_pt = row['comp_earnhead1_pt']
  eh2_pt = row['comp_earnhead2_pt']
  eh3_pt = row['comp_earnhead3_pt']
  eh4_pt = row['comp_earnhead4_pt']
  eh5_pt = row['comp_earnhead5_pt']
  eh6_pt = row['comp_earnhead6_pt']
  eh7_pt = row['comp_earnhead7_pt']
  eh8_pt = row['comp_earnhead8_pt']
  eh9_pt = row['comp_earnhead9_pt']
  eh10_pt = row['comp_earnhead10_pt']
  row = app_tables.transaction.search(trans_comp_code=comp_code,trans_empid=trans_empid)[0]
  if row['trans_empptc'] == True:
    ptsal = 0
    if eh1_pt == True:
      ptsal = row['trans_earn_earn1']
    if eh2_pt == True:
      ptsal = ptsal + row['trans_earn_earn2']
    if eh3_pt == True:
      ptsal = ptsal + row['trans_earn_earn3']
    if eh4_pt == True:
      ptsal = ptsal + row['trans_earn_earn4']
    if eh5_pt == True:
      ptsal = ptsal + row['trans_earn_earn5']
    if eh6_pt == True:
      ptsal = ptsal + row['trans_earn_earn6']
    if eh7_pt == True:
      ptsal = ptsal + row['trans_earn_earn7']
    if eh8_pt == True:
      ptsal = ptsal + row['trans_earn_earn8']
    if eh9_pt == True:
      ptsal = ptsal + row['trans_earn_earn9']
    if eh10_pt == True:
      ptsal = ptsal + row['trans_earn_earn10']
  else:
    ptsal = 0
    
  return ptsal  

@anvil.server.callable
def update_ptsalary(trans_comp_code,trans_empid,earn_pt_salary):
  row = app_tables.transaction.search(trans_comp_code=trans_comp_code,trans_empid=trans_empid)[0]
  row.update(earn_pt_salary = earn_pt_salary)
 ##############################################################################
  ################################ PT Calculation END #######################
  ##############################################################################

  ##############################################################################
  ###################### OverTime [OT] Calculation Start #######################
  ##############################################################################
@anvil.server.callable
def ot_calculaton(comp_code,trans_empid):
  row = app_tables.company.get(comp_code=comp_code,)
  eh1_ot = row['comp_earnhead1_ot']
  eh2_ot = row['comp_earnhead2_ot']
  eh3_ot = row['comp_earnhead3_ot']
  eh4_ot = row['comp_earnhead4_ot']
  eh5_ot = row['comp_earnhead5_ot']
  eh6_ot = row['comp_earnhead6_ot']
  eh7_ot = row['comp_earnhead7_ot']
  eh8_ot = row['comp_earnhead8_ot']
  eh9_ot = row['comp_earnhead9_ot']
  eh10_ot = row['comp_earnhead10_ot']
  
  row_trans_date = app_tables.trans_date.search()[0]
  no_of_days_in_month = row_trans_date['tr_days']
  
  row = app_tables.transaction.search(trans_comp_code=comp_code,trans_empid=trans_empid)[0]
  othrs = row['trans_othrs']
  otrate = 2.0
  otsal = 0
  if eh1_ot == True:
    otsal = row['trans_earn_earn1']
  if eh2_ot == True:
    otsal = otsal + row['trans_earn_earn2']
  if eh3_ot == True:
    otsal = otsal + row['trans_earn_earn3']
  if eh4_ot == True:
    otsal = otsal + row['trans_earn_earn4']
  if eh5_ot == True:
    otsal = otsal + row['trans_earn_earn5']
  if eh6_ot == True:
    otsal = otsal + row['trans_earn_earn6']
  if eh7_ot == True:
    otsal = otsal + row['trans_earn_earn7']
  if eh8_ot == True:
    otsal = otsal + row['trans_earn_earn8']
  if eh9_ot == True:
    otsal = otsal + row['trans_earn_earn9']
  if eh10_ot == True:
    otsal = otsal + row['trans_earn_earn10']

  ot_amt = round((((otsal/no_of_days_in_month) * othrs) *  otrate),0)
  
  return otsal,ot_amt  

@anvil.server.callable
def update_otsalary(trans_comp_code,trans_empid,earn_ot_salary,ot_amt):
  row = app_tables.transaction.search(trans_comp_code=trans_comp_code,trans_empid=trans_empid)[0]
  row.update(earn_ot_salary = earn_ot_salary)
  row.update(ot_amt = ot_amt)
  ##############################################################################
  ###################### OverTime [OT] Calculation End   #######################
  ##############################################################################

  ##############################################################################
  #################### Income Tax [IT] Calculation Start #######################
  ##############################################################################
@anvil.server.callable
def it_calculaton(comp_code,trans_empid):
  row = app_tables.company.get(comp_code=comp_code,)
  eh1_it = row['comp_earnhead1_it']
  eh2_it = row['comp_earnhead2_it']
  eh3_it = row['comp_earnhead3_it']
  eh4_it = row['comp_earnhead4_it']
  eh5_it = row['comp_earnhead5_it']
  eh6_it = row['comp_earnhead6_it']
  eh7_it = row['comp_earnhead7_it']
  eh8_it = row['comp_earnhead8_it']
  eh9_it = row['comp_earnhead9_it']
  eh10_it = row['comp_earnhead10_it']
  row = app_tables.transaction.search(trans_comp_code=comp_code,trans_empid=trans_empid)[0]
  if row['trans_empitc'] == True:
    itsal = 0
    if eh1_it == True:
      itsal = row['trans_earn_earn1']
    if eh2_it == True:
      itsal = itsal + row['trans_earn_earn2']
    if eh3_it == True:
      itsal = itsal + row['trans_earn_earn3']
    if eh4_it == True:
      itsal = itsal + row['trans_earn_earn4']
    if eh5_it == True:
      itsal = itsal + row['trans_earn_earn5']
    if eh6_it == True:
      itsal = itsal + row['trans_earn_earn6']
    if eh7_it == True:
      itsal = itsal + row['trans_earn_earn7']
    if eh8_it == True:
      itsal = itsal + row['trans_earn_earn8']
    if eh9_it == True:
      itsal = itsal + row['trans_earn_earn9']
    if eh10_it == True:
      itsal = itsal + row['trans_earn_earn10']
  else:
    itsal = 0
    
  return itsal

@anvil.server.callable
def update_itsalary(trans_comp_code,trans_empid,earn_it_salary):
  row = app_tables.transaction.search(trans_comp_code=trans_comp_code,trans_empid=trans_empid)[0]
  row.update(earn_it_salary = earn_it_salary)  
  ##############################################################################
  ####################  Income Tax [IT] Calculation End  #######################
  ##############################################################################

  ##############################################################################
  ####################  Bonus [Annual] Calculation Start #######################
  ##############################################################################
@anvil.server.callable
def bonus_calculaton(comp_code,trans_empid):
  row = app_tables.company.get(comp_code=comp_code,)
  eh1_bns = row['comp_earnhead1_bonus']
  eh2_bns = row['comp_earnhead2_bonus']
  eh3_bns = row['comp_earnhead3_bonus']
  eh4_bns = row['comp_earnhead4_bonus']
  eh5_bns = row['comp_earnhead5_bonus']
  eh6_bns = row['comp_earnhead6_bonus']
  eh7_bns = row['comp_earnhead7_bonus']
  eh8_bns = row['comp_earnhead8_bonus']
  eh9_bns = row['comp_earnhead9_bonus']
  eh10_bns = row['comp_earnhead10_bonus']
  bns_percentage = row['comp_bonus_percentage']
  row = app_tables.transaction.search(trans_comp_code=comp_code,trans_empid=trans_empid)[0]
  bns_sal = 0
  if eh1_bns == True:
     bns_sal = row['trans_earn_earn1']
  if eh2_bns == True:
     bns_sal =  bns_sal + row['trans_earn_earn2']
  if eh3_bns == True:
     bns_sal =  bns_sal + row['trans_earn_earn3']
  if eh4_bns == True:
     bns_sal =  bns_sal + row['trans_earn_earn4']
  if eh5_bns == True:
     bns_sal =  bns_sal + row['trans_earn_earn5']
  if eh6_bns == True:
     bns_sal =  bns_sal + row['trans_earn_earn6']
  if eh7_bns == True:
     bns_sal =  bns_sal + row['trans_earn_earn7']
  if eh8_bns == True:
     bns_sal =  bns_sal + row['trans_earn_earn8']
  if eh9_bns == True:
     bns_sal =  bns_sal + row['trans_earn_earn9']
  if eh10_bns == True:
     bns_sal =  bns_sal + row['trans_earn_earn10']

  bonus_amount = round(((bns_percentage/100) * bns_sal),0)
  
  return bns_sal,bonus_amount

@anvil.server.callable
def update_bonus_salary(trans_comp_code,trans_empid,bns_sal,bonus_amt):
  row = app_tables.transaction.search(trans_comp_code=trans_comp_code,trans_empid=trans_empid)[0]
  row.update(earn_bonus_salary = bns_sal)
  row.update(bonus_amt = bonus_amt)
  ##############################################################################
  ####################   Bonus [Annual] Calculation End  #######################
  ##############################################################################

  ##############################################################################
  #####################  Gross salary calculation Start ########################
  ##############################################################################




  ##############################################################################
  #####################   Gross salary calculation End  ########################
  ##############################################################################