import csv # for csv parsing 
import sqlite3 
import re # for data formatting 

# Ammaar Saadat

# connects to the cell database. If the db doesn't exist, it will create one
con = sqlite3.connect('cell-count.db') 

# cursor for the db connection, allowing us to execute commands
cur = con.cursor()

# 1) query following - all melanoma PBMC samples at time_from_treatment_start = 0 from patients who have been treated with miraclib. 
cur.execute("SELECT * FROM cells WHERE condition = 'melanoma' AND sample_type = 'PBMC' AND treatment = 'miraclib' AND time_from_treatment_start = '0'")