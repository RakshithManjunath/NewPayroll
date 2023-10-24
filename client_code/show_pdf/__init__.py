from ._anvil_designer import show_pdfTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..pdf_viewer import pdf_viewer

class show_pdf(show_pdfTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def form_show(self, **event_args):
    """This method is called when the column panel is shown on the screen"""
    url = anvil.server.call('get_url', 'sample')
    print(url)
    self.column_panel_1.add_component(pdf_viewer(url=url))

