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

@anvil.server.http_endpoint('/:name')
def get_doc(name):
  return app_tables.pdfs.get(emp_pdf_docu1_name=name)['emp_pdf_docu1']

@anvil.server.callable
def get_url(name):
  url = anvil.server.get_api_origin() +'/'+name
  return url