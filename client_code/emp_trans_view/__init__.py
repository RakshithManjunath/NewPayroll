from ._anvil_designer import emp_trans_viewTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb
from datetime import datetime


class emp_trans_view(emp_trans_viewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.populate_custom_data_grid()
    ################ tried to convert date to indian format, not happening
    # modified_df = anvil.server.call('trans_get_all_details',gvarb.g_comcode)
    # for _, row in df.iterrows():
    #   # Create a dictionary to store the data for each row
    #   row_data = {}
    #   for column in df.columns:
    #       # Add data for each column dynamically
    #       row_data[column] = row[column]
  
    #   # Append the row_data dictionary to the RepeatingPanel
    #   self.repeating_panel.items.append(row_data)
    self.repeating_panel_1.items = anvil.server.call('trans_get_all_details',gvarb.g_comcode)
    
    if (gvarb.g_curmonyear == False):
      self.label_2.foreground = "#FF0000" 
    self.label_2.text = gvarb.g_comname+' '+gvarb.g_mode+" for the month of "+gvarb.g_transdate.strftime("%B %Y")

  def populate_custom_data_grid(self):
    # col = self.data_grid_1.columns
    columns = self.data_grid_1.columns
    print(columns)
    # print(columns, len(columns))
    comp_details = anvil.server.call('comp_get_details', gvarb.g_comcode)
    print(comp_details)
    
    columns[21]["title"] = comp_details['comp_leave_head1']
    columns[22]["title"] = comp_details['comp_leave_head2']
    columns[23]["title"] = comp_details['comp_leave_head3']  

    columns[26]["title"] = comp_details['comp_ded1'] 
    columns[27]["title"] =comp_details['comp_ded2']      
    columns[28]["title"] = comp_details['comp_ded3']     
    columns[29]["title"] = comp_details['comp_ded4']   

    columns[30]["title"] = comp_details['comp_loan_head1']  
    columns[31]["title"] = comp_details['comp_loan_head2']    

    columns[38]["title"] = comp_details['comp_earn_head1'] 
    columns[39]["title"] = 'Earned '+comp_details['comp_earn_head1'] 
    columns[40]["title"] = comp_details['comp_earn_head2'] 
    columns[41]["title"] = 'Earned '+comp_details['comp_earn_head2'] 
    columns[42]["title"] = comp_details['comp_earn_head3'] 
    columns[43]["title"] = 'Earned '+comp_details['comp_earn_head3'] 
    columns[44]["title"] = comp_details['comp_earn_head4'] 
    columns[45]["title"] = 'Earned '+comp_details['comp_earn_head4']     
    columns[46]["title"] = comp_details['comp_earn_head5'] 
    columns[47]["title"] = 'Earned '+comp_details['comp_earn_head5']     
    columns[48]["title"] = comp_details['comp_earn_head6']
    columns[49]["title"] = 'Earned '+comp_details['comp_earn_head6']        
    columns[50]["title"] = comp_details['comp_earn_head7'] 
    columns[51]["title"] = 'Earned '+comp_details['comp_earn_head7']        
    columns[52]["title"] = comp_details['comp_earn_head8'] 
    columns[53]["title"] = 'Earned '+comp_details['comp_earn_head8']        
    columns[54]["title"] = comp_details['comp_earn_head9'] 
    columns[55]["title"] = 'Earned '+comp_details['comp_earn_head9']         
    columns[56]["title"] = comp_details['comp_earn_head10'] 
    columns[57]["title"] = 'Earned '+comp_details['comp_earn_head10']  

    

    # Update the Data Grid with the modified column
    self.data_grid_1.columns = columns

    
    ######## Find the index value of acolumn in the DataGrid##############
    # # Specify the field name you want to check for
    #field_name = 'Trans Leave1'
    
  # for col in col:
  #   if (col["name"] == field_name):
  #     print(col["name"])
  #   else:
  #     pass

    # Specify the index of the column you want to change (e.g., column at index 2)
    #column_index_to_change = 2
    
    # Set the new header text for the specified column
    # new_header_text = gvarb.g_leave2
    # columns[3]["title"] = new_header_text
  
    # Update the Data Grid with the modified column
    #self.data_grid_1.columns = columns
    
  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    media_object = anvil.server.call('create_zaphod_pdf')
    anvil.media.download(media_object)





