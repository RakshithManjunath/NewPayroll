import anvil.files
from anvil.files import data_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd
import file_path
import io
import base64

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
@anvil.server.callable
def just_test():
  # Access the data table
  cols = app_tables.transaction.list_columns()

  #print(cols)
  
  # # Specify the field name you want to check for
  field_name = 'xxxx'
  field_type = 'bool'

  for col in cols:
    if ((col["name"] == field_name) and (col["type"] == field_type)):
      print(col["name"])
      print(col["type"])
    else:
      pass
    #      print("fail")
    
    # 'type': 'number' for numeric
    # 'type': 'string' for text
    # 'type': 'bool' for logical
    # 'type': 'date' for date

    #  # field_type = anvil.server.app_tables.transaction.TextColumnType()  # You can choose the appropriate column type (e.g., Text, Date, Number)
  #    app_tables.transaction.add_column(field_name, field_type)
  
    # # Get a list of all column names in the data table
    #   # all_column_names = data_table.get_columns()
    #   all_column_names = cols(0)
  
  
@anvil.server.callable
def test_add_column():
  app_tables.transaction.update(columns={"age": int},all=True)

def get_media_from_bytes_image(bytes_data,filename):
  if bytes_data:
    media_bytes = base64.b64decode(bytes_data)
    return anvil.BlobMedia('image/jpeg', media_bytes, name=filename + ".png")
  else:
    return None

def get_media_from_bytes_pdf(bytes_data,filename):
  if bytes_data:
    media_bytes = base64.b64decode(bytes_data)
    return anvil.BlobMedia('application/pdf', media_bytes, name=filename + ".pdf")
  else:
    return None

@anvil.server.callable
def import_test_csv():
  with open(file_path.test_path, "r") as f:
    dtype_mapping = {
      'name':str,
      'age':int,
      'salary':float,
      'gender':bool
    }
    df = pd.read_csv(f, dtype=dtype_mapping,keep_default_na=False)
    for _, row in df.iterrows():
      print(row)
      # Create a media object from the 'photo_bytes' column
      photo_media = get_media_from_bytes_image(row['photo'],row['name'])  # Replace with the actual function

      pdf_media = get_media_from_bytes_pdf(row['pdf'],row['name'])
      
      # Remove the 'photo_bytes' column from the row
      row = row.drop('photo')
      row = row.drop('pdf')
      
      # Convert 'dob' to a datetime.date object
      dob = pd.to_datetime(row['dob']).date()
      
      # Add the row to the Anvil data table
      app_tables.test_table.add_row(
          name=row['name'],
          age=row['age'],
          salary=row['salary'],
          gender=row['gender'],
          dob=dob,  # Use the converted 'dob'
          photo=photo_media,
          pdf=pdf_media
      )
    # df['dob'] = pd.to_datetime(df['dob']).dt.date
    # key_to_ignore = 'ID'
    # ignored_dict = {key: value for key, value in df.items() if key != key_to_ignore}
    # ignored_dict = pd.DataFrame(ignored_dict)
    # for d in ignored_dict.to_dict(orient="records"):
    #   print(d)
    #   app_tables.test_table.add_row(**d)

def get_media_bytes(media_object):
  if media_object:
    return base64.b64encode(media_object.get_bytes()).decode('utf-8')
  else:
    return None

@anvil.server.callable
def get_all_test_download():
  data_table = app_tables.test_table.search()
  csv_rows = []
  gender = None
  
  for row in data_table:
    if row['gender'] == False:
      gender = 0
    elif row['gender'] == True:
      gender = 1
    elif row['gender'] == None:
      gender = 0
    photo_bytes = get_media_bytes(row['photo'])
    pdf_bytes = get_media_bytes(row['pdf'])
    csv_row = [row["name"], row["age"], row['salary'],gender,row['dob'],photo_bytes,pdf_bytes]
    csv_rows.append(csv_row)
  df = pd.DataFrame(csv_rows, columns=["name","age","salary","gender","dob","photo","pdf"])
  df.to_csv('/tmp/test_table.csv',index=False)
  df_media = anvil.media.from_file('/tmp/test_table.csv', 'csv', 'test_table.csv')
  return df_media