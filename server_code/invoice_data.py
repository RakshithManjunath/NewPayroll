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

#Data setting for invoice , Can be generated from Database or Excel ##
my_prod={1:['Hard Disk',80],2:['RAM',90],3:['Monitor',75],
         4:['CPU',55],5:['Keyboard',20],6:['Mouse',10],
         7:['Mother board',50],8:['Power Sypply',20],
         9:['Speaker',50],10:['Microphone',45]}
#sales table keeps the product id and quantity sold 
my_sale={1:2,3:2,7:1,4:3,6:5,5:3,2:1,9:1,10:3} # product id and quanity
