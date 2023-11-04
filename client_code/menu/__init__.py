from ._anvil_designer import menuTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class menu(menuTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def open_login_page(self, **kwargs):
    anvil.users.logout()
    alert(f"You have logged out successfully...!")
    open_form('logform')

  def open_update_page(self, **kwargs):
    open_form('update_trans_date')

  def open_emp_add(self, **kwargs):
    open_form('emp_mast_add')

  def open_emp_chg(self, **kwargs):
    open_form('emp_change')

  def open_dept(self, **kwargs):
    open_form('dept')

  def open_desi(self, **kwargs):
    open_form('desi')

  def open_comp(self, **kwargs):
    open_form('comp_new')

  def open_comp_change(self, **kwargs):
    open_form('comp_change')
  
  def open_comp_more(self, **kwargs):
    open_form('comp_more')

  def open_bank(self, **kwargs):
    open_form('bank_add_change')

  def open_emp_more(self, **kwargs):
    open_form('emp_more1')

  def open_stat(self, **kwargs):
    open_form('statutary')

  def open_change_trans(self, **kwargs):
    open_form('emp_mon_trans_change')

  def open_view_trans(self, **kwargs):
    open_form('emp_trans_view')

  def open_data_backup(self, **kwargs):
    open_form('data_backup')

  def open_pass_add(self, **kwargs):
    open_form('pass_add')

  def open_report1_page(self, **kwargs):
    open_form('report_new')

  def open_complete(self, **kwargs):
    open_form('report_new')

  def open_trans(self, **kwargs):
    open_form('trans')