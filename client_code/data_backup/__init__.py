from ._anvil_designer import data_backupTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb

class data_backup(data_backupTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.label_3.text = gvarb.g_comname+' '+gvarb.g_mode+" for the month of "+gvarb.g_transdate.strftime("%B %Y")
   
    data = anvil.server.call('get_all_companies_download')
    download(data)
    data = anvil.server.call('get_all_password_download')
    download(data)
    data = anvil.server.call('get_all_trans_date_download')
    download(data)
    data = anvil.server.call('get_all_employee_download')
    download(data)
    data = anvil.server.call('get_all_department_download')
    download(data)
    data = anvil.server.call('get_all_designation_download')
    download(data)
    data = anvil.server.call('get_all_transaction_download')
    download(data)
    data = anvil.server.call('get_all_bank_download')
    download(data)

    # data = anvil.server.call('get_all_test_download')
    # download(data)
    
  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')

