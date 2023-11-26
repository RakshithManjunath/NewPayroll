from ._anvil_designer import pf_recoveryTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import report_varb
from .. import gvarb

class pf_recovery(pf_recoveryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

    grid_rows,grid_cols = anvil.server.call('pf_recovery_report',gvarb.g_comcode)
    report_varb.g_pf_recovery_rows = grid_rows
    report_varb.g_pf_recovery_cols = grid_cols

    print("pf recovery grid cols: ",report_varb.g_pf_recovery_cols)
    print("pf recovery grid rows: ",report_varb.g_pf_recovery_rows)
    html_template = """
    <!DOCTYPE html>
    <html>
    
    <head>
        <title>PF Recovery Statement</title>
        <style>
    body {
        font-family: Arial, sans-serif;
        text-align: center;
        /* Center align the content */
    }

    h1 {
        font-size: 24px;
    }

    p {
        font-size: 16px;
    }

    table {
        width: 80%;
        /* Adjust the width as needed */
        margin: 20px auto;
        /* Center the table horizontally with 20px top and bottom margin */
        border-collapse: collapse;
    }

    th,
    td {
        border: 1px solid #000;
        padding: 8px;
        text-align: left;
    }

    .charges-container {
        text-align: left;
        /* Adjust margin-top as needed */
        width: 80%;
        margin: 20px auto; /* Adjust to match the left margin of the table */
    }
</style>

    </head>
    
    <body>
        <div class="content">
            <h1>{{ company_name }}</h1>
            <h4>{{ addr_line1 }}</h4>
            <h4>{{ addr_line2 }}</h4>
            <h4>{{ addr_line3 }}</h4>
            <h1>{{ report_head }}</h1>
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

        <h1>{{ summary_heading }}</h1>
        <div class="charges-container">
            <h4>1 > Total salary for PF [ ₹ ] - {{ report_head }}</h4>
            <h4> </h4>            
            <h4>2 > Total salary for FPF [ ₹ ] - {{ report_head }}</h4>
            <h4> </h4>            
            <h4>3 > Total employee PF [ ₹ ] - {{ report_head }}</h4>
            <h4> </h4>            
            <h4>4 > Total employer PF [ ₹ ] - {{ report_head }}</h4>
            <h4> </h4>            
            <h4>5 > Total employee FPF [ ₹ ] - {{ report_head }}</h4>
            <h4> </h4>            
            <h4>6 > Total employer FPF [ ₹ ] - {{ report_head }}</h4>
            <h4> </h4>            
            <h4>7 > Total admin charges [ ₹ ] - {{ report_head }}</h4>
            <h4> </h4>            
            <h4>8 > Total EDLI charges [ ₹ ] - {{ report_head }}</h4>
            <h4> </h4>            
            <h4>9 > Total mislenous charges [ ₹ ] - {{ report_head }}</h4>
            <h4> </h4>                
        </div>
    
    </body>
    
    </html>

    """

    self.html_content = anvil.server.call('pf_recovery_html',html_template,
                                          report_varb.g_pf_recovery_rows,report_varb.g_pf_recovery_cols,
                                          "PF Recovery statement for the month of "+gvarb.g_transdate.strftime("%B %Y").upper(),
                                          gvarb.g_comname,gvarb.g_comadd1,gvarb.g_comadd2,gvarb.g_comadd3,
                                         "PF summary for the month of "+gvarb.g_transdate.strftime("%B %Y").upper())
    self.html = self.html_content
