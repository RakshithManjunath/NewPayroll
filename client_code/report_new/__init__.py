from ._anvil_designer import report_newTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb
from .. import report_varb

class report_new(report_newTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    if (gvarb.g_curmonyear == False):
      self.label_2.foreground = "#FF0000"
    self.label_2.text = (gvarb.g_comname+' '+gvarb.g_mode+" for the month of "+gvarb.g_transdate.strftime("%B %Y")).upper()
    ############################################################
    #comp_details = anvil.server.call('comp_get_details', '002')  
    ###########################################################
    comp_details = anvil.server.call('comp_get_details', gvarb.g_comcode)

    self.columns,self.unmodified_cols,emp_details_list, general_details_list, attendance_list, earnings_list, deductions_list = anvil.server.call('get_transaction_columns', comp_details,gvarb.g_comcode)
    print("Original cols: ", self.unmodified_cols)
    print("Modified cols: ", self.columns)

    # self.add_component(anvil.CheckBox(text="slno",checked=True,visible=False))

    self.col_panel = anvil.ColumnPanel()

    # flow_panel = anvil.FlowPanel()
    # self.col_panel.add_component(flow_panel)
    # for i in range(len(self.columns)):
    #   if self.columns[i] == 'Emp code' or self.columns[i] == 'Emp name' or self.columns[i] == 'Sl no':
    #     checkbox = CheckBox(text=self.columns[i], checked=True)  
    #     flow_panel.add_component(checkbox)
    #   else:
    #     checkbox = CheckBox(text=self.columns[i], checked=False)  
    #     flow_panel.add_component(checkbox)
    # # self.add_component(flow_panel)
    # self.add_component(self.col_panel)
    
    flow_panel_emp_details = anvil.FlowPanel()
    self.col_panel.add_component(flow_panel_emp_details)
    for name in emp_details_list:
      checkbox = anvil.CheckBox(text=name,checked=True)
      flow_panel_emp_details.add_component(checkbox)

    flow_panel_general_details = anvil.FlowPanel()
    flow_panel_general_details.add_component(anvil.Label(text="General"))
    flow_panel_general_details.add_component(anvil.Spacer())
    self.col_panel.add_component(flow_panel_general_details)
    for name in general_details_list:
      checkbox = anvil.CheckBox(text=name,checked=False)
      flow_panel_general_details.add_component(checkbox)

    flow_panel_attendance_details = anvil.FlowPanel()
    flow_panel_attendance_details.add_component(anvil.Label(text="Attendance"))
    flow_panel_attendance_details.add_component(anvil.Spacer())
    self.col_panel.add_component(flow_panel_attendance_details)
    for name in attendance_list:
      checkbox = anvil.CheckBox(text=name,checked=False)
      flow_panel_attendance_details.add_component(checkbox)

    flow_panel_earnings_details = anvil.FlowPanel()
    flow_panel_earnings_details.add_component(anvil.Label(text="Earings"))
    flow_panel_earnings_details.add_component(anvil.Spacer())
    self.col_panel.add_component(flow_panel_earnings_details)
    for name in  earnings_list:
      checkbox = anvil.CheckBox(text=name,checked=False)
      flow_panel_earnings_details.add_component(checkbox)    

    flow_panel_deduction_details = anvil.FlowPanel()
    flow_panel_deduction_details.add_component(anvil.Label(text="Deductions"))
    flow_panel_deduction_details.add_component(anvil.Spacer())
    self.col_panel.add_component(flow_panel_deduction_details)
    for name in deductions_list:
      checkbox = anvil.CheckBox(text=name,checked=False)
      flow_panel_deduction_details.add_component(checkbox)
    self.add_component(self.col_panel)

    
    # Dynamically create set all button
    button_set = anvil.Button(text="set all sellection")
    button_set.role = 'filled-button'
    self.add_component(button_set)
    button_set.set_event_handler('click', self.dynamic_button_set_click)
    
    # Dynamically create clear all button
    button_clear = anvil.Button(text="Clear all sellection")
    button_clear.role = 'filled-button'
    self.add_component(button_clear)
    button_clear.set_event_handler('click', self.dynamic_button_clear_click)

    # Dynamically create sellect button
    button = anvil.Button(text="Preview")
    button.role = 'filled-button'
    self.add_component(button)
    button.set_event_handler('click', self.dynamic_button_click)

  # Attach a click listener
  def dynamic_button_set_click(self, **event_args):
    all_components = self.get_components()
    
    col_panel = [component for component in all_components if isinstance(component, anvil.ColumnPanel)]
    flow_panel_with_boxes = col_panel[-1].get_components()
    all_flow_components = [component for component in flow_panel_with_boxes if isinstance(component, anvil.FlowPanel)]
    flow_component_with_checkboxes = all_flow_components[-1].get_components()
    only_checkboxes = [component for component in flow_component_with_checkboxes if isinstance(component, anvil.CheckBox)]
    for checkbox in only_checkboxes:
      checkbox.checked = True

  # Attach a click listener
  def dynamic_button_clear_click(self, **event_args):
    open_form('report_new')

  # Attach a click listener
  def dynamic_button_click(self, **event_args):
    # Your code to be executed when the button is clicked
    all_components = self.get_components()
    if isinstance(all_components[-1], anvil.DataGrid):
      all_components[-1].remove_from_parent()
    col_panel = [component for component in all_components if isinstance(component, anvil.ColumnPanel)]
    flow_panel_with_boxes = col_panel[-1].get_components()
    all_flow_components = [component for component in flow_panel_with_boxes if isinstance(component, anvil.FlowPanel)]
    flow_component_with_checkboxes = all_flow_components[-1].get_components()
    only_checkboxes = [component for component in flow_component_with_checkboxes if isinstance(component, anvil.CheckBox)]
    selected_boxes = []
    modified_col_names = []
    for checkbox in only_checkboxes:
      if checkbox.checked and checkbox.text not in self.unmodified_cols:
        print("Selected and not in og list: ",checkbox.text)
        pos = self.columns.index(checkbox.text)
        print("corresponding unmodified value ",self.unmodified_cols[pos])
        selected_boxes.append(self.unmodified_cols[pos])
        modified_col_names.append(checkbox.text)
      elif checkbox.checked and checkbox.text in self.unmodified_cols:
        selected_boxes.append(checkbox.text)
        modified_col_names.append(checkbox.text)
        
    ############################################
    # grid_rows, grid_cols = anvil.server.call('get_only_selected_trans_values', '002',selected_boxes,modified_col_names)
    ############################################
    grid_rows, grid_cols = anvil.server.call('get_only_selected_trans_values', gvarb.g_comcode,selected_boxes,modified_col_names)
    report_varb.g_grid_cols = grid_cols
    report_varb.g_grid_rows = grid_rows

    open_form('output_options')

    # self.add_component(output_options())

    # print("Grid rows: ", grid_rows)

    # print("Selected boxes:, ", selected_boxes)
    # grid = anvil.DataGrid()
    # grid.role = 'wide'
    # self.add_component(grid)
    # print(grid.get_components())
    # grid.columns = grid_cols
    # # grid.columns = selected_boxes

    # rp = anvil.RepeatingPanel(item_template=anvil.DataRowPanel)
    # rp.items = grid_rows
    # # Add the repeating panel to your data grid
    # grid.add_component(rp)
    # all_components = self.get_components()

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('menu')
