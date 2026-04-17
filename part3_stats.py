import csv # for csv parsing 
import sqlite3 
import re # for data formatting 


# connects to the cell database. If the db doesn't exist, it will create one
con = sqlite3.connect('cell-count.db') 

# cursor for the db connection, allowing us to execute commands
cur = con.cursor()

