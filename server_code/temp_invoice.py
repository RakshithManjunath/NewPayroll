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

from reportlab.lib.units import inch
def my_temp(c):
    c.translate(inch,inch)
    c.setFont("Helvetica", 14)
    c.setStrokeColorRGB(0.1,0.8,0.1)
    c.setFillColorRGB(0,0,1) # font colour
    # c.drawImage('D:\\top2.jpg',-0.8*inch,9.3*inch)
    c.drawString(0, 9*inch, "Shop No : 1234, ABCD Road")
    c.drawString(0, 8.7*inch, "City Name: Mycity, ZIP : 12345")
    c.setFillColorRGB(0,0,0) # font colour
    c.line(0,8.6*inch,6.8*inch,8.6*inch)
    c.setFont("Helvetica", 8)
    c.drawString(6.0*inch,9.6*inch,'Page 1')
    
    c.setFont("Helvetica", 8)
    c.drawString(3*inch,9.6*inch,'Tax No :# ABC1234')
    c.setFillColorRGB(1,0,0) # font colour
    c.setFont("Times-Bold", 40)
    c.rotate(45) # rotate by 45 degree 
    c.setFillColorCMYK(0,0,0,0.08) # font colour CYAN, MAGENTA, YELLOW and BLACK
    c.setFont("Helvetica", 140) # font style and size
    c.drawString(2*inch, 1*inch, "SAMPLE") # String written 
    c.rotate(-45) # restore the rotation 
    c.setFillColorRGB(0,0,0) # font colour
    c.setFont("Times-Roman", 22)
    c.drawString(0.1*inch,8.3*inch,'Empcode')
    c.drawString(2.0*inch, 8.3*inch, 'Empname')
    c.drawString(5*inch,8.3*inch,'Pf sal')
    c.drawString(6.5*inch,8.3*inch,'Pf amt')
    c.setStrokeColorCMYK(0,0,0,1) # vertical line colour 
    c.line(5*inch,8.6*inch,5*inch,2.5*inch)# first vertical line
    c.line(1.9*inch,8.6*inch,1.9*inch,2.5*inch)
    c.line(6.5*inch,8.6*inch,6.5*inch,2.5*inch)# second vertical line
    # c.line(6.5*inch,8.3*inch,6.5*inch,2.7*inch)# third vertical line
    c.line(0.01*inch,2.5*inch,7*inch,2.5*inch)# horizontal line total
    return c

