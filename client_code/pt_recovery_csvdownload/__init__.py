from ._anvil_designer import pt_recovery_csvdownloadTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import report_varb
from .. import gvarb

class pt_recovery_csvdownload(pt_recovery_csvdownloadTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

   # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print("pt recovery grid rows: ",report_varb.g_grid_rows)
    print("pt recovery grid cols: ",report_varb.g_grid_cols)
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>PF Recovery Statement</title>
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            h1 {
                font-size: 24px;
            }
            p {
                font-size: 16px;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }
            th, td {
                border: 1px solid #000;
                padding: 8px;
                text-align: left;
            }
        </style>
    </head>
    <body>
    <div class="content">
        <h1>PF Recovery Statement</h1>
        
        <p>Date: {{ trans_date }}</p>

        <h1>{{ company_name }}</h1>
     </div>

    <table>
        <thead>
            <tr>
                {% for column in grid_cols %}
                    <th>{{ column.title }}</th>
                {% endfor %}
            </tr>
        </thead>
        <tbody>
            {% for row in grid_rows %}
                <tr>
                    {% for column in grid_cols %}
                        <td>{{ row[column.data_key] }}</td>
                    {% endfor %}
                </tr>
            {% endfor %}
        </tbody>
    </table>
    </body>
    </html>
    """

    self.html_content = anvil.server.call('pt_recovery_html_report',html_template,
                                          report_varb.g_grid_rows,report_varb.g_grid_cols,
                                          gvarb.g_comname,gvarb.g_transdate)
    self.html = self.html_content

  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('report_new')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    csv = anvil.server.call('download_pt_recovery_csv',self.html_content)
    download(csv)

