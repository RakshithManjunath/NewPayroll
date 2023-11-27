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

      /* Adjust the width of individual columns as needed */
        th:nth-child(1),
        td:nth-child(1) {
            width: 10%;
        }

        th:nth-child(2),
        td:nth-child(2) {
            width: 10%;
        }

        th:nth-child(3),
        td:nth-child(3) {
            width: 25%;
        }
        
        th:nth-child(4),
        td:nth-child(4) {
            width: 10%;
        }
        
        th:nth-child(5),
        td:nth-child(5) {
            width: 10%;
        }
        
        th:nth-child(6),
        td:nth-child(6) {
            width: 15%;
        }  
        th:nth-child(7),
        td:nth-child(7) {
            width: 10%;
        }  
        th:nth-child(8),
        td:nth-child(8) {
            width: 10%;
        } 
        th:nth-child(9),
        td:nth-child(9) {
            width: 20%;
        }        
        } 
        th:nth-child(10),
        td:nth-child(10) {
            width: 20%;
        }  
        } 
        th:nth-child(11),
        td:nth-child(11) {
            width: 10%;
        } 
        } 
        th:nth-child(12),
        td:nth-child(12) {
            width: 10%;
        }  
        
        
    .charges-container {
        text-align: left;
        /* Adjust margin-top as needed */
        width: 80%;
        margin: 20px auto; /* Adjust to match the left margin of the table */
    }

    button {
            padding: 10px;
            font-size: 16px;
            background-color: darkblue;
            color: white;
            border-radius: 20px; /* Adjust the value to control the roundness, making it oval-shaped */
           }

    

    .button-container {
            position: absolute;
            top: 10px;
            right: 10px;
        }
</style>

    </head>
    
    <body>
    <div id="back_btn" class="button-container">
        <button>  Main menu  </button>
    </div>
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
        <h1> </h1> 
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

        
    <script>
    $('#back_btn').on('click', function(e) {
    var linkElement = this;
    anvil.call(linkElement, "open_menu");
    e.preventDefault();   
  }); 
  </script>
    </body>
    </html>
    """

    self.html_content = anvil.server.call('pf_recovery_html',html_template,
                                          report_varb.g_pf_recovery_rows,report_varb.g_pf_recovery_cols,
                                          "PF Recovery statement for the month of "+gvarb.g_transdate.strftime("%B %Y").upper(),
                                          gvarb.g_comname,gvarb.g_comadd1,gvarb.g_comadd2,gvarb.g_comadd3,
                                         "PF summary for the month of "+gvarb.g_transdate.strftime("%B %Y").upper())
    self.html = self.html_content

  def open_menu(self, **kwargs):
    open_form('menu')

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pdf = anvil.server.call('download_report_recovery_pdf',self.html_content)
    download(pdf)

  def outlined_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    excel = anvil.server.call('download_report_recovery_excel',self.html_content,gvarb.g_comcode,gvarb.g_transdate)
    download(excel)

  def outlined_button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    csv = anvil.server.call('download_report_recovery_csv',self.html_content)
    download(csv)

