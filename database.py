import sqlite3
connection = sqlite3.connect("tkinter_form.db") 
crsr = connection.cursor() 
'''sql_command = """CREATE TABLE Form_Entries(  
Firstname VARCHAR(50),  
Lastname VARCHAR(50),  
Rollnumber VARCHAR(50),
Emailid VARCHAR(30),  
Sex VARCHAR(30),  
DOB VARCHAR(30),
Country VARCHAR(30),
Institute VARCHAR(30),
C VARCHAR(10),
Cpp VARCHAR(10),
Ruby VARCHAR(10),
python VARCHAR(10),
Java VARCHAR(10),
Phonecode VARCHAR(10),
Mobileno VARCHAR(50),
Degree VARCHAR(30),
Cpi_percenatge REAL(30),
Class_12 REAL(30),
Class_10 REAL(30)
);"""
'''
cursor = connection.execute("SELECT * FROM Form_Entries") 
for row in cursor: 
   print (row) 
  
#crsr.execute(sql_command) 
connection.commit() 
connection.close() 