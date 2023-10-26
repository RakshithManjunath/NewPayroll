import anvil.files
from anvil.files import data_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

####### trans date #######
@anvil.server.callable
def cur_trans_date():
    return [(r["tr_date"]) for r in app_tables.trans_date.search()]

@anvil.server.callable
def cur_trans_date_update(next_initial_date, next_days, next_num_of_sundays, next_end_date):
  row = app_tables.trans_date.get(tr_id=1)
  row.update(tr_date=next_initial_date)
  row.update(tr_days=next_days)
  row.update(tr_sundays=next_num_of_sundays)
  row.update(tr_end_date=next_end_date)

@anvil.server.callable
def new_trans_date(tr_date,tr_days,tr_sundays,tr_end_date,comcode):
  app_tables.trans_date.add_row(tr_date=tr_date,
                               tr_days=tr_days,
                               tr_sundays=tr_sundays,
                               tr_end_date=tr_end_date,
                               tr_id=1,
                               trdate_comp_code=comcode)
