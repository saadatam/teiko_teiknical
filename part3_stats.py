import csv # for csv parsing 
import sqlite3 
import re # for data formatting 


# connects to the cell database. If the db doesn't exist, it will create one
con = sqlite3.connect('cell-count.db') 

# cursor for the db connection, allowing us to execute commands
cur = con.cursor()

# 1) get ids for patients from freq table of those who have miraclib + respond via joining a condition from cells, 
#       then pipe into freq table for frequencies. 
# 2) repeat process but for non-responders 

# gather data to plot for responders
cur.execute("SELECT fr1.population, fr1.percentage FROM freq fr1 JOIN cells c1 ON fr1.sample = c1.sample WHERE c1.condition = 'melanoma' AND c1.treatment = 'miraclib' AND c1.response = 'yes' AND c1.sample_type = 'PBMC' ORDER BY fr1.population;")
responders = cur.fetchall()

# gather data to plot for NON-responders
cur.execute("SELECT fr1.population, fr1.percentage FROM freq fr1 JOIN cells c1 ON fr1.sample = c1.sample WHERE c1.condition = 'melanoma' AND c1.treatment = 'miraclib' AND c1.response = 'no' AND c1.sample_type = 'PBMC' ORDER BY fr1.population;")
non_responders = cur.fetchall()

# immune cell categorization, will help in plotting. 
labels = ["b_cell", "cd8_t_cell", "cd4_t_cell", "nk_cell", "monocyte"]
resp_dict = {}
non_resp_dict = {}
# populate 
for row in responders:
    resp_dict.setdefault(row[0], []).extend(row[1])
for row in non_responders:
    non_resp_dict.setdefault(row[0], []).extend(row[1])

for label in labels: 
    # TODO:plot the immune cell, + report
    resp_dict[label]
    non_resp_dict[label]