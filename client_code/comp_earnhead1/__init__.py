from ._anvil_designer import comp_earnhead1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .. import gvarb


class comp_earnhead1(comp_earnhead1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.refresh()

  def refresh(self):
    comp_details = anvil.server.call('comp_get_details', gvarb.g_comcode)

    ## HEAD1 ######   
    if comp_details['comp_earn_head1']!="":     
      self.label_1.text = comp_details['comp_earn_head1']
      self.label_1.border="solid"
      self.check_box_1.checked = comp_details['comp_earnhead1_pf']
      self.check_box_11.checked = comp_details['comp_earnhead1_esi']
      self.check_box_21.checked = comp_details['comp_earnhead1_pt']
      self.check_box_31.checked = comp_details['comp_earnhead1_ot']
      self.check_box_41.checked = comp_details['comp_earnhead1_it'] 
      self.check_box_51.checked = comp_details['comp_earnhead1_bonus']
    else:
      self.check_box_1.enabled = False
      self.check_box_11.enabled = False
      self.check_box_21.enabled = False
      self.check_box_31.enabled = False
      self.check_box_41.enabled = False
      self.check_box_51.enabled = False
      
    ## HEAD2 ###### 
    if comp_details['comp_earn_head2']!="":     
      self.label_2.text = comp_details['comp_earn_head2']
      self.label_2.border="solid"
      self.check_box_2.checked = comp_details['comp_earnhead2_pf']
      self.check_box_12.checked = comp_details['comp_earnhead2_esi']
      self.check_box_22.checked = comp_details['comp_earnhead2_pt']
      self.check_box_32.checked = comp_details['comp_earnhead2_ot'] 
      self.check_box_42.checked = comp_details['comp_earnhead2_it'] 
      self.check_box_52.checked = comp_details['comp_earnhead2_bonus']    
    else:
      self.check_box_2.enabled = False
      self.check_box_12.enabled = False
      self.check_box_22.enabled = False
      self.check_box_32.enabled = False
      self.check_box_42.enabled = False
      self.check_box_52.enabled = False

    ## HEAD3 ###### 
    if comp_details['comp_earn_head3']!="":     
      self.label_3.text = comp_details['comp_earn_head3']
      self.label_3.border="solid"
      self.check_box_3.checked = comp_details['comp_earnhead3_pf']
      self.check_box_13.checked = comp_details['comp_earnhead3_esi']
      self.check_box_23.checked = comp_details['comp_earnhead3_pt']
      self.check_box_33.checked = comp_details['comp_earnhead3_ot']    
      self.check_box_43.checked = comp_details['comp_earnhead3_it']
      self.check_box_53.checked = comp_details['comp_earnhead3_bonus']    
    else:
      self.check_box_3.enabled = False
      self.check_box_13.enabled = False
      self.check_box_23.enabled = False
      self.check_box_33.enabled = False
      self.check_box_43.enabled = False
      self.check_box_53.enabled = False      
      
    ## HEAD4 ###### 
    if comp_details['comp_earn_head4']!="":     
      self.label_4.text = comp_details['comp_earn_head4'] 
      self.label_4.border="solid"
      self.check_box_4.checked = comp_details['comp_earnhead4_pf']
      self.check_box_14.checked = comp_details['comp_earnhead4_esi']
      self.check_box_24.checked = comp_details['comp_earnhead4_pt']
      self.check_box_34.checked = comp_details['comp_earnhead4_ot']    
      self.check_box_44.checked = comp_details['comp_earnhead4_it']
      self.check_box_54.checked = comp_details['comp_earnhead4_bonus']
    else:
      self.check_box_4.enabled = False
      self.check_box_14.enabled = False
      self.check_box_24.enabled = False
      self.check_box_34.enabled = False
      self.check_box_44.enabled = False
      self.check_box_54.enabled = False   
      
    ## HEAD5 ###### 
    if comp_details['comp_earn_head5']!="":         
      self.label_5.text = comp_details['comp_earn_head5']
      self.label_5.border="solid"
      self.check_box_5.checked = comp_details['comp_earnhead5_pf']
      self.check_box_15.checked = comp_details['comp_earnhead5_esi']
      self.check_box_25.checked = comp_details['comp_earnhead5_pt']
      self.check_box_35.checked = comp_details['comp_earnhead5_ot']
      self.check_box_45.checked = comp_details['comp_earnhead5_it']
      self.check_box_55.checked = comp_details['comp_earnhead5_bonus']
    else: 
      self.check_box_5.enabled = False
      self.check_box_15.enabled = False
      self.check_box_25.enabled = False
      self.check_box_35.enabled = False
      self.check_box_45.enabled = False
      self.check_box_55.enabled = False
      
    ## HEAD6 ######
    if comp_details['comp_earn_head6']!="":       
      self.label_6.text = comp_details['comp_earn_head6']
      self.label_6.border="solid"
      self.check_box_6.checked = comp_details['comp_earnhead6_pf']    
      self.check_box_16.checked = comp_details['comp_earnhead6_esi']
      self.check_box_26.checked = comp_details['comp_earnhead6_pt']
      self.check_box_36.checked = comp_details['comp_earnhead6_ot']
      self.check_box_46.checked = comp_details['comp_earnhead6_it']
      self.check_box_56.checked = comp_details['comp_earnhead6_bonus']
    else:  
      self.check_box_6.enabled = False
      self.check_box_16.enabled = False
      self.check_box_26.enabled = False
      self.check_box_36.enabled = False
      self.check_box_46.enabled = False
      self.check_box_56.enabled = False
      
    ## HEAD7 ######
    if comp_details['comp_earn_head7']!="":      
      self.label_7.text = comp_details['comp_earn_head7']
      self.label_7.border="solid"
      self.check_box_7.checked = comp_details['comp_earnhead7_pf']
      self.check_box_17.checked = comp_details['comp_earnhead7_esi']    
      self.check_box_27.checked = comp_details['comp_earnhead7_pt']
      self.check_box_37.checked = comp_details['comp_earnhead7_ot']
      self.check_box_47.checked = comp_details['comp_earnhead7_it']
      self.check_box_57.checked = comp_details['comp_earnhead7_bonus'] 
    else:
      self.check_box_7.enabled = False
      self.check_box_17.enabled = False
      self.check_box_27.enabled = False
      self.check_box_37.enabled = False
      self.check_box_47.enabled = False
      self.check_box_57.enabled = False
      
    ## HEAD8 ######   
    if comp_details['comp_earn_head8']!="":        
      self.label_8.text = comp_details['comp_earn_head8']
      self.label_8.border="solid"
      self.check_box_8.checked = comp_details['comp_earnhead8_pf']
      self.check_box_18.checked = comp_details['comp_earnhead8_esi']    
      self.check_box_28.checked = comp_details['comp_earnhead8_pt']
      self.check_box_38.checked = comp_details['comp_earnhead8_ot']
      self.check_box_48.checked = comp_details['comp_earnhead8_it']
      self.check_box_58.checked = comp_details['comp_earnhead8_bonus']    
    else:
      self.check_box_8.enabled = False
      self.check_box_18.enabled = False
      self.check_box_28.enabled = False
      self.check_box_38.enabled = False
      self.check_box_48.enabled = False
      self.check_box_58.enabled = False
      
    ## HEAD9 ###### 
    if comp_details['comp_earn_head9']!="":      
      self.label_9.text = comp_details['comp_earn_head9'] 
      self.label_9.border="solid"
      self.check_box_9.checked = comp_details['comp_earnhead9_pf']
      self.check_box_19.checked = comp_details['comp_earnhead9_esi']
      self.check_box_29.checked = comp_details['comp_earnhead9_pt']
      self.check_box_39.checked = comp_details['comp_earnhead9_ot']
      self.check_box_49.checked = comp_details['comp_earnhead9_it']    
      self.check_box_59.checked = comp_details['comp_earnhead9_bonus']    
    else:
      self.check_box_9.enabled = False
      self.check_box_19.enabled = False
      self.check_box_29.enabled = False
      self.check_box_39.enabled = False
      self.check_box_49.enabled = False
      self.check_box_59.enabled = False
      
    ## HEAD10 ######
    if comp_details['comp_earn_head10']!="":         
      self.label_10.text = comp_details['comp_earn_head10']
      self.label_10.border="solid"
      self.check_box_10.checked = comp_details['comp_earnhead10_pf']
      self.check_box_20.checked = comp_details['comp_earnhead10_esi']
      self.check_box_30.checked = comp_details['comp_earnhead10_pt']
      self.check_box_40.checked = comp_details['comp_earnhead10_ot'] 
      self.check_box_50.checked = comp_details['comp_earnhead10_it']
      self.check_box_60.checked = comp_details['comp_earnhead10_bonus']    
    else:
      self.check_box_10.enabled = False
      self.check_box_20.enabled = False
      self.check_box_30.enabled = False
      self.check_box_40.enabled = False
      self.check_box_50.enabled = False
      self.check_box_60.enabled = False
      
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('comp_earnhead1',gvarb.g_comcode,self.check_box_1.checked,self.check_box_2.checked,self.check_box_3.checked,
                      self.check_box_4.checked,self.check_box_5.checked,self.check_box_6.checked,self.check_box_7.checked,
                      self.check_box_8.checked,self.check_box_9.checked,self.check_box_10.checked,self.check_box_11.checked,
                      self.check_box_12.checked,self.check_box_13.checked,self.check_box_14.checked,self.check_box_15.checked,
                      self.check_box_16.checked,self.check_box_17.checked,self.check_box_18.checked,self.check_box_19.checked,
                      self.check_box_20.checked,self.check_box_21.checked,self.check_box_22.checked,self.check_box_23.checked,
                      self.check_box_24.checked,self.check_box_25.checked,self.check_box_26.checked,self.check_box_27.checked,
                      self.check_box_28.checked,self.check_box_29.checked,self.check_box_30.checked,self.check_box_31.checked,
                      self.check_box_32.checked,self.check_box_33.checked,self.check_box_34.checked,self.check_box_35.checked,
                      self.check_box_36.checked,self.check_box_37.checked,self.check_box_38.checked,self.check_box_39.checked,
                      self.check_box_40.checked,self.check_box_41.checked,self.check_box_42.checked,self.check_box_43.checked,
                      self.check_box_44.checked,self.check_box_45.checked,self.check_box_46.checked,self.check_box_47.checked,
                      self.check_box_48.checked,self.check_box_49.checked,self.check_box_50.checked,
                      self.check_box_51.checked,self.check_box_52.checked,self.check_box_53.checked,
                      self.check_box_54.checked,self.check_box_55.checked,self.check_box_56.checked,self.check_box_57.checked,
                      self.check_box_58.checked,self.check_box_59.checked,self.check_box_60.checked)

    self.refresh()
    
