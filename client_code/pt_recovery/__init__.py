from ._anvil_designer import pt_recoveryTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import report_varb

class pt_recovery(pt_recoveryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.html='<b> This form has been changed </b>'

    self.html = """
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
        <h1>PF Recovery Statement</h1>
        
        <p>Date: [Date]</p>
        
        <h2>Employee Details</h2>
        <p><strong>Name:</strong> [Employee Name]</p>
        <p><strong>Employee ID:</strong> [Employee ID]</p>
        
        <h2>Recovery Details</h2>
        <table>
            <thead>
                <tr>
                    <th>Month</th>
                    <th>Contribution</th>
                    <th>Employer Share</th>
                    <th>Employee Share</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>[Month 1]</td>
                    <td>[Contribution 1]</td>
                    <td>[Employer Share 1]</td>
                    <td>[Employee Share 1]</td>
                </tr>
                <tr>
                    <td>[Month 2]</td>
                    <td>[Contribution 2]</td>
                    <td>[Employer Share 2]</td>
                    <td>[Employee Share 2]</td>
                </tr>
                <!-- Add more rows as needed -->
            </tbody>
        </table>
        
        <h2>Total Recovery</h2>
        <p><strong>Total Contribution:</strong> [Total Contribution]</p>
        <p><strong>Total Employer Share:</strong> [Total Employer Share]</p>
        <p><strong>Total Employee Share:</strong> [Total Employee Share]</p>
    </body>
    </html>
    """


    # Any code you write here will run before the form opens.
    print("pt recovery grid rows: ",report_varb.g_grid_rows)
    print("pt recovery grid cols: ",report_varb.g_grid_cols)
