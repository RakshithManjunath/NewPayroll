from ._anvil_designer import output_optionsTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import report_varb
from .. import gvarb
  
#self.label_1.text = gvarb.g_comname+' '+(gvarb.g_mode+" for the month of "+gvarb.g_transdate.strftime("%B %Y")).upper()

class output_options(output_optionsTemplate):
  def __init__(self, **properties):
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

    self.html_content = anvil.server.call('report_recovery_html_report',html_template,
                                          report_varb.g_grid_rows,report_varb.g_grid_cols,
                                          gvarb.g_comname,gvarb.g_transdate)
    self.html = self.html_content

    # self.col_panel = anvil.ColumnPanel()
    # flow_panel_emp_details = anvil.FlowPanel()
    # self.col_panel.add_component(flow_panel_emp_details)
    # flow_panel_emp_details.add_component(anvil.Button(text="Front",align="center"))
    # self.add_component(self.col_panel)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('report_new')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    pdf = anvil.server.call('download_report_recovery_pdf',self.html_content)
    download(pdf)

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    excel = anvil.server.call('download_report_recovery_excel',self.html_content,gvarb.g_comcode,gvarb.g_transdate)
    download(excel)

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    csv = anvil.server.call('download_report_recovery_csv',self.html_content)
    download(csv)
  
